# Gunicorn vs Runserver Benchmark

| Server | User | Requests/sec | Mean time/request (ms) | Max RSS (MB) | Avg RSS (MB) |
| --- | --- | ---: | ---: | ---: | ---: |
| runserver | customer_1 | 111.75 | 447.409 | 19.47 | 0.4 |
| gunicorn | customer_1 | 204.42 | 244.599 | 15.45 | 0.84 |

JSON: gunicorn_vs_runserver.json