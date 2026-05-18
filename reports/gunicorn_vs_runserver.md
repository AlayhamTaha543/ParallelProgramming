# Gunicorn vs Runserver Benchmark

| Server | User | Requests/sec | Mean time/request (ms) | Max RSS (MB) | Avg RSS (MB) |
| --- | --- | ---: | ---: | ---: | ---: |
| runserver | customer_1 | 111.44 | 448.653 | 19.32 | 0.4 |
| gunicorn | customer_1 | 199.51 | 250.608 | 15.48 | 0.82 |

JSON: gunicorn_vs_runserver.json