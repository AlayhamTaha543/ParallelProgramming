#!/usr/bin/env python3

"""Benchmark Django runserver vs Gunicorn and save a comparison report.

The script starts each server, runs the same ApacheBench workload, samples
memory while the load is in progress, and writes JSON plus Markdown reports
under the chosen output directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import threading
import time
import urllib.request
import urllib.error
from urllib.parse import urlsplit
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class BenchmarkResult:
    name: str
    username: str | None
    command: str
    url: str
    requests: int
    concurrency: int
    requests_per_second: float | None
    mean_time_per_request_ms: float | None
    total_time_s: float
    max_rss_mb: float
    avg_rss_mb: float
    memory_samples: list[dict[str, float]]
    ab_output: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare memory usage and response time for runserver and Gunicorn."
    )
    parser.add_argument("--requests", type=int, default=2000)
    parser.add_argument("--concurrency", type=int, default=50)
    parser.add_argument(
        "--url-path",
        default="/admin/login/",
        help="Path to benchmark on each server, default: /admin/login/",
    )
    parser.add_argument(
        "--output-dir",
        default="reports",
        help="Directory where comparison reports are written.",
    )
    parser.add_argument(
        "--wait-timeout",
        type=int,
        default=60,
        help="Seconds to wait for each server to become reachable.",
    )
    parser.add_argument("--method", choices=["GET", "POST"], default="GET")
    parser.add_argument("--post-file", help="Path to file with POST body (used when --method=POST)")
    parser.add_argument("--content-type", default="application/json", help="Content-Type for POST body")
    parser.add_argument(
        "--header",
        action="append",
        default=[],
        help="Extra HTTP header to pass to AB, e.g. 'Authorization: Bearer <token>' (can be repeated)",
    )
    return parser.parse_args()


def wait_for_url(url: str, timeout: int) -> None:
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=3) as response:
                if 200 <= response.status < 500:
                    return
        except urllib.error.HTTPError as he:
            # Treat HTTP responses with status < 500 (e.g. 401 Unauthorized)
            # as a valid reachable server - proceed to next steps (login, etc.).
            if getattr(he, 'code', 500) < 500:
                return
            last_error = he
        except Exception as exc:  # noqa: BLE001 - retry loop intentionally swallows transient failures
            last_error = exc
        time.sleep(1)
    raise RuntimeError(f"Timed out waiting for {url}: {last_error}")


def sample_memory_mb(pattern: str) -> float:
    pgrep = subprocess.run(
        ["pgrep", "-f", pattern],
        capture_output=True,
        text=True,
        check=False,
    )
    if pgrep.returncode != 0:
        return 0.0

    pids = [pid for pid in pgrep.stdout.split() if pid.strip()]
    if not pids:
        return 0.0

    ps = subprocess.run(
        ["ps", "-o", "rss=", "-p", ",".join(pids)],
        capture_output=True,
        text=True,
        check=False,
    )
    rss_kb = 0
    for line in ps.stdout.splitlines():
        line = line.strip()
        if line.isdigit():
            rss_kb += int(line)
    return rss_kb / 1024.0


def sample_memory(pattern: str, stop_event: threading.Event, samples: list[dict[str, float]]) -> None:
    while not stop_event.is_set():
        samples.append({"ts": time.time(), "rss_mb": sample_memory_mb(pattern)})
        time.sleep(1)


def run_ab(url: str, requests: int, concurrency: int, method: str = "GET", post_file: str | None = None, content_type: str = "application/json", headers: list[str] | None = None) -> tuple[dict[str, float | None], str, float]:
    start = time.perf_counter()
    cmd = ["ab", "-n", str(requests), "-c", str(concurrency)]
    if method == "POST":
        if not post_file:
            raise RuntimeError("POST method requires --post-file to be specified")
        cmd += ["-p", post_file, "-T", content_type]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(url)
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    elapsed = time.perf_counter() - start
    output = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")

    rps_match = re.search(r"Requests per second:\s+([0-9.]+)", output)
    tpr_match = re.search(r"Time per request:\s+([0-9.]+)\s+\[ms\]\s+\(mean\)", output)

    metrics = {
        "requests_per_second": float(rps_match.group(1)) if rps_match else None,
        "mean_time_per_request_ms": float(tpr_match.group(1)) if tpr_match else None,
    }
    return metrics, output, elapsed


def start_process(command: str) -> subprocess.Popen[str]:
    return subprocess.Popen(
        command,
        shell=True,
        cwd=PROJECT_ROOT,
        preexec_fn=os.setsid,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def stop_process(proc: subprocess.Popen[str] | None) -> None:
    if proc is None:
        return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
        proc.wait(timeout=10)
    except Exception:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except Exception:
            pass


def benchmark_server(name: str, command: str, url: str, requests: int, concurrency: int, wait_timeout: int) -> BenchmarkResult:
    proc = start_process(command)
    try:
        wait_for_url(url, wait_timeout)
        memory_samples: list[dict[str, float]] = []
        stop_event = threading.Event()
        sampler = threading.Thread(target=sample_memory, args=(command, stop_event, memory_samples), daemon=True)
        sampler.start()
        # respect POST options from environment variables if present
        method = os.getenv("BENCH_METHOD", "GET")
        post_file = os.getenv("BENCH_POST_FILE")
        content_type = os.getenv("BENCH_CONTENT_TYPE", "application/json")
        headers_env = os.getenv("BENCH_HEADERS")
        headers = headers_env.split("||") if headers_env else []
        login_path = os.getenv("BENCH_LOGIN_PATH", "/api/users/login/")

        username = None
        password = None
        if os.getenv("BENCH_AUTO_LOGIN") == "1":
            default_username = os.getenv("BENCH_AUTH_USERNAME", "customer_1")
            default_password = os.getenv("BENCH_AUTH_PASSWORD", "Pass12345!")
            if name == "runserver":
                username = os.getenv("BENCH_RUNSERVER_USERNAME", default_username)
                password = os.getenv("BENCH_RUNSERVER_PASSWORD", default_password)
            else:
                username = os.getenv("BENCH_GUNICORN_USERNAME", default_username)
                password = os.getenv("BENCH_GUNICORN_PASSWORD", default_password)

        # Optionally obtain JWT token automatically from the login endpoint
        if username and password:
            parts = urlsplit(url)
            login_endpoint = f"{parts.scheme}://{parts.netloc}{login_path}"
            try:
                data = json.dumps({"username": username, "password": password}).encode("utf-8")
                req = urllib.request.Request(
                    login_endpoint,
                    data=data,
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    body = json.load(resp)
                    token = body.get('access') or body.get('token') or body.get('access_token')
                    if token:
                        headers = headers + [f"Authorization: Bearer {token}"]
            except Exception as exc:  # non-fatal; fallback to provided headers
                print(f"Warning: auto-login failed: {exc}")

        metrics, ab_output, total_time_s = run_ab(url, requests, concurrency, method=method, post_file=post_file, content_type=content_type, headers=headers)
        stop_event.set()
        sampler.join(timeout=5)

        rss_values = [sample["rss_mb"] for sample in memory_samples]
        max_rss_mb = max(rss_values) if rss_values else 0.0
        avg_rss_mb = sum(rss_values) / len(rss_values) if rss_values else 0.0

        return BenchmarkResult(
            name=name,
            username=username,
            command=command,
            url=url,
            requests=requests,
            concurrency=concurrency,
            requests_per_second=metrics["requests_per_second"],
            mean_time_per_request_ms=metrics["mean_time_per_request_ms"],
            total_time_s=total_time_s,
            max_rss_mb=max_rss_mb,
            avg_rss_mb=avg_rss_mb,
            memory_samples=memory_samples,
            ab_output=ab_output,
        )
    finally:
        stop_process(proc)


def write_report(results: list[BenchmarkResult], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "gunicorn_vs_runserver.json"
    md_path = output_dir / "gunicorn_vs_runserver.md"

    payload = {"generated_at": time.time(), "results": [asdict(result) for result in results]}
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = [
        "# Gunicorn vs Runserver Benchmark",
        "",
        "| Server | User | Requests/sec | Mean time/request (ms) | Max RSS (MB) | Avg RSS (MB) |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for result in results:
        lines.append(
            f"| {result.name} | {result.username or 'n/a'} | {result.requests_per_second or 'n/a'} | "
            f"{result.mean_time_per_request_ms or 'n/a'} | {round(result.max_rss_mb, 2)} | {round(result.avg_rss_mb, 2)} |"
        )
    lines.append("")
    lines.append(f"JSON: {json_path.name}")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    return json_path, md_path


def main() -> int:
    args = parse_args()
    url = f"http://127.0.0.1:8000{args.url_path}"
    gunicorn_url = f"http://127.0.0.1:8004{args.url_path}"

    results = [
        benchmark_server(
            name="runserver",
            command="pipenv run python manage.py runserver 127.0.0.1:8000",
            url=url,
            requests=args.requests,
            concurrency=args.concurrency,
            wait_timeout=args.wait_timeout,
        ),
        benchmark_server(
            name="gunicorn",
            command="pipenv run gunicorn ecommerce.wsgi:application --bind 127.0.0.1:8004 --workers 3 --threads 2",
            url=gunicorn_url,
            requests=args.requests,
            concurrency=args.concurrency,
            wait_timeout=args.wait_timeout,
        ),
    ]

    json_path, md_path = write_report(results, Path(args.output_dir))
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())