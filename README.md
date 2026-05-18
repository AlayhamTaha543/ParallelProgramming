# ParallelProgramming

## Run with Docker and Gunicorn

Start the stack with:

```bash
docker-compose up --build -d
```

The Django app is exposed on port `8001` to avoid conflicts with a local service that may already be using `8000`.

Open:

```bash
http://localhost:8001/
```

If you need a different host port, change the `web` service mapping in `docker-compose.yml`.

## Compare Gunicorn vs Native Django

Run the benchmark script to measure response time and memory usage for both servers. It starts each server, runs the same ApacheBench workload, and saves the results in `reports/`.

```bash
pipenv run python scripts/benchmark_compare.py
```

The script writes:

- `reports/gunicorn_vs_runserver.json`
- `reports/gunicorn_vs_runserver.md`

You can adjust the workload with `--requests`, `--concurrency`, and `--url-path`.