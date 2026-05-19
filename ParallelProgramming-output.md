# 📁 PROJECT EXPORT FOR LLMs

## 📊 Project Information

- **Project Name**: `ParallelProgramming`
- **Generated On**: 2026-05-18 12:59:18 (Asia/Damascus / GMT+03:00)
- **Total Files Processed**: 117
- **Export Tool**: Easy Whole Project to Single Text File for LLMs v1.1.0
- **Tool Author**: Jota / José Guilherme Pandolfi

### ⚙️ Export Configuration

| Setting | Value |
|---------|-------|
| Language | `en` |
| Max File Size | `1 MB` |
| Include Hidden Files | `false` |
| Output Format | `both` |

## 🌳 Project Structure

```
├── 📁 benchmark/
│   ├── 📄 benchmark_results.txt (8.66 KB)
│   ├── 📄 locustfile_simple.py (2.9 KB)
│   ├── 📄 locustfile.py (2.75 KB)
│   ├── 📄 probe_backends.py (2.31 KB)
│   ├── 📄 probe_concurrent.py (3.5 KB)
│   ├── 📄 probe_long_requests.py (4.78 KB)
│   ├── 📄 probe_sequence.py (1.54 KB)
│   ├── 📄 run_benchmark_with_metrics.ps1 (3.24 KB)
│   └── 📄 run_benchmark.ps1 (823 B)
├── 📁 cart/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   └── 📄 0001_initial.py (871 B)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (93 B)
│   ├── 📄 apps.py (88 B)
│   ├── 📄 models.py (419 B)
│   ├── 📄 permissions.py (361 B)
│   ├── 📄 serializers.py (256 B)
│   ├── 📄 tests.py (1.02 KB)
│   ├── 📄 urls.py (303 B)
│   └── 📄 views.py (646 B)
├── 📁 cart_items/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 0001_initial.py (1.05 KB)
│   │   └── 📄 0002_cartitem_total_price.py (433 B)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (101 B)
│   ├── 📄 apps.py (99 B)
│   ├── 📄 models.py (919 B)
│   ├── 📄 permissions.py (370 B)
│   ├── 📄 serializers.py (267 B)
│   ├── 📄 tests.py (2.48 KB)
│   └── 📄 views.py (1.69 KB)
├── 📁 ecommerce/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-314.pyc (199 B)
│   │   ├── 📄 settings.cpython-314.pyc (2.75 KB)
│   │   └── 📄 urls.cpython-314.pyc (690 B)
│   ├── 📄 __init__.py
│   ├── 📄 asgi.py (411 B)
│   ├── 📄 middleware.py (706 B)
│   ├── 📄 settings.py (4.24 KB)
│   ├── 📄 urls.py (324 B)
│   └── 📄 wsgi.py (411 B)
├── 📁 nginx/
│   ├── 📄 least-connections.conf (549 B)
│   └── 📄 round-robin.conf (528 B)
├── 📁 order/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 0001_initial.py (1.17 KB)
│   │   └── 📄 0002_alter_order_store.py (554 B)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (95 B)
│   ├── 📄 apps.py (90 B)
│   ├── 📄 models.py (913 B)
│   ├── 📄 permissions.py (812 B)
│   ├── 📄 serializers.py (334 B)
│   ├── 📄 tests.py (4.92 KB)
│   ├── 📄 urls.py (542 B)
│   └── 📄 views.py (3.15 KB)
├── 📁 order_items/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   └── 📄 0001_initial.py (1.06 KB)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (103 B)
│   ├── 📄 apps.py (101 B)
│   ├── 📄 models.py (657 B)
│   ├── 📄 permissions.py (766 B)
│   ├── 📄 serializers.py (253 B)
│   ├── 📄 tests.py (5.01 KB)
│   └── 📄 views.py (1.54 KB)
├── 📁 payments/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   └── 📄 0001_initial.py (967 B)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (66 B)
│   ├── 📄 apps.py (96 B)
│   ├── 📄 models.py (691 B)
│   ├── 📄 permissions.py (832 B)
│   ├── 📄 serializers.py (272 B)
│   ├── 📄 tests.py (1.88 KB)
│   └── 📄 views.py (1.99 KB)
├── 📁 products/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   └── 📄 0001_initial.py (993 B)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (66 B)
│   ├── 📄 apps.py (96 B)
│   ├── 📄 models.py (499 B)
│   ├── 📄 permission.py (543 B)
│   ├── 📄 serializers.py (248 B)
│   ├── 📄 tests.py (63 B)
│   └── 📄 views.py (980 B)
├── 📁 store/
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   └── 📄 0001_initial.py (917 B)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (66 B)
│   ├── 📄 apps.py (90 B)
│   ├── 📄 models.py (454 B)
│   ├── 📄 permissions.py (531 B)
│   ├── 📄 serializers.py (228 B)
│   ├── 📄 tests.py (63 B)
│   ├── 📄 urls.py (440 B)
│   └── 📄 views.py (522 B)
├── 📁 users/
│   ├── 📁 management/
│   │   └── 📁 commands/
│   │       ├── 📁 __pycache__/
│   │       └── 📄 seed_benchmark_data.py (2.03 KB)
│   ├── 📁 migrations/
│   │   ├── 📄 __init__.py
│   │   └── 📄 0001_initial.py (2.97 KB)
│   ├── 📄 __init__.py
│   ├── 📄 admin.py (66 B)
│   ├── 📄 apps.py (90 B)
│   ├── 📄 models.py (606 B)
│   ├── 📄 serializers.py (809 B)
│   ├── 📄 tests.py (63 B)
│   ├── 📄 urls.py (380 B)
│   └── 📄 views.py (876 B)
├── 📄 benchmark_context.json (59 B)
├── 📄 db.sqlite3 (700 KB)
├── 📄 docker-compose.lb.yml (2.08 KB)
├── 📄 docker-compose.least.yml (2.18 KB)
├── 📄 docker-compose.yml (859 B)
├── 📄 Dockerfile (445 B)
├── 📄 manage.py (687 B)
├── 📄 Pipfile (336 B)
├── 📄 Pipfile.lock (148.2 KB)
├── 📄 README.md (2.61 KB)
└── 📄 requirements.txt (188 B)
```

## 📑 Table of Contents

**Project Files:**

- [📄 benchmark/benchmark_results.txt](#📄-benchmark-benchmark-results-txt)
- [📄 benchmark/locustfile_simple.py](#📄-benchmark-locustfile-simple-py)
- [📄 benchmark/locustfile.py](#📄-benchmark-locustfile-py)
- [📄 benchmark/probe_backends.py](#📄-benchmark-probe-backends-py)
- [📄 benchmark/probe_concurrent.py](#📄-benchmark-probe-concurrent-py)
- [📄 benchmark/probe_long_requests.py](#📄-benchmark-probe-long-requests-py)
- [📄 benchmark/probe_sequence.py](#📄-benchmark-probe-sequence-py)
- [📄 benchmark/run_benchmark_with_metrics.ps1](#📄-benchmark-run-benchmark-with-metrics-ps1)
- [📄 benchmark/run_benchmark.ps1](#📄-benchmark-run-benchmark-ps1)
- [📄 cart/migrations/__init__.py](#📄-cart-migrations-init-py)
- [📄 cart/migrations/0001_initial.py](#📄-cart-migrations-0001-initial-py)
- [📄 cart/__init__.py](#📄-cart-init-py)
- [📄 cart/admin.py](#📄-cart-admin-py)
- [📄 cart/apps.py](#📄-cart-apps-py)
- [📄 cart/models.py](#📄-cart-models-py)
- [📄 cart/permissions.py](#📄-cart-permissions-py)
- [📄 cart/serializers.py](#📄-cart-serializers-py)
- [📄 cart/tests.py](#📄-cart-tests-py)
- [📄 cart/urls.py](#📄-cart-urls-py)
- [📄 cart/views.py](#📄-cart-views-py)
- [📄 cart_items/migrations/__init__.py](#📄-cart-items-migrations-init-py)
- [📄 cart_items/migrations/0001_initial.py](#📄-cart-items-migrations-0001-initial-py)
- [📄 cart_items/migrations/0002_cartitem_total_price.py](#📄-cart-items-migrations-0002-cartitem-total-price-py)
- [📄 cart_items/__init__.py](#📄-cart-items-init-py)
- [📄 cart_items/admin.py](#📄-cart-items-admin-py)
- [📄 cart_items/apps.py](#📄-cart-items-apps-py)
- [📄 cart_items/models.py](#📄-cart-items-models-py)
- [📄 cart_items/permissions.py](#📄-cart-items-permissions-py)
- [📄 cart_items/serializers.py](#📄-cart-items-serializers-py)
- [📄 cart_items/tests.py](#📄-cart-items-tests-py)
- [📄 cart_items/views.py](#📄-cart-items-views-py)
- [📄 ecommerce/__init__.py](#📄-ecommerce-init-py)
- [📄 ecommerce/asgi.py](#📄-ecommerce-asgi-py)
- [📄 ecommerce/middleware.py](#📄-ecommerce-middleware-py)
- [📄 ecommerce/settings.py](#📄-ecommerce-settings-py)
- [📄 ecommerce/urls.py](#📄-ecommerce-urls-py)
- [📄 ecommerce/wsgi.py](#📄-ecommerce-wsgi-py)
- [📄 nginx/least-connections.conf](#📄-nginx-least-connections-conf)
- [📄 nginx/round-robin.conf](#📄-nginx-round-robin-conf)
- [📄 order/migrations/__init__.py](#📄-order-migrations-init-py)
- [📄 order/migrations/0001_initial.py](#📄-order-migrations-0001-initial-py)
- [📄 order/migrations/0002_alter_order_store.py](#📄-order-migrations-0002-alter-order-store-py)
- [📄 order/__init__.py](#📄-order-init-py)
- [📄 order/admin.py](#📄-order-admin-py)
- [📄 order/apps.py](#📄-order-apps-py)
- [📄 order/models.py](#📄-order-models-py)
- [📄 order/permissions.py](#📄-order-permissions-py)
- [📄 order/serializers.py](#📄-order-serializers-py)
- [📄 order/tests.py](#📄-order-tests-py)
- [📄 order/urls.py](#📄-order-urls-py)
- [📄 order/views.py](#📄-order-views-py)
- [📄 order_items/migrations/__init__.py](#📄-order-items-migrations-init-py)
- [📄 order_items/migrations/0001_initial.py](#📄-order-items-migrations-0001-initial-py)
- [📄 order_items/__init__.py](#📄-order-items-init-py)
- [📄 order_items/admin.py](#📄-order-items-admin-py)
- [📄 order_items/apps.py](#📄-order-items-apps-py)
- [📄 order_items/models.py](#📄-order-items-models-py)
- [📄 order_items/permissions.py](#📄-order-items-permissions-py)
- [📄 order_items/serializers.py](#📄-order-items-serializers-py)
- [📄 order_items/tests.py](#📄-order-items-tests-py)
- [📄 order_items/views.py](#📄-order-items-views-py)
- [📄 payments/migrations/__init__.py](#📄-payments-migrations-init-py)
- [📄 payments/migrations/0001_initial.py](#📄-payments-migrations-0001-initial-py)
- [📄 payments/__init__.py](#📄-payments-init-py)
- [📄 payments/admin.py](#📄-payments-admin-py)
- [📄 payments/apps.py](#📄-payments-apps-py)
- [📄 payments/models.py](#📄-payments-models-py)
- [📄 payments/permissions.py](#📄-payments-permissions-py)
- [📄 payments/serializers.py](#📄-payments-serializers-py)
- [📄 payments/tests.py](#📄-payments-tests-py)
- [📄 payments/views.py](#📄-payments-views-py)
- [📄 products/migrations/__init__.py](#📄-products-migrations-init-py)
- [📄 products/migrations/0001_initial.py](#📄-products-migrations-0001-initial-py)
- [📄 products/__init__.py](#📄-products-init-py)
- [📄 products/admin.py](#📄-products-admin-py)
- [📄 products/apps.py](#📄-products-apps-py)
- [📄 products/models.py](#📄-products-models-py)
- [📄 products/permission.py](#📄-products-permission-py)
- [📄 products/serializers.py](#📄-products-serializers-py)
- [📄 products/tests.py](#📄-products-tests-py)
- [📄 products/views.py](#📄-products-views-py)
- [📄 store/migrations/__init__.py](#📄-store-migrations-init-py)
- [📄 store/migrations/0001_initial.py](#📄-store-migrations-0001-initial-py)
- [📄 store/__init__.py](#📄-store-init-py)
- [📄 store/admin.py](#📄-store-admin-py)
- [📄 store/apps.py](#📄-store-apps-py)
- [📄 store/models.py](#📄-store-models-py)
- [📄 store/permissions.py](#📄-store-permissions-py)
- [📄 store/serializers.py](#📄-store-serializers-py)
- [📄 store/tests.py](#📄-store-tests-py)
- [📄 store/urls.py](#📄-store-urls-py)
- [📄 store/views.py](#📄-store-views-py)
- [📄 users/management/commands/seed_benchmark_data.py](#📄-users-management-commands-seed-benchmark-data-py)
- [📄 users/migrations/__init__.py](#📄-users-migrations-init-py)
- [📄 users/migrations/0001_initial.py](#📄-users-migrations-0001-initial-py)
- [📄 users/__init__.py](#📄-users-init-py)
- [📄 users/admin.py](#📄-users-admin-py)
- [📄 users/apps.py](#📄-users-apps-py)
- [📄 users/models.py](#📄-users-models-py)
- [📄 users/serializers.py](#📄-users-serializers-py)
- [📄 users/tests.py](#📄-users-tests-py)
- [📄 users/urls.py](#📄-users-urls-py)
- [📄 users/views.py](#📄-users-views-py)
- [📄 benchmark_context.json](#📄-benchmark-context-json)
- [📄 docker-compose.lb.yml](#📄-docker-compose-lb-yml)
- [📄 docker-compose.least.yml](#📄-docker-compose-least-yml)
- [📄 docker-compose.yml](#📄-docker-compose-yml)
- [📄 manage.py](#📄-manage-py)
- [📄 Pipfile.lock](#📄-pipfile-lock)
- [📄 README.md](#📄-readme-md)
- [📄 requirements.txt](#📄-requirements-txt)

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| Total Files | 117 |
| Total Directories | 23 |
| Text Files | 111 |
| Binary Files | 6 |
| Total Size | 953.28 KB |

### 📄 File Types Distribution

| Extension | Count |
|-----------|-------|
| `.py` | 99 |
| `.pyc` | 3 |
| `.yml` | 3 |
| `.txt` | 2 |
| `.ps1` | 2 |
| `.conf` | 2 |
| `no extension` | 2 |
| `.json` | 1 |
| `.sqlite3` | 1 |
| `.lock` | 1 |
| `.md` | 1 |

## 💻 File Code Contents

### <a id="📄-benchmark-benchmark-results-txt"></a>📄 `benchmark/benchmark_results.txt`

**File Info:**
- **Size**: 8.66 KB
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `benchmark/benchmark_results.txt`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-17 18:59:35 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 12:59:17 (Asia/Damascus / GMT+03:00)
- **MD5**: `cb0bf80ab38def74c5ec67c0ade801b7`
- **SHA256**: `616eb92eb4acb7439be35847b80fbf23f4a30fe94d2629c28353e102885631d4`
- **Encoding**: ASCII

**File code content:**

```text
Load Test Results
=================

Project: E-commerce API
Test plan: 100 concurrent users


// here is the Load Balancer with  Round-Robin 
----------------------------------------------------------------------------
Users: 100
Spawn rate: 10
Run time: 5m
pipenv : [2026-05-18 11:11:25,450] omar/INFO/locust.main: Starting Locust 2.44.0

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /api/stores/                                                                     792     0(0.00%) |   6163      60   57794   5100 |    2.65        0.00
GET      /api/stores/7/products/                                                         1603     0(0.00%) |   6426      57   56557   5300 |    5.36        0.00
POST     /api/users/login/                                                                100     0(0.00%) |  44643    8928   57795  44000 |    0.33        0.00
POST     /api/users/register/                                                             382     0(0.00%) |  13309    1371   59089   7500 |    1.28        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                      2877     0(0.00%) |   8596      57   59089   5500 |    9.62        0.00

Response time percentiles (approximated)
Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
GET      /api/stores/                                                                         5100   6400   7700   8600  11000  17000  26000  36000  58000  58000  58000    792
GET      /api/stores/7/products/                                                              5300   6800   7900   8700  12000  18000  29000  37000  56000  57000  57000   1603
POST     /api/users/login/                                                                   45000  52000  53000  54000  57000  58000  58000  58000  58000  58000  58000    100
POST     /api/users/register/                                                                 7600  10000  16000  18000  40000  48000  55000  57000  59000  59000  59000    382
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated                                                                           5500   7400   8800   9600  18000  39000  50000  55000  58000  59000  59000   2877


---------------------------------------------------------------------------------------------------------------
// here without the Load Balancer
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /api/stores/                                                                    1518 1067(70.29%) |    916       7    4858    750 |    5.08        3.57
GET      /api/stores/7/products/                                                         3076 2154(70.03%) |    892       7    5916    730 |   10.29        7.21
POST     /api/users/login/                                                                100   67(67.00%) |  23641    2522   62594  17000 |    0.33        0.22
POST     /api/users/register/                                                             599  418(69.78%) |  23711    3115  104477  14000 |    2.00        1.40
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                      5293 3706(70.02%) |   3911       7  104477    890 |   17.71       12.40

Response time percentiles (approximated)
Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
GET      /api/stores/                                                                          750   1100   1400   1500   2000   2500   3000   3400   4300   4900   4900   1518
GET      /api/stores/7/products/                                                               730   1100   1300   1400   1900   2400   3000   3500   4600   5900   5900   3076
POST     /api/users/login/                                                                   18000  28000  38000  47000  56000  60000  61000  63000  63000  63000  63000    100
POST     /api/users/register/                                                                14000  17000  26000  45000  56000  64000  92000  97000 104000 104000 104000    599
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated                                                                            890   1300   1700   2100  11000  17000  52000  59000  97000 104000 104000   5293


-------------------------------------------------------------------
//here used Least connection
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |
req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|-------
-|-----------
GET      /api/stores/                                                                    1109     0(0.00%) |   4800     718   39777   4000 |
3.70        0.00
GET      /api/stores/7/products/                                                         2236     0(0.00%) |   4840     579   39702   3900 |
7.47        0.00
POST     /api/users/login/                                                                100     0(0.00%) |  33610    7524   41385  36000 |
0.33        0.00
POST     /api/users/register/                                                             461     0(0.00%) |   9097    1205   40691   5900 |
1.54        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|-------
-|-----------
         Aggregated                                                                      3906     0(0.00%) |   6067     579   41385   4200 |
13.04        0.00
Response time percentiles (approximated)
Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%
99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------
|------|------|------|------
GET      /api/stores/                                                                         4000   4900   5800   6400   8100   8800  13000
25000  38000  40000  40000   1109
GET      /api/stores/7/products/                                                              3900   4900   5500   6200   8000   9100  20000
30000  39000  40000  40000   2236
POST     /api/users/login/                                                                   36000  38000  39000  40000  40000  41000  41000
41000  41000  41000  41000    100
POST     /api/users/register/                                                                 5900   7500   8600   9900  24000  31000  37000
39000  41000  41000  41000    461
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------
|------|------|------|------
         Aggregated                                                                           4200   5200   6300   7200   8800  22000  36000
38000  41000  41000  41000   3906
```

---

### <a id="📄-benchmark-locustfile-simple-py"></a>📄 `benchmark/locustfile_simple.py`

**File Info:**
- **Size**: 2.9 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `benchmark/locustfile_simple.py`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-18 07:32:15 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 07:32:59 (Asia/Damascus / GMT+03:00)
- **MD5**: `c01e7acfb2d5d69277a2c0da113ebb75`
- **SHA256**: `71023942ee95daa6b9d15cd2cf28665c20c7f3c1b9c2b9857d3f2dd572975dc4`
- **Encoding**: ASCII

**File code content:**

```python
import json
import os
import uuid
from pathlib import Path

from locust import HttpUser, task, between


BASE_DIR = Path(__file__).resolve().parent.parent
CONTEXT_FILE = Path(os.getenv('BENCHMARK_CONTEXT_FILE', BASE_DIR / 'benchmark_context.json'))


def load_context():
    if CONTEXT_FILE.exists():
        try:
            return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
        except Exception:
            return {}
    return {}


class SimpleUser(HttpUser):
    """State-free user that registers a unique account on start, logs in,
    then performs only GETs (and occasional lightweight register POSTs)
    so requests are deterministic and should succeed.
    """

    wait_time = between(1, 2)
    ctx = load_context()

    def on_start(self):
        # perform a lightweight register + login sequence per simulated user
        self.username = f"load_{uuid.uuid4().hex[:8]}"
        self.password = "LoadTest123!"
        # register
        try:
            r = self.client.post('/api/users/register/', json={
                'username': self.username,
                'email': f'{self.username}@example.com',
                'password': self.password,
                'role': 'CUSTOMER',
            })
        except Exception:
            r = None
        # login if possible
        try:
            login = self.client.post('/api/users/login/', json={'username': self.username, 'password': self.password})
            if login and login.status_code == 200:
                token = login.json().get('access')
                if token:
                    self.auth_headers = {'Authorization': f'Bearer {token}'}
                else:
                    self.auth_headers = {}
            else:
                self.auth_headers = {}
        except Exception:
            self.auth_headers = {}

        self.store_id = self.ctx.get('store_id')
        self.product_id = self.ctx.get('product_id')

    @task(3)
    def list_stores(self):
        r = self.client.get('/api/stores/', headers=getattr(self, 'auth_headers', {}))
        if r.status_code >= 500:
            r.raise_for_status()

    @task(6)
    def list_products(self):
        store_id = self.store_id or 1
        r = self.client.get(f'/api/stores/{store_id}/products/', headers=getattr(self, 'auth_headers', {}))
        if r.status_code >= 500:
            r.raise_for_status()

    @task(1)
    def lightweight_register(self):
        # occasional POST that creates a unique, harmless user (no DB conflicts)
        uname = f"load_{uuid.uuid4().hex[:10]}"
        r = self.client.post('/api/users/register/', json={
            'username': uname,
            'email': f'{uname}@example.com',
            'password': 'LoadTest123!',
            'role': 'CUSTOMER',
        })
        # only escalate on server error
        if r.status_code >= 500:
            r.raise_for_status()

```

---

### <a id="📄-benchmark-locustfile-py"></a>📄 `benchmark/locustfile.py`

**File Info:**
- **Size**: 2.75 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `benchmark/locustfile.py`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-17 18:59:35 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 06:54:16 (Asia/Damascus / GMT+03:00)
- **MD5**: `934300ff75fb1963688fbe4b31c9ec73`
- **SHA256**: `128a92f52bce9d3c53859417234e2900e70ee3d8016ad4c2e41bd7fe2dc014a7`
- **Encoding**: ASCII

**File code content:**

```python
import json
import os
import random
from pathlib import Path
from uuid import uuid4

from locust import HttpUser, task, between


BASE_DIR = Path(__file__).resolve().parent.parent
CONTEXT_FILE = Path(os.getenv('BENCHMARK_CONTEXT_FILE', BASE_DIR / 'benchmark_context.json'))


def load_context():
    if CONTEXT_FILE.exists():
        return json.loads(CONTEXT_FILE.read_text(encoding='utf-8'))
    return {
        'store_id': int(os.getenv('BENCHMARK_STORE_ID', '1')),
        'product_id': int(os.getenv('BENCHMARK_PRODUCT_ID', '1')),
        'quantity': int(os.getenv('BENCHMARK_QUANTITY', '1')),
    }


class EcommerceUser(HttpUser):
    wait_time = between(1, 3)
    bench_context = load_context()

    def on_start(self):
        self.username = f'benchmark_{uuid4().hex[:10]}'
        self.password = 'Benchmark123!'
        self.access_token = None
        self.completed = False
        self._register_and_login()

    def _auth_headers(self):
        return {'Authorization': f'Bearer {self.access_token}'} if self.access_token else {}

    def _register_and_login(self):
        register_payload = {
            'username': self.username,
            'email': f'{self.username}@example.com',
            'password': self.password,
            'role': 'CUSTOMER',
        }
        register_response = self.client.post('/api/users/register/', json=register_payload)
        register_response.raise_for_status()

        login_response = self.client.post('/api/users/login/', json={
            'username': self.username,
            'password': self.password,
        })
        login_response.raise_for_status()
        self.access_token = login_response.json()['access']

    @task
    def purchase_flow(self):
        if self.completed:
            return

        headers = self._auth_headers()
        store_id = self.bench_context['store_id']
        product_id = self.bench_context['product_id']
        quantity = self.bench_context['quantity']

        products_response = self.client.get(f'/api/stores/{store_id}/products/', headers=headers)
        products_response.raise_for_status()

        cart_response = self.client.post(
            '/api/cart/items/',
            headers=headers,
            json={'product': product_id, 'quantity': quantity},
        )
        cart_response.raise_for_status()

        order_response = self.client.post('/api/orders/', headers=headers, json={})
        order_response.raise_for_status()
        order_id = order_response.json()['id']

        payment_response = self.client.post(
            f'/api/orders/{order_id}/payment/',
            headers=headers,
            json={},
        )
        payment_response.raise_for_status()

        self.completed = True
```

---

### <a id="📄-benchmark-probe-backends-py"></a>📄 `benchmark/probe_backends.py`

**File Info:**
- **Size**: 2.31 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `benchmark/probe_backends.py`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-17 19:13:19 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 09:25:17 (Asia/Damascus / GMT+03:00)
- **MD5**: `df9a6b0b356e7d034b8a01c65f31726d`
- **SHA256**: `47ce41f76ba763d97b145819f7035151669de81e1bdd3f6385d585f271441a1f`
- **Encoding**: ASCII

**File code content:**

```python
import argparse
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen


LOGIN_PATH = '/api/users/login/'


def login_and_get_token(base_url, username, password):
    payload = json.dumps({
        'username': username,
        'password': password,
    }).encode('utf-8')
    request = Request(
        f'{base_url}{LOGIN_PATH}',
        data=payload,
        method='POST',
        headers={'Content-Type': 'application/json'},
    )
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
    return data.get('access')


def fetch_backend_header(base_url, path, token=None):
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = Request(f'{base_url}{path}', method='GET', headers=headers)
    try:
        with urlopen(request, timeout=10) as response:
            backend_id = response.headers.get('X-Backend-Server', 'missing')
            return response.status, backend_id
    except HTTPError as error:
        backend_id = error.headers.get('X-Backend-Server', 'missing') if error.headers else 'missing'
        return error.code, backend_id


def main():
    parser = argparse.ArgumentParser(description='Probe load balancer backends via X-Backend-Server header')
    parser.add_argument('--host', default='http://localhost:8080', help='Base URL of the load balancer')
    parser.add_argument('--path', default='/api/stores/', help='API path to request')
    parser.add_argument('--count', '-n', type=int, default=10, help='Number of requests to make')
    parser.add_argument('--no-auth', action='store_true', help='Do not authenticate before requests')
    parser.add_argument('--username', default='benchmark_owner')
    parser.add_argument('--password', default='Benchmark123!')
    args = parser.parse_args()

    token = None
    if not args.no_auth:
        try:
            token = login_and_get_token(args.host, args.username, args.password)
        except Exception as e:
            print('Login failed:', e)
            return

    for index in range(args.count):
        status_code, backend_id = fetch_backend_header(args.host, args.path, token)
        print(f'{index + 1}: {status_code} {backend_id}')


if __name__ == '__main__':
    main()
```

---

### <a id="📄-benchmark-probe-concurrent-py"></a>📄 `benchmark/probe_concurrent.py`

**File Info:**
- **Size**: 3.5 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `benchmark/probe_concurrent.py`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-18 09:28:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 09:45:35 (Asia/Damascus / GMT+03:00)
- **MD5**: `590ff929b34fe866e4983b8d65ac100e`
- **SHA256**: `86840206821213c11f1f6c6af1680b0abb5be1b090158a7e938f016ca2d63557`
- **Encoding**: ASCII

**File code content:**

```python
import argparse
import asyncio
import json
import sys

try:
    import aiohttp
except Exception:
    print('aiohttp is required: pip install aiohttp')
    sys.exit(1)

LOGIN_PATH = '/api/users/login/'


async def get_token(session, base, username, password):
    url = f"{base}{LOGIN_PATH}"
    async with session.post(url, json={'username': username, 'password': password}) as r:
        r.raise_for_status()
        data = await r.json()
        return data.get('access')


async def fetch(session, url, headers):
    import time
    start = time.time()
    try:
        async with session.get(url, headers=headers) as r:
            elapsed = time.time() - start
            h = r.headers.get('X-Backend-Server', 'missing')
            return {'backend': h, 'status': r.status, 'elapsed': elapsed, 'error': None}
    except Exception as e:
        return {'backend': 'missing', 'status': None, 'elapsed': None, 'error': str(e)}


async def run_probe(args):
    base = args.host.rstrip('/')
    path = args.path
    url = f"{base}{path}"
    headers = {}
    connector = aiohttp.TCPConnector(limit=args.connector_limit) if args.connector_limit is not None else None
    timeout = aiohttp.ClientTimeout(total=args.timeout) if args.timeout is not None else None
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        if not args.no_auth:
            token = await get_token(session, base, args.username, args.password)
            headers['Authorization'] = f'Bearer {token}'

        sem = asyncio.Semaphore(args.concurrency)

        async def sem_fetch(i):
            async with sem:
                return await fetch(session, url, headers)

        tasks = [asyncio.create_task(sem_fetch(i)) for i in range(args.count)]
        results = await asyncio.gather(*tasks)

    counts = {}
    errors = []
    latencies = []
    for r in results:
        backend = r.get('backend', 'missing') if isinstance(r, dict) else 'missing'
        counts[backend] = counts.get(backend, 0) + 1
        if isinstance(r, dict):
            if r.get('error'):
                errors.append(r)
            if r.get('elapsed'):
                latencies.append(r['elapsed'])

    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f'{k}: {v}')

    if errors:
        print('\nSample errors (up to 5):')
        for e in errors[:5]:
            print(f"error={e['error']} status={e.get('status')} backend={e.get('backend')}")

    if latencies:
        import statistics
        print(f"\nRequests: {len(latencies)}, avg latency: {statistics.mean(latencies):.3f}s, p95: {statistics.quantiles(latencies, n=100)[94]:.3f}s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='http://localhost:8080')
    parser.add_argument('--path', default='/api/stores/')
    parser.add_argument('--count', type=int, default=200)
    parser.add_argument('--concurrency', type=int, default=50)
    parser.add_argument('--timeout', type=float, default=10.0, help='per-request total timeout in seconds')
    parser.add_argument('--connector-limit', type=int, default=None, help='aiohttp TCPConnector limit (None = default)')
    parser.add_argument('--no-auth', action='store_true')
    parser.add_argument('--username', default='benchmark_owner')
    parser.add_argument('--password', default='Benchmark123!')
    args = parser.parse_args()
    asyncio.run(run_probe(args))


if __name__ == '__main__':
    main()

```

---

### <a id="📄-benchmark-probe-long-requests-py"></a>📄 `benchmark/probe_long_requests.py`

**File Info:**
- **Size**: 4.78 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `benchmark/probe_long_requests.py`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-18 10:21:41 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 12:30:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `755fca884e4e76a723ee7a821d8be84c`
- **SHA256**: `1b400888cfc857e63dd743441ca748d305800ce1ab74d723f19419599e7fe79a`
- **Encoding**: ASCII

**File code content:**

```python
import argparse
import asyncio
import sys
import json

try:
    import aiohttp
except Exception:
    print('aiohttp is required: pip install aiohttp')
    sys.exit(1)

LOGIN_PATH = '/api/users/login/'


async def get_token(session, base, username, password):
    url = f"{base}{LOGIN_PATH}"
    async with session.post(url, json={'username': username, 'password': password}) as r:
        r.raise_for_status()
        data = await r.json()
        return data.get('access')


async def fetch(session, url, headers, method='GET', body=None):
    import time
    start = time.time()
    try:
        if method.upper() == 'GET':
            async with session.get(url, headers=headers) as r:
                elapsed = time.time() - start
                h = r.headers.get('X-Backend-Server', 'missing')
                return {'backend': h, 'status': r.status, 'elapsed': elapsed, 'error': None}
        else:
            async with session.post(url, headers=headers, json=body) as r:
                elapsed = time.time() - start
                h = r.headers.get('X-Backend-Server', 'missing')
                return {'backend': h, 'status': r.status, 'elapsed': elapsed, 'error': None}
    except Exception as e:
        return {'backend': 'missing', 'status': None, 'elapsed': None, 'error': str(e)}


async def run_probe(args):
    base = args.host.rstrip('/')
    path = args.path
    url = f"{base}{path}"
    headers = {}
    connector = aiohttp.TCPConnector(limit=args.connector_limit) if args.connector_limit is not None else None
    timeout = aiohttp.ClientTimeout(total=args.timeout) if args.timeout is not None else None
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        if not args.no_auth:
            token = await get_token(session, base, args.username, args.password)
            headers['Authorization'] = f'Bearer {token}'

        # warmup
        if args.warmup and args.warmup > 0:
            for _ in range(args.warmup):
                await fetch(session, url, headers, method=args.method, body=args.body)

        sem = asyncio.Semaphore(args.concurrency)

        async def sem_fetch(i):
            async with sem:
                result = await fetch(session, url, headers, method=args.method, body=args.body)
                result['index'] = i
                return result

        tasks = []
        for i in range(args.count):
            tasks.append(asyncio.create_task(sem_fetch(i)))
            if args.stagger > 0:
                await asyncio.sleep(args.stagger)

        results = await asyncio.gather(*tasks)

    counts = {}
    errors = []
    latencies = []
    ordered = sorted(results, key=lambda item: item.get('index', 0))
    for r in results:
        backend = r.get('backend', 'missing') if isinstance(r, dict) else 'missing'
        counts[backend] = counts.get(backend, 0) + 1
        if isinstance(r, dict):
            if r.get('error'):
                errors.append(r)
            if r.get('elapsed'):
                latencies.append(r['elapsed'])

    for r in ordered:
        print(f"Request {r.get('index', '?') + 1}: {r.get('backend', 'missing')}")

    print('\n--- Counts ---')
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f'{k}: {v}')

    if errors:
        print('\nSample errors (up to 5):')
        for e in errors[:5]:
            print(f"error={e['error']} status={e.get('status')} backend={e.get('backend')}")

    if latencies:
        import statistics
        p95 = statistics.quantiles(latencies, n=100)[94] if len(latencies) >= 100 else max(latencies)
        print(f"\nRequests: {len(latencies)}, avg latency: {statistics.mean(latencies):.3f}s, p95: {p95:.3f}s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='http://localhost:8080')
    parser.add_argument('--path', default='/api/stores/')
    parser.add_argument('--count', type=int, default=500)
    parser.add_argument('--concurrency', type=int, default=400)
    parser.add_argument('--timeout', type=float, default=30.0)
    parser.add_argument('--connector-limit', type=int, default=0)
    parser.add_argument('--no-auth', action='store_true')
    parser.add_argument('--username', default='benchmark_owner')
    parser.add_argument('--password', default='Benchmark123!')
    parser.add_argument('--method', default='GET')
    parser.add_argument('--body', type=json.loads, default=None)
    parser.add_argument('--warmup', type=int, default=5, help='number of warmup requests (sequential)')
    parser.add_argument('--stagger', type=float, default=0.0, help='delay between starting tasks (seconds)')
    args = parser.parse_args()
    asyncio.run(run_probe(args))


if __name__ == '__main__':
    main()

```

---

### <a id="📄-benchmark-probe-sequence-py"></a>📄 `benchmark/probe_sequence.py`

**File Info:**
- **Size**: 1.54 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `benchmark/probe_sequence.py`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-18 10:38:33 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 10:38:34 (Asia/Damascus / GMT+03:00)
- **MD5**: `2eda8e6c5ed7e82cec55544a6ccba87e`
- **SHA256**: `3b3127a47b82168ee0abddadb8b13890a7cb9822e18b0059a26777884335b0f0`
- **Encoding**: ASCII

**File code content:**

```python
import argparse
import requests
import sys
import time

def run_sequence_probe(args):
    """Makes sequential requests and prints the backend server for each."""
    backend_hits = []
    print(f"--- Probing {args.host} {args.count} times sequentially ({args.delay:.2f}s delay between requests) ---\n")

    for i in range(args.count):
        try:
            r = requests.get(args.host, timeout=10)
            r.raise_for_status()
            backend_id = r.headers.get('X-Backend-Server', 'missing')
            backend_hits.append(backend_id)
            print(f"Request {i+1}: {backend_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request {i+1}: FAILED ({e})")
            backend_hits.append("FAILED")
        
        if args.delay > 0:
            time.sleep(args.delay)

    print("\n--- Sequence Summary ---")
    print(", ".join(backend_hits))
    print("\n--- Counts ---")
    counts = {}
    for hit in backend_hits:
        counts[hit] = counts.get(hit, 0) + 1
    for k, v in sorted(counts.items()):
        print(f"{k}: {v}")


def main():
    parser = argparse.ArgumentParser(description="Probe backends sequentially to observe LB patterns.")
    parser.add_argument('--host', default='http://localhost:8080/api/stores/')
    parser.add_argument('--count', type=int, default=10)
    parser.add_argument('--delay', type=float, default=0, help="Delay in seconds between requests.")
    args = parser.parse_args()
    run_sequence_probe(args)


if __name__ == '__main__':
    main()

```

---

### <a id="📄-benchmark-run-benchmark-with-metrics-ps1"></a>📄 `benchmark/run_benchmark_with_metrics.ps1`

**File Info:**
- **Size**: 3.24 KB
- **Extension**: `.ps1`
- **Language**: `powershell`
- **Location**: `benchmark/run_benchmark_with_metrics.ps1`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-18 08:29:36 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 08:31:54 (Asia/Damascus / GMT+03:00)
- **MD5**: `ffe74e7728cef07cba625ce1711c7d27`
- **SHA256**: `01a746e496b4a63d10ece58b1c22c61127f22f4f2ff76a9b759514b60ecf7bb2`
- **Encoding**: ASCII

**File code content:**

```powershell
param(
    [Parameter(Mandatory = $true)]
    [string]$HostUrl,

    [Parameter(Mandatory = $true)]
    [string]$Label,

    [string]$LocustFile = 'locustfile_simple.py',
    [int]$Users = 100,
    [int]$SpawnRate = 10,
    [string]$RunTime = '5m',
    [string]$ResultsFile = 'benchmark_results.txt',
    [string]$MetricsFile = 'resource_usage.csv',
    [string]$ComposeFile,
    [string[]]$Services = @('db', 'web1', 'web2', 'web3', 'nginx'),
    [string[]]$ProcessNames = @('python', 'pythonw')
)

$resultsPath = Join-Path $PSScriptRoot $ResultsFile
$metricsPath = Join-Path $PSScriptRoot $MetricsFile
$locustPath = Join-Path $PSScriptRoot $LocustFile

$header = @"

$Label
$('-' * $Label.Length)
Date: $(Get-Date -Format o)
Host: $HostUrl
Users: $Users
Spawn rate: $SpawnRate
Run time: $RunTime
"@

Add-Content -Path $resultsPath -Value $header

if (Test-Path $metricsPath) {
    Add-Content -Path $metricsPath -Value "`n$Label`n$(('-' * $Label.Length))`nTimestamp,Container,CPU,Memory"
}
else {
    Add-Content -Path $metricsPath -Value "Label,Timestamp,Container,CPU,Memory"
}

$containerIds = @()
if ($ComposeFile) {
    foreach ($service in $Services) {
        $containerId = & docker compose -f $ComposeFile ps -q $service 2>$null
        if ($containerId) {
            $containerIds += $containerId.Trim()
        }
    }
}

$metricsJob = $null
if ($containerIds.Count -gt 0) {
    $metricsJob = Start-Job -ArgumentList @($containerIds, $metricsPath, $Label) -ScriptBlock {
        param($ids, $path, $scenarioLabel)
        while ($true) {
            $timestamp = Get-Date -Format o
            foreach ($id in $ids) {
                $line = & docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemUsage}}" $id 2>$null
                if ($line) {
                    Add-Content -Path $path -Value "$scenarioLabel,$timestamp,$line"
                }
            }
            Start-Sleep -Seconds 1
        }
    }
}
else {
    $metricsJob = Start-Job -ArgumentList @($ProcessNames, $metricsPath, $Label) -ScriptBlock {
        param($names, $path, $scenarioLabel)
        while ($true) {
            $timestamp = Get-Date -Format o
            foreach ($name in $names) {
                $processes = Get-Process -Name $name -ErrorAction SilentlyContinue
                foreach ($process in $processes) {
                    $cpu = if ($null -ne $process.CPU) { [math]::Round($process.CPU, 2) } else { 0 }
                    $memoryMb = [math]::Round($process.WorkingSet64 / 1MB, 2)
                    Add-Content -Path $path -Value "$scenarioLabel,$timestamp,$($process.ProcessName),$cpu,$memoryMb"
                }
            }
            Start-Sleep -Seconds 1
        }
    }
}

try {
    $locustOutput = & pipenv run locust -f $locustPath `
        --headless `
        --host $HostUrl `
        --users $Users `
        --spawn-rate $SpawnRate `
        --run-time $RunTime `
        --only-summary 2>&1 | Out-String -Width 5000

    Add-Content -Path $resultsPath -Value $locustOutput
}
finally {
    if ($metricsJob) {
        Stop-Job $metricsJob -ErrorAction SilentlyContinue | Out-Null
        Remove-Job $metricsJob -Force -ErrorAction SilentlyContinue | Out-Null
    }
}

```

---

### <a id="📄-benchmark-run-benchmark-ps1"></a>📄 `benchmark/run_benchmark.ps1`

**File Info:**
- **Size**: 823 B
- **Extension**: `.ps1`
- **Language**: `powershell`
- **Location**: `benchmark/run_benchmark.ps1`
- **Relative Path**: `benchmark`
- **Created**: 2026-05-17 19:00:10 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 08:09:42 (Asia/Damascus / GMT+03:00)
- **MD5**: `9ed489025684b0f10b2269b1416ba4ac`
- **SHA256**: `e1477be62238a4852b50ce19e4f02bb2f23c26ffea429bc6b2564ba34aec3f18`
- **Encoding**: ASCII

**File code content:**

```powershell
param(
    [Parameter(Mandatory = $true)]
    [string]$HostUrl,

    [Parameter(Mandatory = $true)]
    [string]$Label,

    [int]$Users = 100,
    [int]$SpawnRate = 10,
    [string]$RunTime = '5m',
    [string]$ResultsFile = 'benchmark_results.txt'
)

$resultsPath = Join-Path $PSScriptRoot $ResultsFile
$header = @"

$Label
$('-' * $Label.Length)
Date: $(Get-Date -Format o)
Host: $HostUrl
Users: $Users
Spawn rate: $SpawnRate
Run time: $RunTime
"@

Add-Content -Path $resultsPath -Value $header

$locustOutput = & locust -f (Join-Path $PSScriptRoot 'locustfile.py') `
    --headless `
    --host $HostUrl `
    --users $Users `
    --spawn-rate $SpawnRate `
    --run-time $RunTime `
    --only-summary 2>&1 | Out-String -Width 5000

Add-Content -Path $resultsPath -Value $locustOutput
```

---

### <a id="📄-cart-migrations-init-py"></a>📄 `cart/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/migrations/__init__.py`
- **Relative Path**: `cart/migrations`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-cart-migrations-0001-initial-py"></a>📄 `cart/migrations/0001_initial.py`

**File Info:**
- **Size**: 871 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/migrations/0001_initial.py`
- **Relative Path**: `cart/migrations`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `2dea5754f939de6e20bd8cc2ef15085c`
- **SHA256**: `9a75231bbe546dfd78f7677370e747eec6b77b2df9eaaa061f6bba7eb27dacb1`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```

---

### <a id="📄-cart-init-py"></a>📄 `cart/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/__init__.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-cart-admin-py"></a>📄 `cart/admin.py`

**File Info:**
- **Size**: 93 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/admin.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `0d7915af7415faf4dba56c5d0c9bf80a`
- **SHA256**: `2e49652ba0ad4ca787638bfd6aadf3821f59d6f11f747afc25b0899d5d47586a`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

from .models import Cart


admin.site.register(Cart)

```

---

### <a id="📄-cart-apps-py"></a>📄 `cart/apps.py`

**File Info:**
- **Size**: 88 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/apps.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `76f3d6ed9985cb3d0543f563c047e798`
- **SHA256**: `15210df6d60787f870bc6b531cbfef42314be1cc007c0792207481d0a2144003`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class CartConfig(AppConfig):
    name = 'cart'

```

---

### <a id="📄-cart-models-py"></a>📄 `cart/models.py`

**File Info:**
- **Size**: 419 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/models.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `361723d3be161bfcbf6f99619cea7d89`
- **SHA256**: `dc550a47b09749fb7e21a905c5d92807c29f503544f958b40eb0b523849f32a5`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models
from django.conf import settings


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart({self.user.username})'

```

---

### <a id="📄-cart-permissions-py"></a>📄 `cart/permissions.py`

**File Info:**
- **Size**: 361 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/permissions.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `9901916cc5fd8ab721229467ada89865`
- **SHA256**: `3e0d67c831eafc988059fb408dc9bc91ea186658e64bfd3d662bbd567fc7212f`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'CUSTOMER'


class IsCartOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

```

---

### <a id="📄-cart-serializers-py"></a>📄 `cart/serializers.py`

**File Info:**
- **Size**: 256 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/serializers.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `d231a45cd26a3218e6b47b13321d867e`
- **SHA256**: `39eb0e49936f439b63f545d92d7e616a934292963ca975bac75f8d2445b5c9e4`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

```

---

### <a id="📄-cart-tests-py"></a>📄 `cart/tests.py`

**File Info:**
- **Size**: 1.02 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/tests.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `8d61bb9dcd6dd146c36362b1159e61d7`
- **SHA256**: `70bc089fe0fefd6e75408ed6447843ff44daf65a6371cf5d07bc3d21eab892e8`
- **Encoding**: ASCII

**File code content:**

```python
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from .models import Cart


class CartModelTest(TestCase):
    def test_create_cart(self):
        user = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        cart = Cart.objects.get(user=user)
        self.assertEqual(cart.user, user)


class CartViewSetTest(TestCase):
    def test_prevent_duplicate_cart(self):
        user = get_user_model().objects.create_user(
            username='duplicate',
            password='password',
            role='CUSTOMER'
        )
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/api/carts/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Cart.objects.filter(user=user).count(), 1)

```

---

### <a id="📄-cart-urls-py"></a>📄 `cart/urls.py`

**File Info:**
- **Size**: 303 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/urls.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `1e8fc6eab71d85a07fd40d4235107c8a`
- **SHA256**: `45ceb6ed9efeb89ad0f326e20750bec020b6e8cb6140709cfbe091f5f714591e`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.routers import DefaultRouter
from .views import CartViewSet
from cart_items.views import CartItemViewSet

router = DefaultRouter()
router.register(r'items', CartItemViewSet, basename='cart-items') 
router.register(r'', CartViewSet, basename='cart')

urlpatterns = router.urls
```

---

### <a id="📄-cart-views-py"></a>📄 `cart/views.py`

**File Info:**
- **Size**: 646 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart/views.py`
- **Relative Path**: `cart`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `3d109cb0dabe51f98dc3e836f4242c70`
- **SHA256**: `3282b106561fad4eda3bb89f4098b0e07e60da06adf6a6d0b6be5f2a1b590b9d`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import Cart
from .permissions import IsCustomer, IsCartOwner
from .serializers import CartSerializer


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsCustomer, IsCartOwner]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        raise ValidationError('Cart is created automatically for customers')

```

---

### <a id="📄-cart-items-migrations-init-py"></a>📄 `cart_items/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/migrations/__init__.py`
- **Relative Path**: `cart_items/migrations`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-cart-items-migrations-0001-initial-py"></a>📄 `cart_items/migrations/0001_initial.py`

**File Info:**
- **Size**: 1.05 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/migrations/0001_initial.py`
- **Relative Path**: `cart_items/migrations`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `541b0e64edec43d2942b2f303439d3d8`
- **SHA256**: `fd52c36daced57bd759e8a9b1e50db7d7f3256e9314322148b6c0b60b08035f0`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='products.product')),
            ],
            options={
                'unique_together': {('cart', 'product')},
            },
        ),
    ]

```

---

### <a id="📄-cart-items-migrations-0002-cartitem-total-price-py"></a>📄 `cart_items/migrations/0002_cartitem_total_price.py`

**File Info:**
- **Size**: 433 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/migrations/0002_cartitem_total_price.py`
- **Relative Path**: `cart_items/migrations`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `69a0d4ec73dd9e12101fcbe619ac4a25`
- **SHA256**: `71434a784aacf81d2bbb4208c1591595152e5b7b3a7789a4cb3be2d9f0957fec`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

```

---

### <a id="📄-cart-items-init-py"></a>📄 `cart_items/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/__init__.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-cart-items-admin-py"></a>📄 `cart_items/admin.py`

**File Info:**
- **Size**: 101 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/admin.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `c537967d1698f2eb5ee39556965c5f79`
- **SHA256**: `955d27bacec9db18e410cde1bb7ee6e7b44693b4e7850f68d067b0048be10eb6`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

from .models import CartItem


admin.site.register(CartItem)

```

---

### <a id="📄-cart-items-apps-py"></a>📄 `cart_items/apps.py`

**File Info:**
- **Size**: 99 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/apps.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `cb0025831630e0d0f1dc3b6bc16c936b`
- **SHA256**: `6a3b4a88daf83731863d751f8bce0724839d88a671f1e0e68bc3130107b82c1e`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class CartItemsConfig(AppConfig):
    name = 'cart_items'

```

---

### <a id="📄-cart-items-models-py"></a>📄 `cart_items/models.py`

**File Info:**
- **Size**: 919 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/models.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `27bea75a63949660344390617ddab3d9`
- **SHA256**: `c2ba1eec57f7089edc263e0c344fcbd9f5a766d09af03977dc77225333780c80`
- **Encoding**: ASCII

**File code content:**

```python
from decimal import Decimal

from django.db import models

from cart.models import Cart
from products.models import Product


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
        return f'{self.product.name} x{self.quantity}'

    def save(self, *args, **kwargs):
        self.total_price = Decimal(self.quantity) * Decimal(str(self.product.price))
        super().save(*args, **kwargs)

```

---

### <a id="📄-cart-items-permissions-py"></a>📄 `cart_items/permissions.py`

**File Info:**
- **Size**: 370 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/permissions.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `ae6bfa5f9a67aebefbf1937f979de8bf`
- **SHA256**: `76bec136d0f33dbc1e5e2c441046237e18964a5bad4c01d0781318013471048d`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'CUSTOMER'


class IsCartItemOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cart.user == request.user

```

---

### <a id="📄-cart-items-serializers-py"></a>📄 `cart_items/serializers.py`

**File Info:**
- **Size**: 267 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/serializers.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `361fd0305d3c5d2e659d19b6df6282cb`
- **SHA256**: `3fd1e41f994e1761eb8ad5142b6a55f703e67b076e014e5bd7ccb696f350c8b6`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['cart', 'added_at', 'total_price']

```

---

### <a id="📄-cart-items-tests-py"></a>📄 `cart_items/tests.py`

**File Info:**
- **Size**: 2.48 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/tests.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `02f903e217e5e6c687beddbefd9211cf`
- **SHA256**: `97469534153a21a2359b95b503de72963b12d313de4b7ccd0d619b161e890e21`
- **Encoding**: ASCII

**File code content:**

```python
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from cart.models import Cart
from .models import CartItem
from products.models import Product
from store.models import Store


class CartItemModelTest(TestCase):
    def test_create_cart_item(self):
        owner = get_user_model().objects.create_user(
            username='owner',
            password='password',
            role='STORE_OWNER'
        )
        store = Store.objects.create(
            name='My Store',
            description='Test store',
            owner=owner
        )
        product = Product.objects.create(
            store=store,
            name='Item',
            description='Test product',
            price='9.99',
            stock=10
        )
        customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        cart = Cart.objects.get(user=customer)
        item = CartItem.objects.create(cart=cart, product=product, quantity=2)
        self.assertEqual(item.cart, cart)


class CartItemViewSetTest(TestCase):
    def test_other_customer_cannot_view_cart_items(self):
        owner = get_user_model().objects.create_user(
            username='owner',
            password='password',
            role='STORE_OWNER'
        )
        store = Store.objects.create(
            name='My Store',
            description='Test store',
            owner=owner
        )
        product = Product.objects.create(
            store=store,
            name='Item',
            description='Test product',
            price='9.99',
            stock=10
        )
        customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        other_customer = get_user_model().objects.create_user(
            username='other_customer',
            password='password',
            role='CUSTOMER'
        )
        cart = Cart.objects.get(user=customer)
        CartItem.objects.create(cart=cart, product=product, quantity=1)
        client = APIClient()
        client.force_authenticate(user=other_customer)
        response = client.get(f'/api/carts/{cart.id}/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

```

---

### <a id="📄-cart-items-views-py"></a>📄 `cart_items/views.py`

**File Info:**
- **Size**: 1.69 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `cart_items/views.py`
- **Relative Path**: `cart_items`
- **Created**: 2026-05-18 07:25:43 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 07:25:43 (Asia/Damascus / GMT+03:00)
- **MD5**: `3a9aefb9e0c89a02c4c8098ee65212ea`
- **SHA256**: `316067b00055368dba48622b8dc0dc03a813e13d88e316dc5027770ff5588cfd`
- **Encoding**: ASCII

**File code content:**

```python
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart
from .models import CartItem
from .permissions import IsCustomer, IsCartItemOwner
from .serializers import CartItemSerializer


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsCustomer, IsCartItemOwner]

    def get_cart(self):
        return self.request.user.cart

    def get_queryset(self):
        cart = self.get_cart()
        return CartItem.objects.filter(cart=cart)

    def create(self, request, *args, **kwargs):
        cart = self.get_cart()
        if cart.user != request.user:
            raise PermissionDenied('This cart does not belong to you')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)
        existing_item = CartItem.objects.filter(cart=cart, product=product).first()
        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
            output = self.get_serializer(existing_item)
            return Response(output.data, status=status.HTTP_200_OK)
        serializer.save(cart=cart)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `ecommerce/__pycache__/__init__.cpython-314.pyc`
- `ecommerce/__pycache__/settings.cpython-314.pyc`
- `ecommerce/__pycache__/urls.cpython-314.pyc`

### <a id="📄-ecommerce-init-py"></a>📄 `ecommerce/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ecommerce/__init__.py`
- **Relative Path**: `ecommerce`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-ecommerce-asgi-py"></a>📄 `ecommerce/asgi.py`

**File Info:**
- **Size**: 411 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ecommerce/asgi.py`
- **Relative Path**: `ecommerce`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `15c5ca8f5269f1010cde508bd0012f92`
- **SHA256**: `e1fa5d9f533b151c5d09b772b5a0470a32ddc9636113b4d70645da3c13b163ba`
- **Encoding**: ASCII

**File code content:**

```python
"""
ASGI config for ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_asgi_application()

```

---

### <a id="📄-ecommerce-middleware-py"></a>📄 `ecommerce/middleware.py`

**File Info:**
- **Size**: 706 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ecommerce/middleware.py`
- **Relative Path**: `ecommerce`
- **Created**: 2026-05-17 19:13:19 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 10:03:29 (Asia/Damascus / GMT+03:00)
- **MD5**: `d93b94d524624324bcbee72315eb4e5e`
- **SHA256**: `5201415f5127f609461cfb66e74818627a32687a3cf25c5e6c06aecaf1803d1c`
- **Encoding**: ASCII

**File code content:**

```python
import os
import time


class BackendIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Optional demo sleep to make connection handling and least_conn effects visible.
        # Configure via the environment variable `DEMO_SLEEP_SECONDS` (float seconds).
        try:
            sleep_s = float(os.getenv('DEMO_SLEEP_SECONDS', '0'))
        except Exception:
            sleep_s = 0.0
        if sleep_s and sleep_s > 0:
            time.sleep(sleep_s)

        response['X-Backend-Server'] = os.getenv('BACKEND_ID', 'unknown')
        return response
```

---

### <a id="📄-ecommerce-settings-py"></a>📄 `ecommerce/settings.py`

**File Info:**
- **Size**: 4.24 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ecommerce/settings.py`
- **Relative Path**: `ecommerce`
- **Created**: 2026-05-16 15:05:15 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:14:34 (Asia/Damascus / GMT+03:00)
- **MD5**: `8174fa6bf5666373edb39d44e2e87a92`
- **SHA256**: `fb4aa730a2710add247e67d6b8bd6682a185770e91be8497635df89a49a32c09`
- **Encoding**: ASCII

**File code content:**

```python
"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 6.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-$f$tc9xd(%tmt#oir!v0*!&d)0tuie61*x-28+f_=#*j0btm0g')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() in {'1', 'true', 'yes', 'on'}

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,web,nginx').split(',')
    if host.strip()
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'users',
    'store',
    'products',
    'cart',
    'cart_items',
    'order',
    'order_items',
    'payments'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'ecommerce.middleware.BackendIdMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DB_ENGINE = os.getenv('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': os.getenv('DJANGO_DB_NAME', BASE_DIR / 'db.sqlite3'),
    }
}

if DB_ENGINE != 'django.db.backends.sqlite3':
    DATABASES['default'].update({
        'USER': os.getenv('DJANGO_DB_USER', 'ecommerce'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', 'ecommerce'),
        'HOST': os.getenv('DJANGO_DB_HOST', 'localhost'),
        'PORT': os.getenv('DJANGO_DB_PORT', '5432'),
    })


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
AUTH_USER_MODEL = 'users.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

```

---

### <a id="📄-ecommerce-urls-py"></a>📄 `ecommerce/urls.py`

**File Info:**
- **Size**: 324 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ecommerce/urls.py`
- **Relative Path**: `ecommerce`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `f1278dc75595b246de00748eb28104eb`
- **SHA256**: `bac047c48b8478c23b2465cc2151e5a038e8d952218653c99f20c0e9f95fbecd`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/stores/', include('store.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('order.urls'))
]

```

---

### <a id="📄-ecommerce-wsgi-py"></a>📄 `ecommerce/wsgi.py`

**File Info:**
- **Size**: 411 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ecommerce/wsgi.py`
- **Relative Path**: `ecommerce`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `ed527aa408c7437ec62c51af60a7f7ab`
- **SHA256**: `fb82f18646e8b2519d37364aa4ebcc9ce9a9d62102fc7ad3d4ebfadbf31ba7f8`
- **Encoding**: ASCII

**File code content:**

```python
"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()

```

---

### <a id="📄-nginx-least-connections-conf"></a>📄 `nginx/least-connections.conf`

**File Info:**
- **Size**: 549 B
- **Extension**: `.conf`
- **Language**: `text`
- **Location**: `nginx/least-connections.conf`
- **Relative Path**: `nginx`
- **Created**: 2026-05-17 18:58:57 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:00:32 (Asia/Damascus / GMT+03:00)
- **MD5**: `2dc4d6486f6ba39cbfc45970f4c93c88`
- **SHA256**: `23cd897b3be04290885ba35c2e8f0dff9df9e94dad8c68dfd2de6e22847f8143`
- **Encoding**: ASCII

**File code content:**

```text
events {}

http {
    upstream ecommerce_api {
        least_conn;
        server web1:8000;
        server web2:8000;
        server web3:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://ecommerce_api;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

---

### <a id="📄-nginx-round-robin-conf"></a>📄 `nginx/round-robin.conf`

**File Info:**
- **Size**: 528 B
- **Extension**: `.conf`
- **Language**: `text`
- **Location**: `nginx/round-robin.conf`
- **Relative Path**: `nginx`
- **Created**: 2026-05-17 18:58:57 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:00:32 (Asia/Damascus / GMT+03:00)
- **MD5**: `67dd64a14eb2d308a54fd9fa26f23b17`
- **SHA256**: `8c08a3bc0293e5a42dd3979c0b4dfea6b449cd4fbd0f392fa99a9859fa84cdb8`
- **Encoding**: ASCII

**File code content:**

```text
events {}

http {
    upstream ecommerce_api {
        server web1:8000;
        server web2:8000;
        server web3:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://ecommerce_api;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

---

### <a id="📄-order-migrations-init-py"></a>📄 `order/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/migrations/__init__.py`
- **Relative Path**: `order/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-order-migrations-0001-initial-py"></a>📄 `order/migrations/0001_initial.py`

**File Info:**
- **Size**: 1.17 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/migrations/0001_initial.py`
- **Relative Path**: `order/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `9da5e86fe7fd9f34175ac3d1ea0f38c3`
- **SHA256**: `e137b836f4bddfc8fa00b509c600e6fe014d2eb16a1b2a0c75afdf5cc5f820be`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```

---

### <a id="📄-order-migrations-0002-alter-order-store-py"></a>📄 `order/migrations/0002_alter_order_store.py`

**File Info:**
- **Size**: 554 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/migrations/0002_alter_order_store.py`
- **Relative Path**: `order/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `59664d3904682010d432ff8a7364a9bc`
- **SHA256**: `ff2b9d217168ae85845d5eef7131b651127f18a0dc244a5a475430199486b731`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.store'),
        ),
    ]

```

---

### <a id="📄-order-init-py"></a>📄 `order/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/__init__.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-order-admin-py"></a>📄 `order/admin.py`

**File Info:**
- **Size**: 95 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/admin.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `cad39818a3ca375f3d65e7131cf7220d`
- **SHA256**: `3034b89a358b9434a246f5aae6e0aef287de0d0ff96388584ee426bf0787e246`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

from .models import Order


admin.site.register(Order)

```

---

### <a id="📄-order-apps-py"></a>📄 `order/apps.py`

**File Info:**
- **Size**: 90 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/apps.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `4b6ca46b9c39807bec5d61b25d904dca`
- **SHA256**: `f77c4d4133d885743c039cc7bbbab40d670b9418faa04c414e09f8627f12a8d1`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'order'

```

---

### <a id="📄-order-models-py"></a>📄 `order/models.py`

**File Info:**
- **Size**: 913 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/models.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `2fd456de1c150f861f7d8cd1b199d661`
- **SHA256**: `bbabeda1b4e5bfd80cb2a8944d2fc95a441aa90f0fdda088bbb244f7eaedc290`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models
from django.conf import settings

from store.models import Store


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PAID = 'PAID', 'Paid'
        CANCELLED = 'CANCELLED', 'Cancelled'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} ({self.user.username})'

```

---

### <a id="📄-order-permissions-py"></a>📄 `order/permissions.py`

**File Info:**
- **Size**: 812 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/permissions.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `caf941a7f8bb5282d4bb62da7ecaf36a`
- **SHA256**: `75029c387fe78d4ea99cc9814d9b71c9f9f297202687abc8bb560f9550286ace`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrderAccess(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return request.user.role in ('CUSTOMER', 'STORE_OWNER')
        return request.user.role == 'CUSTOMER'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.role == 'CUSTOMER':
                return obj.user == request.user
            if request.user.role == 'STORE_OWNER':
                return obj.items.filter(
                    product__store__owner=request.user
                ).exists()
        return obj.user == request.user

```

---

### <a id="📄-order-serializers-py"></a>📄 `order/serializers.py`

**File Info:**
- **Size**: 334 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/serializers.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `636ccc90b0489139f09e1482ee918d39`
- **SHA256**: `db646aa9e336156d9ea644ecf1e3fbd4eefa8a017be857f608d269ec125d15b9`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
        extra_kwargs = {'store': {'required': False, 'allow_null': True}}

```

---

### <a id="📄-order-tests-py"></a>📄 `order/tests.py`

**File Info:**
- **Size**: 4.92 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/tests.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `02aeda51af47130426263471f284a439`
- **SHA256**: `da9e8dfeb33e58def220877b22cf80a17abfa98bae9d4df37ff0c9f40a648cb8`
- **Encoding**: ASCII

**File code content:**

```python
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from cart.models import Cart
from cart_items.models import CartItem
from order_items.models import OrderItem
from store.models import Store
from products.models import Product
from .models import Order


class OrderModelTest(TestCase):
    def test_create_order(self):
        customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        order = Order.objects.create(user=customer)
        self.assertIsNone(order.store)


class OrderViewSetTest(TestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(
            username='owner',
            password='password',
            role='STORE_OWNER'
        )
        self.other_owner = get_user_model().objects.create_user(
            username='other_owner',
            password='password',
            role='STORE_OWNER'
        )
        self.store = Store.objects.create(
            name='Store',
            description='Test store',
            owner=self.owner
        )
        self.other_store = Store.objects.create(
            name='Other Store',
            description='Other store',
            owner=self.other_owner
        )
        self.customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        self.other_customer = get_user_model().objects.create_user(
            username='other_customer',
            password='password',
            role='CUSTOMER'
        )
        self.customer_order = Order.objects.create(
            user=self.customer,
            store=self.store
        )
        self.other_order = Order.objects.create(
            user=self.other_customer,
            store=self.other_store
        )
        self.product = Product.objects.create(
            store=self.store,
            name='Item',
            description='Test product',
            price='10.00',
            stock=5
        )
        self.other_product = Product.objects.create(
            store=self.other_store,
            name='Other Item',
            description='Other product',
            price='7.50',
            stock=3
        )
        OrderItem.objects.create(
            order=self.customer_order,
            product=self.product,
            quantity=1,
            price=self.product.price
        )
        OrderItem.objects.create(
            order=self.other_order,
            product=self.other_product,
            quantity=1,
            price=self.other_product.price
        )

    def test_customer_only_sees_own_orders(self):
        client = APIClient()
        client.force_authenticate(user=self.customer)
        response = client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], self.customer_order.id)

    def test_store_owner_only_sees_store_orders(self):
        client = APIClient()
        client.force_authenticate(user=self.owner)
        response = client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], self.customer_order.id)

    def test_create_order_moves_cart_items_and_clears_cart(self):
        product = Product.objects.create(
            store=self.store,
            name='Item',
            description='Test product',
            price='10.00',
            stock=5
        )
        other_product = Product.objects.create(
            store=self.store,
            name='Another Item',
            description='Another product',
            price='7.50',
            stock=3
        )
        cart = Cart.objects.get(user=self.customer)
        CartItem.objects.create(cart=cart, product=product, quantity=2)
        CartItem.objects.create(cart=cart, product=other_product, quantity=1)
        client = APIClient()
        client.force_authenticate(user=self.customer)
        response = client.post(
            '/api/orders/',
            {'store': self.store.id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(id=response.json()['id'])
        self.assertEqual(OrderItem.objects.filter(order=order).count(), 2)
        order_item = OrderItem.objects.get(order=order, product=product)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, Decimal('10.00'))
        self.assertEqual(CartItem.objects.filter(cart=cart).count(), 0)

```

---

### <a id="📄-order-urls-py"></a>📄 `order/urls.py`

**File Info:**
- **Size**: 542 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/urls.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `80c3168b71d43ac39085e9cad03e5260`
- **SHA256**: `74516fd8a39045a4e7c14d0422a7b21b60ca6bd3401806f2a5aa0c70c019fb61`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework_nested import routers

from .views import OrderViewSet
from order_items.views import OrderItemViewSet
from payments.views import PaymentViewSet


router = routers.DefaultRouter()
router.register(r'', OrderViewSet, basename='orders')

orders_router = routers.NestedDefaultRouter(router, r'', lookup='order')
orders_router.register(r'items', OrderItemViewSet, basename='order-items')
orders_router.register(r'payment', PaymentViewSet, basename='order-payment')

urlpatterns = router.urls + orders_router.urls

```

---

### <a id="📄-order-views-py"></a>📄 `order/views.py`

**File Info:**
- **Size**: 3.15 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order/views.py`
- **Relative Path**: `order`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `372cdcf639c488d3dc3540eaf2bedd0b`
- **SHA256**: `c598bcff5c17f0780238bb2d706c6f89c333de326c2d1688803d78fe60fce205`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import transaction

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from cart.models import Cart
from cart_items.models import CartItem
from order_items.models import OrderItem
from products.models import Product

from .models import Order
from .permissions import IsOrderAccess
from .serializers import OrderSerializer
from rest_framework import status

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOrderAccess]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'CUSTOMER':
            return Order.objects.filter(user=user)
        if user.role == 'STORE_OWNER':
            return Order.objects.filter(items__product__store__owner=user).distinct()
        return Order.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.filter(user=user).first()
        if not cart:
            raise ValidationError('Cart not found')
        cart_items = list(
            CartItem.objects.select_related('product', 'product__store')
            .filter(cart=cart)
        )
        if not cart_items:
            raise ValidationError('Cart is empty')
        with transaction.atomic():
            order = serializer.save(user=user)
            order_items = []
            
            for item in cart_items:
                product = Product.objects.select_for_update().get(id=item.product_id)
                if item.quantity > product.stock:
                    raise ValidationError(f'Not enough stock for {product.name}')
                
                product.stock -= item.quantity
                product.save()

                order_items.append(OrderItem(
                    order=order,
                    product=product,
                    quantity=item.quantity,
                    price=product.price
                ))
            OrderItem.objects.bulk_create(order_items)
            CartItem.objects.filter(cart=cart).delete()

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):

        order = self.get_object()

        if order.status == 'CANCELLED':
            raise ValidationError('Order already cancelled')

        with transaction.atomic():

            order_items = (
                OrderItem.objects
                .select_related('product')
                .filter(order=order)
            )

            for item in order_items:

                product = (
                    Product.objects
                    .select_for_update()
                    .get(id=item.product.id)
                )

                product.stock += item.quantity
                product.save()

            order.status = 'CANCELLED'
            order.save()

        return Response(
            {'message': 'Order cancelled successfully'},
            status=status.HTTP_200_OK
        )
```

---

### <a id="📄-order-items-migrations-init-py"></a>📄 `order_items/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/migrations/__init__.py`
- **Relative Path**: `order_items/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-order-items-migrations-0001-initial-py"></a>📄 `order_items/migrations/0001_initial.py`

**File Info:**
- **Size**: 1.06 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/migrations/0001_initial.py`
- **Relative Path**: `order_items/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `5da3a919f1d3608ba7b8662b931f52db`
- **SHA256**: `7c6efc6999b3ee2341cd285f0407a0c2e4625448f214dd7f74c87a8efa96b418`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
    ]

```

---

### <a id="📄-order-items-init-py"></a>📄 `order_items/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/__init__.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-order-items-admin-py"></a>📄 `order_items/admin.py`

**File Info:**
- **Size**: 103 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/admin.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `9bda42fd414eda5f9b990cf553532251`
- **SHA256**: `5c2a6140be031a705d3ecc17dbef04a0cfeb432cac49ef09d0f19564f88fca31`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

from .models import OrderItem


admin.site.register(OrderItem)

```

---

### <a id="📄-order-items-apps-py"></a>📄 `order_items/apps.py`

**File Info:**
- **Size**: 101 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/apps.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `03ff0fddd9e3d9071c935dab9b5c1de4`
- **SHA256**: `3776ea978474115e0ea032a5317d9de3a95a462b9e5a6f45f79a3979e8e895f1`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class OrderItemsConfig(AppConfig):
    name = 'order_items'

```

---

### <a id="📄-order-items-models-py"></a>📄 `order_items/models.py`

**File Info:**
- **Size**: 657 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/models.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d24377b656cc390cde8e2257baf4444f`
- **SHA256**: `6000dbc01c0b360f457660ef72c850e4a4cf3d13acad2659145ff973520b2601`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models

from order.models import Order
from products.models import Product


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f'{self.product.name} x{self.quantity}'

```

---

### <a id="📄-order-items-permissions-py"></a>📄 `order_items/permissions.py`

**File Info:**
- **Size**: 766 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/permissions.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `8dc357f849c9164e0a9319aa58754af2`
- **SHA256**: `4c0418213453684baa0b2f2eee2bc71f4f0bcbf20927c68c9a76084bd01d8665`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrderItemAccess(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return request.user.role in ('CUSTOMER', 'STORE_OWNER')
        return request.user.role == 'CUSTOMER'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.role == 'CUSTOMER':
                return obj.order.user == request.user
            if request.user.role == 'STORE_OWNER':
                return obj.product.store.owner == request.user
        return obj.order.user == request.user

```

---

### <a id="📄-order-items-serializers-py"></a>📄 `order_items/serializers.py`

**File Info:**
- **Size**: 253 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/serializers.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `6d333388016264b41f352ba7777a6272`
- **SHA256**: `c3a65989e3c1ecb178991607eb406ab3c216d7417e55b03480f48c9e7010188a`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers

from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['order', 'price']

```

---

### <a id="📄-order-items-tests-py"></a>📄 `order_items/tests.py`

**File Info:**
- **Size**: 5.01 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/tests.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `2c55768f1c20e4ad8d8bf0438d535895`
- **SHA256**: `7217fd844da0668d2e197f8e55ec54d325d58268aec489207442d67d0e53f488`
- **Encoding**: ASCII

**File code content:**

```python
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from order.models import Order
from products.models import Product
from store.models import Store
from .models import OrderItem


class OrderItemModelTest(TestCase):
    def test_create_order_item(self):
        owner = get_user_model().objects.create_user(
            username='owner',
            password='password',
            role='STORE_OWNER'
        )
        store = Store.objects.create(
            name='Store',
            description='Test store',
            owner=owner
        )
        product = Product.objects.create(
            store=store,
            name='Item',
            description='Test product',
            price='12.50',
            stock=5
        )
        customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        order = Order.objects.create(user=customer, store=store)
        item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            price=product.price
        )
        self.assertEqual(item.order, order)


class OrderItemViewSetTest(TestCase):
    def setUp(self):
        owner = get_user_model().objects.create_user(
            username='owner',
            password='password',
            role='STORE_OWNER'
        )
        other_owner = get_user_model().objects.create_user(
            username='other_owner',
            password='password',
            role='STORE_OWNER'
        )
        self.store = Store.objects.create(
            name='Store',
            description='Test store',
            owner=owner
        )
        self.other_store = Store.objects.create(
            name='Other Store',
            description='Other store',
            owner=other_owner
        )
        self.product = Product.objects.create(
            store=self.store,
            name='Item',
            description='Test product',
            price='12.50',
            stock=5
        )
        self.other_product = Product.objects.create(
            store=self.other_store,
            name='Other Item',
            description='Other product',
            price='7.25',
            stock=5
        )
        self.customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        self.order = Order.objects.create(user=self.customer, store=self.store)
        self.client = APIClient()
        self.client.force_authenticate(user=self.customer)

    def test_allow_product_from_other_store(self):
        response = self.client.post(
            f'/api/orders/{self.order.id}/items/',
            {'product': self.other_product.id, 'quantity': 1},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item = OrderItem.objects.get(order=self.order, product=self.other_product)
        self.assertEqual(item.price, Decimal('7.25'))

    def test_capture_product_price(self):
        response = self.client.post(
            f'/api/orders/{self.order.id}/items/',
            {'product': self.product.id, 'quantity': 2},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item = OrderItem.objects.get(order=self.order, product=self.product)
        self.assertEqual(item.price, Decimal('12.50'))

    def test_customer_cannot_view_other_order_items(self):
        other_customer = get_user_model().objects.create_user(
            username='other_customer',
            password='password',
            role='CUSTOMER'
        )
        other_order = Order.objects.create(
            user=other_customer,
            store=self.store
        )
        OrderItem.objects.create(
            order=other_order,
            product=self.product,
            quantity=1,
            price=self.product.price
        )
        response = self.client.get(f'/api/orders/{other_order.id}/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_store_owner_cannot_view_other_store_items(self):
        other_order = Order.objects.create(
            user=self.customer,
            store=self.other_store
        )
        OrderItem.objects.create(
            order=other_order,
            product=self.other_product,
            quantity=1,
            price=self.other_product.price
        )
        owner_client = APIClient()
        owner_client.force_authenticate(user=self.store.owner)
        response = owner_client.get(f'/api/orders/{other_order.id}/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

```

---

### <a id="📄-order-items-views-py"></a>📄 `order_items/views.py`

**File Info:**
- **Size**: 1.54 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `order_items/views.py`
- **Relative Path**: `order_items`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `aa17e357106023f4736a635f37998de6`
- **SHA256**: `2c99aa6821ee3d56b3f806dfda6bd74a94fdd4244d4ed08426560f4fd45e5e19`
- **Encoding**: ASCII

**File code content:**

```python
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from order.models import Order
from products.models import Product

from .models import OrderItem
from .permissions import IsOrderItemAccess
from .serializers import OrderItemSerializer


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated, IsOrderItemAccess]
    http_method_names = ['get', 'post', 'delete', 'head', 'options']

    def get_order(self):
        order_id = self.kwargs['order_pk']
        return get_object_or_404(Order, id=order_id)

    def get_queryset(self):
        order = self.get_order()
        user = self.request.user
        if user.role == 'CUSTOMER':
            if order.user != user:
                return OrderItem.objects.none()
        elif user.role == 'STORE_OWNER':
            return OrderItem.objects.filter(
                order=order,
                product__store__owner=user
            )
        else:
            return OrderItem.objects.none()
        return OrderItem.objects.filter(order=order)

    def perform_create(self, serializer):
        order = self.get_order()
        if order.user != self.request.user:
            raise ValidationError('Only the order owner can add items')
        product = serializer.validated_data['product']
        serializer.save(order=order, price=product.price)

```

---

### <a id="📄-payments-migrations-init-py"></a>📄 `payments/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/migrations/__init__.py`
- **Relative Path**: `payments/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-payments-migrations-0001-initial-py"></a>📄 `payments/migrations/0001_initial.py`

**File Info:**
- **Size**: 967 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/migrations/0001_initial.py`
- **Relative Path**: `payments/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `c1f5bd34b74b485fda8c992a6dbae2ee`
- **SHA256**: `174fb829a1d81cd82da7ca6160ee0b8b7bf18fdf847b2cb7d59e5ced60721b17`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_alter_order_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='COMPLETED', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='order.order')),
            ],
        ),
    ]

```

---

### <a id="📄-payments-init-py"></a>📄 `payments/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/__init__.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-payments-admin-py"></a>📄 `payments/admin.py`

**File Info:**
- **Size**: 66 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/admin.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `ef4c241c5311eee11a93e9366f492a72`
- **SHA256**: `a7ac68a753eeb831b6530bf71bf6917e577139f0734d17cc6a8666391564ab25`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

# Register your models here.

```

---

### <a id="📄-payments-apps-py"></a>📄 `payments/apps.py`

**File Info:**
- **Size**: 96 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/apps.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `cfff670440b70a9499ddb71cdda6233b`
- **SHA256**: `ae37ef0c8a8418f959b3e003714150c883cc3d39d0dbc30fdcecf7d722e5153d`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    name = 'payments'

```

---

### <a id="📄-payments-models-py"></a>📄 `payments/models.py`

**File Info:**
- **Size**: 691 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/models.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `7719d4599c809b84cb9c8bb44f7ac602`
- **SHA256**: `bf25725fcc79d07ec448b38cebdd872ea373d430a3633b79c8bc8d80ab072ddd`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models

from order.models import Order


class Payment(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.COMPLETED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment {self.id} for Order {self.order_id}'

```

---

### <a id="📄-payments-permissions-py"></a>📄 `payments/permissions.py`

**File Info:**
- **Size**: 832 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/permissions.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `f937bc9bbca3e51d7f5146db1e0b7d81`
- **SHA256**: `ecae016fbcccfc3ff934af8a0cf2e4860fed8bd4ba61e59f98199eea669cab8e`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPaymentAccess(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return request.user.role in ('CUSTOMER', 'STORE_OWNER')
        return request.user.role == 'CUSTOMER'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.role == 'CUSTOMER':
                return obj.order.user == request.user
            if request.user.role == 'STORE_OWNER':
                return obj.order.items.filter(
                    product__store__owner=request.user
                ).exists()
        return obj.order.user == request.user

```

---

### <a id="📄-payments-serializers-py"></a>📄 `payments/serializers.py`

**File Info:**
- **Size**: 272 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/serializers.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `f99d99282953a8791aece1110a37c26c`
- **SHA256**: `df6db44d34f744732c137051bbebf6c561317af4a1d47c53d3d07bed9195dd5c`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['order', 'amount', 'status', 'created_at']

```

---

### <a id="📄-payments-tests-py"></a>📄 `payments/tests.py`

**File Info:**
- **Size**: 1.88 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/tests.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `3fa4d4ea30cbfe76bccf7b8869fe769c`
- **SHA256**: `21b0943d3c3e5fb257f4fad143eef64671e9f91f219490141f4f5013099ec9f0`
- **Encoding**: ASCII

**File code content:**

```python
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from order.models import Order
from order_items.models import OrderItem
from products.models import Product
from store.models import Store

from .models import Payment


class PaymentViewSetTest(TestCase):
    def setUp(self):
        owner = get_user_model().objects.create_user(
            username='owner',
            password='password',
            role='STORE_OWNER'
        )
        self.store = Store.objects.create(
            name='Store',
            description='Test store',
            owner=owner
        )
        self.product = Product.objects.create(
            store=self.store,
            name='Item',
            description='Test product',
            price='12.50',
            stock=5
        )
        self.customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            role='CUSTOMER'
        )
        self.order = Order.objects.create(user=self.customer)
        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=self.product.price
        )

    def test_create_payment_marks_order_paid(self):
        client = APIClient()
        client.force_authenticate(user=self.customer)
        response = client.post(
            f'/api/orders/{self.order.id}/payment/',
            {},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, Order.Status.PAID)
        payment = Payment.objects.get(order=self.order)
        self.assertEqual(payment.amount, Decimal('25.00'))

```

---

### <a id="📄-payments-views-py"></a>📄 `payments/views.py`

**File Info:**
- **Size**: 1.99 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `payments/views.py`
- **Relative Path**: `payments`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `afb7235715eb05a9885cdaf741bd4555`
- **SHA256**: `11699018d000c6bc989adbfd5b6ad0bb16df56d13f640b7e5e05334021db2ed1`
- **Encoding**: ASCII

**File code content:**

```python
from decimal import Decimal

from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from order.models import Order

from .models import Payment
from .permissions import IsPaymentAccess
from .serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsPaymentAccess]
    http_method_names = ['get', 'post', 'head', 'options']

    def get_order(self):
        order_id = self.kwargs['order_pk']
        return get_object_or_404(Order, id=order_id)

    def get_queryset(self):
        order = self.get_order()
        user = self.request.user
        if user.role == 'CUSTOMER' and order.user != user:
            return Payment.objects.none()
        if user.role == 'STORE_OWNER':
            if not order.items.filter(product__store__owner=user).exists():
                return Payment.objects.none()
        return Payment.objects.filter(order=order)

    def perform_create(self, serializer):
        order = self.get_order()
        if order.user != self.request.user:
            raise ValidationError('Only the order owner can pay')
        if order.status == Order.Status.PAID:
            raise ValidationError('Order is already paid')
        if not order.items.exists():
            raise ValidationError('Order has no items')
        if Payment.objects.filter(order=order).exists():
            raise ValidationError('Payment already exists for this order')
        total_amount = sum(
            (item.quantity * item.price for item in order.items.all()),
            Decimal('0.00')
        )
        with transaction.atomic():
            serializer.save(order=order, amount=total_amount)
            order.status = Order.Status.PAID
            order.save(update_fields=['status'])

```

---

### <a id="📄-products-migrations-init-py"></a>📄 `products/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/migrations/__init__.py`
- **Relative Path**: `products/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-products-migrations-0001-initial-py"></a>📄 `products/migrations/0001_initial.py`

**File Info:**
- **Size**: 993 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/migrations/0001_initial.py`
- **Relative Path**: `products/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `5f1f378bccaa189a1707271ab91a7414`
- **SHA256**: `834baa91de3485432c836aebce909c043feb5545ae61cd03adbf5843c6c58f78`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.store')),
            ],
        ),
    ]

```

---

### <a id="📄-products-init-py"></a>📄 `products/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/__init__.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-products-admin-py"></a>📄 `products/admin.py`

**File Info:**
- **Size**: 66 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/admin.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `ef4c241c5311eee11a93e9366f492a72`
- **SHA256**: `a7ac68a753eeb831b6530bf71bf6917e577139f0734d17cc6a8666391564ab25`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

# Register your models here.

```

---

### <a id="📄-products-apps-py"></a>📄 `products/apps.py`

**File Info:**
- **Size**: 96 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/apps.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d75e75f846335c240d02b27064246407`
- **SHA256**: `408cbc7b67220e9fc52b7563ebde76f9ea2f4e82181380b9c4ecc36f5f5dad8e`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

```

---

### <a id="📄-products-models-py"></a>📄 `products/models.py`

**File Info:**
- **Size**: 499 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/models.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `5afe731e8b98ee9938bebfde1e9adbda`
- **SHA256**: `d687f8967abb1cc10499fd3f538d1fff2c5581ac37925b98c4f8c755857cd564`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models
from store.models import Store
# Create your models here.
class Product(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

---

### <a id="📄-products-permission-py"></a>📄 `products/permission.py`

**File Info:**
- **Size**: 543 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/permission.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `cacbdd1fe0ecbf0027735eee34d57464`
- **SHA256**: `7c15c3342f41f37ddd8a5a1d571f2a17953bc741e2e780dd84ec60bb8b8370eb`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProductStoreOwner(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        
        if request.method == 'POST':
            return request.user.role == 'STORE_OWNER'

        return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.store.owner == request.user
```

---

### <a id="📄-products-serializers-py"></a>📄 `products/serializers.py`

**File Info:**
- **Size**: 248 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/serializers.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `7d66a6f9417737fe3dfadf2c55457b29`
- **SHA256**: `48abf2616fe369bab5d959965e79bab68b1850a401f63f6b26f3496333be083f`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['store', 'created_at']
```

---

### <a id="📄-products-tests-py"></a>📄 `products/tests.py`

**File Info:**
- **Size**: 63 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/tests.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `e08f0582500f6562bf0a931ef9503b39`
- **SHA256**: `dae0da7efdcdb3a7fb572d5e914b60631099122d4a4727ac6434c016161c5fe1`
- **Encoding**: ASCII

**File code content:**

```python
from django.test import TestCase

# Create your tests here.

```

---

### <a id="📄-products-views-py"></a>📄 `products/views.py`

**File Info:**
- **Size**: 980 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `products/views.py`
- **Relative Path**: `products`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `4ca052ec05e14d76f962fe768b56d512`
- **SHA256**: `7cd4184972adb803d18256fbac71f187b8bf148225c024be2f681f6e4886e0a3`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from products.permission import IsProductStoreOwner

from .models import Product
from .serializers import ProductSerializer

from store.models import Store


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsProductStoreOwner]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        store_id = self.kwargs['store_pk']
        return Product.objects.filter(store_id=store_id)

    def perform_create(self, serializer):
        store_id = self.kwargs['store_pk']
        store = Store.objects.get(id=store_id)
        
        if store.owner != self.request.user:
            raise PermissionDenied('This store does not belong to you')

        serializer.save(store=store)
```

---

### <a id="📄-store-migrations-init-py"></a>📄 `store/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/migrations/__init__.py`
- **Relative Path**: `store/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-store-migrations-0001-initial-py"></a>📄 `store/migrations/0001_initial.py`

**File Info:**
- **Size**: 917 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/migrations/0001_initial.py`
- **Relative Path**: `store/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `055adda68a28d61a7cf932cfaa4749f1`
- **SHA256**: `7348e67a1b0b8768c11a030e01d69626be9953f2f6453c647b89b86e9b493168`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```

---

### <a id="📄-store-init-py"></a>📄 `store/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/__init__.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-store-admin-py"></a>📄 `store/admin.py`

**File Info:**
- **Size**: 66 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/admin.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `ef4c241c5311eee11a93e9366f492a72`
- **SHA256**: `a7ac68a753eeb831b6530bf71bf6917e577139f0734d17cc6a8666391564ab25`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

# Register your models here.

```

---

### <a id="📄-store-apps-py"></a>📄 `store/apps.py`

**File Info:**
- **Size**: 90 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/apps.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `863289c350efe01078adb3332153b95f`
- **SHA256**: `0bced40841d1bd763d1f0ca6222653de21d640cedf738ed29b3527b289b352c8`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

```

---

### <a id="📄-store-models-py"></a>📄 `store/models.py`

**File Info:**
- **Size**: 454 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/models.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `b8b5a6e460db85ebbb8f64eaea23de1a`
- **SHA256**: `096a0642911a59585b119d9eae321783c9315664eebb2d9a6f9d1fc3ac45844c`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='stores'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

---

### <a id="📄-store-permissions-py"></a>📄 `store/permissions.py`

**File Info:**
- **Size**: 531 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/permissions.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `dc3dbf9c7feef5add1abbd54cf4512d4`
- **SHA256**: `1850e389acf34726693ab635e9f4815c261a217dcf4369f41fb02e081cd9f5ad`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsStoreOwner(BasePermission):

    def has_permission(self, request, view):

        if request.method in ('GET'):
            return True
        
        if request.method == 'POST':
            return request.user.role == 'STORE_OWNER'

        return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
    
```

---

### <a id="📄-store-serializers-py"></a>📄 `store/serializers.py`

**File Info:**
- **Size**: 228 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/serializers.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `5524585ad3699148f48035d5326c6235`
- **SHA256**: `cd813d132d7e0c78c60683655cc52c299a5de6a556a9509d68f3011eb492075c`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['owner']
```

---

### <a id="📄-store-tests-py"></a>📄 `store/tests.py`

**File Info:**
- **Size**: 63 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/tests.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `e08f0582500f6562bf0a931ef9503b39`
- **SHA256**: `dae0da7efdcdb3a7fb572d5e914b60631099122d4a4727ac6434c016161c5fe1`
- **Encoding**: ASCII

**File code content:**

```python
from django.test import TestCase

# Create your tests here.

```

---

### <a id="📄-store-urls-py"></a>📄 `store/urls.py`

**File Info:**
- **Size**: 440 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/urls.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `87e3398c974c58ac236e3023e61199d9`
- **SHA256**: `886bb36f6d05aba3be4480af248a0c9e2e9bcff582dfc91a93e3b931057a9cc3`
- **Encoding**: ASCII

**File code content:**

```python
# stores/urls.py

from rest_framework_nested import routers

from .views import StoreViewSet
from products.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'', StoreViewSet, basename='stores')

stores_router = routers.NestedDefaultRouter(router, r'', lookup='store')
stores_router.register(r'products', ProductViewSet, basename='store-products')

urlpatterns = router.urls + stores_router.urls

```

---

### <a id="📄-store-views-py"></a>📄 `store/views.py`

**File Info:**
- **Size**: 522 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `store/views.py`
- **Relative Path**: `store`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `4151fda91cfdc63e0d1fb9dd8b002bab`
- **SHA256**: `a94b78c7450abfd73ae29326d16df6c519d383b8314ae6cedd615d35b89357a4`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from store.permissions import IsStoreOwner

from .models import Store
from .serializers import StoreSerializer


class StoreViewSet(ModelViewSet):

    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsStoreOwner]

    def get_queryset(self):
        return Store.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

---

### <a id="📄-users-management-commands-seed-benchmark-data-py"></a>📄 `users/management/commands/seed_benchmark_data.py`

**File Info:**
- **Size**: 2.03 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/management/commands/seed_benchmark_data.py`
- **Relative Path**: `users/management/commands`
- **Created**: 2026-05-17 18:59:35 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:00:32 (Asia/Damascus / GMT+03:00)
- **MD5**: `7a4e9c2dd28d38eb117f207bed5295f6`
- **SHA256**: `a613d5d7b15830dd6282585fdeaea7b6d36307693b1272793a6ff3a600e741ce`
- **Encoding**: ASCII

**File code content:**

```python
import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from products.models import Product
from store.models import Store
from users.models import User


class Command(BaseCommand):
    help = 'Seed deterministic store and product data for load testing.'

    def handle(self, *args, **options):
        owner, _ = User.objects.get_or_create(
            username='benchmark_owner',
            defaults={
                'email': 'benchmark_owner@example.com',
                'role': User.Roles.STORE_OWNER,
            },
        )
        owner.role = User.Roles.STORE_OWNER
        owner.email = 'benchmark_owner@example.com'
        owner.set_password('Benchmark123!')
        owner.save()

        store, _ = Store.objects.get_or_create(
            name='Benchmark Store',
            defaults={
                'description': 'Deterministic catalog used for benchmark runs.',
                'owner': owner,
            },
        )
        if store.owner != owner:
            store.owner = owner
            store.save(update_fields=['owner'])

        product, _ = Product.objects.get_or_create(
            store=store,
            name='Benchmark Product',
            defaults={
                'description': 'Seeded product for concurrent checkout tests.',
                'price': '19.99',
                'stock': 10000,
            },
        )
        if product.stock < 10000:
            product.stock = 10000
        product.price = '19.99'
        product.description = 'Seeded product for concurrent checkout tests.'
        product.save()

        context = {
            'store_id': store.id,
            'product_id': product.id,
            'quantity': 1,
        }
        context_path = Path(settings.BASE_DIR) / 'benchmark_context.json'
        context_path.write_text(json.dumps(context, indent=2), encoding='utf-8')

        self.stdout.write(self.style.SUCCESS(f'Benchmark context written to {context_path}'))
```

---

### <a id="📄-users-migrations-init-py"></a>📄 `users/migrations/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/migrations/__init__.py`
- **Relative Path**: `users/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-users-migrations-0001-initial-py"></a>📄 `users/migrations/0001_initial.py`

**File Info:**
- **Size**: 2.97 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/migrations/0001_initial.py`
- **Relative Path**: `users/migrations`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `70d3e9f454884d4bf1fb6eced01958ba`
- **SHA256**: `29eacb586577b49e89ac288be679c38e6b6049362b5e0c4c9886387e412fb75a`
- **Encoding**: ASCII

**File code content:**

```python
# Generated by Django 6.0.5 on 2026-05-12 05:53

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('CUSTOMER', 'Customer'), ('STORE_OWNER', 'Store Owner')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

```

---

### <a id="📄-users-init-py"></a>📄 `users/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/__init__.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-users-admin-py"></a>📄 `users/admin.py`

**File Info:**
- **Size**: 66 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/admin.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `ef4c241c5311eee11a93e9366f492a72`
- **SHA256**: `a7ac68a753eeb831b6530bf71bf6917e577139f0734d17cc6a8666391564ab25`
- **Encoding**: ASCII

**File code content:**

```python
from django.contrib import admin

# Register your models here.

```

---

### <a id="📄-users-apps-py"></a>📄 `users/apps.py`

**File Info:**
- **Size**: 90 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/apps.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `b58a3d79b02f68089b3ab907f861310d`
- **SHA256**: `c7d2701ca19f0e13c458fc56480ddbab050b7d8e76d7209621abd3070f87c0c1`
- **Encoding**: ASCII

**File code content:**

```python
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

```

---

### <a id="📄-users-models-py"></a>📄 `users/models.py`

**File Info:**
- **Size**: 606 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/models.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `0a9938ed0565da3f04c58c23a6b21ed4`
- **SHA256**: `93070b1cd5ac0c63e0d33724fb4b0a06a9d30bd47bf57817009964ef5f10804d`
- **Encoding**: ASCII

**File code content:**

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Roles(models.TextChoices):
        CUSTOMER= 'CUSTOMER', 'Customer'
        STORE_OWNER = 'STORE_OWNER', 'Store Owner'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices
    )

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new and self.role == self.Roles.CUSTOMER:
            from cart.models import Cart
            Cart.objects.get_or_create(user=self)

```

---

### <a id="📄-users-serializers-py"></a>📄 `users/serializers.py`

**File Info:**
- **Size**: 809 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/serializers.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `3b9d612c23b8a38591df0ed947cba592`
- **SHA256**: `7df387fc6edc258410b4fecf7249ba0801bbe5d5df2ffc90f258ff2e2c881bda`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    


class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()
    
    def save(self):
        refresh_token = self.validated_data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
```

---

### <a id="📄-users-tests-py"></a>📄 `users/tests.py`

**File Info:**
- **Size**: 63 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/tests.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `e08f0582500f6562bf0a931ef9503b39`
- **SHA256**: `dae0da7efdcdb3a7fb572d5e914b60631099122d4a4727ac6434c016161c5fe1`
- **Encoding**: ASCII

**File code content:**

```python
from django.test import TestCase

# Create your tests here.

```

---

### <a id="📄-users-urls-py"></a>📄 `users/urls.py`

**File Info:**
- **Size**: 380 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/urls.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `5629199579e67eac9f06594de51942f8`
- **SHA256**: `338cf3434d165b1978bca8e8789408057c7648fbfc10808907580cb8a2ed9856`
- **Encoding**: ASCII

**File code content:**

```python
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import LogoutView, RegisterView
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
]
```

---

### <a id="📄-users-views-py"></a>📄 `users/views.py`

**File Info:**
- **Size**: 876 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `users/views.py`
- **Relative Path**: `users`
- **Created**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:07 (Asia/Damascus / GMT+03:00)
- **MD5**: `2ac103ba59952f3fd5f93abef611208b`
- **SHA256**: `d2920ffcf568862b749258a179930b13dd6dd31b273b6a116c6144647530583f`
- **Encoding**: ASCII

**File code content:**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LogoutSerializer, RegisterSerializer

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Logged out successfully'},
            status=status.HTTP_205_RESET_CONTENT
        )
```

---

### <a id="📄-benchmark-context-json"></a>📄 `benchmark_context.json`

**File Info:**
- **Size**: 59 B
- **Extension**: `.json`
- **Language**: `json`
- **Location**: `benchmark_context.json`
- **Relative Path**: `root`
- **Created**: 2026-05-18 07:08:15 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 09:50:14 (Asia/Damascus / GMT+03:00)
- **MD5**: `98557768565ecd4e6edb49170ee19deb`
- **SHA256**: `78f87fea1344488c6b28ab457a7f4dae849440c814f0a49c20a32b21336f7ab6`
- **Encoding**: ASCII

**File code content:**

```json
{
  "store_id": 7,
  "product_id": 6,
  "quantity": 1
}
```

---

### <a id="📄-docker-compose-lb-yml"></a>📄 `docker-compose.lb.yml`

**File Info:**
- **Size**: 2.08 KB
- **Extension**: `.yml`
- **Language**: `yaml`
- **Location**: `docker-compose.lb.yml`
- **Relative Path**: `root`
- **Created**: 2026-05-17 18:58:57 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 10:29:29 (Asia/Damascus / GMT+03:00)
- **MD5**: `ef31637ecf66e50d696d0ef7bd88cc8d`
- **SHA256**: `c6bf27d931e3dab51f84ea044f9294808326ef8603a65e35e5b1cb473b2ba2f7`
- **Encoding**: ASCII

**File code content:**

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ecommerce
      POSTGRES_USER: ecommerce
      POSTGRES_PASSWORD: ecommerce
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web1:
    build: .
    environment:
      BACKEND_ID: app-1
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web1,web2,web3,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: sh -c "python manage.py migrate --noinput && gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000" --workers 4

  web2:
    build: .
    environment:
      BACKEND_ID: app-2
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web1,web2,web3,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000 --workers 4

  web3:
    build: .
    environment:
      BACKEND_ID: app-3
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web1,web2,web3,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000 --workers 4

  nginx:
    image: nginx:1.27-alpine
    depends_on:
      - web1
      - web2
      - web3
    ports:
      - "8080:80"
    volumes:
      - ./nginx/round-robin.conf:/etc/nginx/nginx.conf:ro

volumes:
  postgres_data:
```

---

### <a id="📄-docker-compose-least-yml"></a>📄 `docker-compose.least.yml`

**File Info:**
- **Size**: 2.18 KB
- **Extension**: `.yml`
- **Language**: `yaml`
- **Location**: `docker-compose.least.yml`
- **Relative Path**: `root`
- **Created**: 2026-05-17 18:58:57 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 10:29:46 (Asia/Damascus / GMT+03:00)
- **MD5**: `5274bfcd458a5ad5cde3d35103286c00`
- **SHA256**: `502863ddd79392538599a65016ad741b648f419b6ac87bf578b5d54d76f2cd57`
- **Encoding**: ASCII

**File code content:**

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ecommerce
      POSTGRES_USER: ecommerce
      POSTGRES_PASSWORD: ecommerce
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web1:
    build: .
    environment:
      BACKEND_ID: app-1
      DEMO_SLEEP_SECONDS: '0.05'
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web1,web2,web3,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: sh -c "python manage.py migrate --noinput && gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000" --workers 4

  web2:
    build: .
    environment:
      BACKEND_ID: app-2
      DEMO_SLEEP_SECONDS: '0.05'
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web1,web2,web3,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000 --workers 4

  web3:
    build: .
    environment:
      BACKEND_ID: app-3
      DEMO_SLEEP_SECONDS: '0.05'
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web1,web2,web3,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000 --workers 4

  nginx:
    image: nginx:1.27-alpine
    depends_on:
      - web1
      - web2
      - web3
    ports:
      - "8080:80"
    volumes:
      - ./nginx/least-connections.conf:/etc/nginx/nginx.conf:ro

volumes:
  postgres_data:
```

---

### <a id="📄-docker-compose-yml"></a>📄 `docker-compose.yml`

**File Info:**
- **Size**: 859 B
- **Extension**: `.yml`
- **Language**: `yaml`
- **Location**: `docker-compose.yml`
- **Relative Path**: `root`
- **Created**: 2026-05-17 18:58:57 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:00:32 (Asia/Damascus / GMT+03:00)
- **MD5**: `1989311cd480bd8736a172a01d5683ec`
- **SHA256**: `7a4205b3a59c3a0969887dd88e20d14e4c3bda3d56b6f42d5a56ac177ecfbfe8`
- **Encoding**: ASCII

**File code content:**

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ecommerce
      POSTGRES_USER: ecommerce
      POSTGRES_PASSWORD: ecommerce
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    environment:
      DJANGO_DEBUG: "False"
      DJANGO_ALLOWED_HOSTS: localhost,127.0.0.1,web,nginx
      DJANGO_SECRET_KEY: change-me-for-production
      DJANGO_DB_ENGINE: django.db.backends.postgresql
      DJANGO_DB_NAME: ecommerce
      DJANGO_DB_USER: ecommerce
      DJANGO_DB_PASSWORD: ecommerce
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 5432
    depends_on:
      - db
    command: sh -c "python manage.py migrate --noinput && gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000"
    ports:
      - "8000:8000"

volumes:
  postgres_data:
```

---

### <a id="📄-manage-py"></a>📄 `manage.py`

**File Info:**
- **Size**: 687 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `manage.py`
- **Relative Path**: `root`
- **Created**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-15 17:56:06 (Asia/Damascus / GMT+03:00)
- **MD5**: `1ac4a52ada1fffc207d6ad928d3ac240`
- **SHA256**: `7d2d4a8d5b7ec987f78f3a02fdccae2a1704961afed3327069429778253944b7`
- **Encoding**: ASCII

**File code content:**

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

---

### <a id="📄-pipfile-lock"></a>📄 `Pipfile.lock`

**File Info:**
- **Size**: 148.2 KB
- **Extension**: `.lock`
- **Language**: `text`
- **Location**: `Pipfile.lock`
- **Relative Path**: `root`
- **Created**: 2026-05-18 09:33:40 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-18 09:33:40 (Asia/Damascus / GMT+03:00)
- **MD5**: `9e368fb91ca7a9f0abab649c8b2b304a`
- **SHA256**: `99bc114f54c9ae9a55623d3ba5323eee3c5cf7b6b10dcd4b759c8da49ec574aa`
- **Encoding**: ASCII

**File code content:**

```text
{
    "_meta": {
        "hash": {
            "sha256": "386c2ff2614c85f9603b1542a5dde4a230140874c08aff1eb6aa241665ec30ca"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.14"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "aiohappyeyeballs": {
            "hashes": [
                "sha256:c3f9d0113123803ccadfdf3f0faa505bc78e6a72d1cc4806cbd719826e943558",
                "sha256:f349ba8f4b75cb25c99c5c2d84e997e485204d2902a9597802b0371f09331fb8"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==2.6.1"
        },
        "aiohttp": {
            "hashes": [
                "sha256:019a67772e034a0e6b9b17c13d0a8fe56ad9fb150fc724b7f3ffd3724288d9e5",
                "sha256:02222e7e233295f40e011c1b00e3b0bd451f22cf853a0304c3595633ee47da4b",
                "sha256:023ecba036ddd840b0b19bf195bfae970083fd7024ce1ac22e9bba90464620e9",
                "sha256:02e048037a6501a5ec1f6fc9736135aec6eb8a004ce48838cb951c515f32c80b",
                "sha256:0494a01ca9584eea1e5fbd6d748e61ecff218c51b576ee1999c23db7066417d8",
                "sha256:0f7a18f258d124cd678c5fe072fe4432a4d5232b0657fca7c1847f599233c83a",
                "sha256:10a75acfcf794edf9d8db50e5a7ec5fc818b2a8d3f591ce93bc7b1210df016d2",
                "sha256:110e448e02c729bcebb18c60b9214a87ba33bac4a9fa5e9a5f139938b56c6cb1",
                "sha256:147b4f501d0292077f29d5268c16bb7c864a1f054d7001c4c1812c0421ea1ed0",
                "sha256:157826e2fa245d2ef46c83ea8a5faf77ca19355d278d425c29fda0beb3318037",
                "sha256:15c933ad7920b7d9a20de151efcd05a6e38302cbf0e10c9b2acb9a42210a2416",
                "sha256:178c7b5e62b454c2bc790786e6058c3cc968613b4419251b478c153a4aec32b1",
                "sha256:18a2f6c1182c51baa1d28d68fea51513cb2a76612f038853c0ad3c145423d3d9",
                "sha256:1efb06900858bb618ff5cee184ae2de5828896c448403d51fb633f09e109be0a",
                "sha256:20058e23909b9e65f9da62b396b77dfa95965cbe840f8def6e572538b1d32e36",
                "sha256:206b7b3ef96e4ce211754f0cd003feb28b7d81f0ad26b8d077a5d5161436067f",
                "sha256:20ae0ff08b1f2c8788d6fb85afcb798654ae6ba0b747575f8562de738078457b",
                "sha256:2294172ce08a82fb7c7273485895de1fa1186cc8294cfeb6aef4af42ad261174",
                "sha256:241a94f7de7c0c3b616627aaad530fe2cb620084a8b144d3be7b6ecfe95bae3b",
                "sha256:26d2f8546f1dfa75efa50c3488215a903c0168d253b75fba4210f57ab77a0fb8",
                "sha256:2837fb92951564d6339cedae4a7231692aa9f73cbc4fb2e04263b96844e03b4e",
                "sha256:2994be9f6e51046c4f864598fd9abeb4fba6e88f0b2152422c9666dcd4aea9c6",
                "sha256:2d6d44a5b48132053c2f6cd5c8cb14bc67e99a63594e336b0f2af81e94d5530c",
                "sha256:31cebae8b26f8a615d2b546fee45d5ffb76852ae6450e2a03f42c9102260d6fe",
                "sha256:327cc432fdf1356fb4fbc6fe833ad4e9f6aacb71a8acaa5f1855e4b25910e4a9",
                "sha256:329f292ed14d38a6c4c435e465f48bebb47479fd676a0411936cc371643225cc",
                "sha256:330f5da04c987f1d5bdb8ae189137c77139f36bd1cb23779ca1a354a4b027800",
                "sha256:33add2463dde55c4f2d9635c6ab33ce154e5ecf322bd26d09af95c5f81cfa286",
                "sha256:347542f0ea3f95b2a955ee6656461fa1c776e401ac50ebce055a6c38454a0adf",
                "sha256:39380e12bd1f2fdab4285b6e055ad48efbaed5c836433b142ed4f5b9be71036a",
                "sha256:3a807cabd5115fb55af198b98178997a5e0e57dead43eb74a93d9c07d6d4a7dc",
                "sha256:3b13560160d07e047a93f23aaa30718606493036253d5430887514715b67c9d9",
                "sha256:3df334e39d4c2f899a914f1dba283c1aadc311790733f705182998c6f7cae665",
                "sha256:4bb6bf5811620003614076bdc807ef3b5e38244f9d25ca5fe888eaccea2a9832",
                "sha256:4beac52e9fe46d6abf98b0176a88154b742e878fdf209d2248e99fcdf73cd297",
                "sha256:4e704c52438f66fdd89588346183d898bb42167cf88f8b7ff1c0f9fc957c348f",
                "sha256:4eac02d9af4813ee289cd63a361576da36dba57f5a1ab36377bc2600db0cbb73",
                "sha256:53fc049ed6390d05423ba33103ded7281fe897cf97878f369a527070bd95795b",
                "sha256:55b3bdd3292283295774ab585160c4004f4f2f203946997f49aac032c84649e9",
                "sha256:57653eac22c6a4c13eb22ecf4d673d64a12f266e72785ab1c8b8e5940d0e8090",
                "sha256:60869c7ac4aaabe7110f26499f3e6e5696eae98144735b12a9c3d9eae2b51a49",
                "sha256:636bc362f0c5bbc7372bc3ae49737f9e3030dbce469f0f422c8f38079780363d",
                "sha256:676e5651705ad5d8a70aeb8eb6936c436d8ebbd56e63436cb7dd9bb36d2a9a46",
                "sha256:69f571de7500e0557801c0b51f4780482c0ec5fe2ac851af5a92cfce1af1cb83",
                "sha256:6a7cbeb06d1070f1d14895eeeed4dac5913b22d7b456f2eb969f11f4b3993796",
                "sha256:6cf81fe010b8c17b09495cbd15c1d35afbc8fb405c0c9cf4738e5ae3af1d65be",
                "sha256:6e27ea05d184afac78aabbac667450c75e54e35f62238d44463131bd3f96753d",
                "sha256:6f1cbf0c7926d315c3c26c2da41fd2b5d2fe01ac0e157b78caefc51a782196cf",
                "sha256:6f497a6876aa4b1a102b04996ce4c1170c7040d83faa9387dd921c16e30d5c83",
                "sha256:756c3c304d394977519824449600adaf2be0ccee76d206ee339c5e76b70ded25",
                "sha256:77dfa48c9f8013271011e51c00f8ada19851f013cde2c48fca1ba5e0caf5bb06",
                "sha256:7996023b2ed59489ae4762256c8516df9820f751cf2c5da8ed2fb20ee50abab3",
                "sha256:7ab7229b6f9b5c1ba4910d6c41a9eb11f543eadb3f384df1b4c293f4e73d44d6",
                "sha256:7becdf835feff2f4f335d7477f121af787e3504b48b449ff737afb35869ba7bb",
                "sha256:7c35b0bf0b48a70b4cb4fc5d7bed9b932532728e124874355de1a0af8ec4bc88",
                "sha256:7c4b6668b2b2b9027f209ddf647f2a4407784b5d88b8be4efcc72036f365baf9",
                "sha256:7e5dc4311bd5ac493886c63cbf76ab579dbe4641268e7c74e48e774c74b6f2be",
                "sha256:888e78eb5ca55a615d285c3c09a7a91b42e9dd6fc699b166ebd5dee87c9ccf14",
                "sha256:898703aa2667e3c5ca4c54ca36cd73f58b7a38ef87a5606414799ebce4d3fd3a",
                "sha256:8b14eb3262fad0dc2f89c1a43b13727e709504972186ff6a99a3ecaa77102b6c",
                "sha256:8bd3ec6376e68a41f9f95f5ed170e2fcf22d4eb27a1f8cb361d0508f6e0557f3",
                "sha256:8cf20a8d6868cb15a73cab329ffc07291ba8c22b1b88176026106ae39aa6df0f",
                "sha256:8f14c50708bb156b3a3ca7230b3d820199d56a48e3af76fa21c2d6087190fe3d",
                "sha256:8f546a4dc1e6a5edbb9fd1fd6ad18134550e096a5a43f4ad74acfbd834fc6670",
                "sha256:912d4b6af530ddb1338a66229dac3a25ff11d4448be3ec3d6340583995f56031",
                "sha256:9277145d36a01653863899c665243871434694bcc3431922c3b35c978061bdb8",
                "sha256:95d14ca7abefde230f7639ec136ade282655431fd5db03c343b19dda72dd1643",
                "sha256:999802d5fa0389f58decd24b537c54aa63c01c3219ce17d1214cbda3c2b22d2d",
                "sha256:9a0f4474b6ea6818b41f82172d799e4b3d29e22c2c520ce4357856fced9af2f8",
                "sha256:9b16c653d38eb1a611cc898c41e76859ca27f119d25b53c12875fd0474ae31a8",
                "sha256:9d98cc980ecc96be6eb4c1994ce35d28d8b1f5e5208a23b421187d1209dbb7d1",
                "sha256:9efcc0f11d850cefcafdd9275b9576ad3bfb539bed96807663b32ad99c4d4b88",
                "sha256:a2567b72e1ffc3ab25510db43f355b29eeada56c0a622e58dcdb19530eb0a3cb",
                "sha256:a5029cc80718bbd545123cd8fe5d15025eccaaaace5d0eeec6bd556ad6163d61",
                "sha256:a60eaa2d440cd4707696b52e40ed3e2b0f73f65be07fd0ef23b6b539c9c0b0b4",
                "sha256:a79a6d399cef33a11b6f004c67bb07741d91f2be01b8d712d52c75711b1e07c7",
                "sha256:a84792f8631bf5a94e52d9cc881c0b824ab42717165a5579c760b830d9392ac9",
                "sha256:a8a4d3427e8de1312ddf309cc482186466c79895b3a139fed3259fc01dfa9a5b",
                "sha256:a8aca50daa9493e9e13c0f566201a9006f080e7c50e5e90d0b06f53146a54500",
                "sha256:aa6d0d932e0f39c02b80744273cd5c388a2d9bc07760a03164f229c8e02662f6",
                "sha256:ab2899f9fa2f9f741896ebb6fa07c4c883bfa5c7f2ddd8cf2aafa86fa981b2d2",
                "sha256:af545c2cffdb0967a96b6249e6f5f7b0d92cdfd267f9d5238d5b9ca63e8edb10",
                "sha256:b18f31b80d5a33661e08c89e202edabf1986e9b49c42b4504371daeaa11b47c1",
                "sha256:b20df693de16f42b2472a9c485e1c948ee55524786a0a34345511afdd22246f3",
                "sha256:b38765950832f7d728297689ad78f5f2cf79ff82487131c4d26fe6ceecdc5f8e",
                "sha256:b6f6cd1560c5fa427e3b6074bb24d2c64e225afbb7165008903bd42e4e33e28a",
                "sha256:bace460460ed20614fa6bc8cb09966c0b8517b8c58ad8046828c6078d25333b5",
                "sha256:bca9ef7517fd7874a1a08970ae88f497bf5c984610caa0bf40bd7e8450852b95",
                "sha256:c180f480207a9b2475f2b8d8bd7204e47aec952d084b2a2be58a782ffcf96074",
                "sha256:c2b2355dc094e5f7d45a7bb262fe7207aa0460b37a0d87027dcf21b5d890e7d5",
                "sha256:c564dd5f09ddc9d8f2c2d0a301cd30a79a2cc1b46dd1a73bef8f0038863d016b",
                "sha256:c632ce9c0b534fbe25b52c974515ed674937c5b99f549a92127c85f771a78772",
                "sha256:c719f65bebcdf6716f10e9eff80d27567f7892d8988c06de12bbbd39307c6e3a",
                "sha256:c86969d012e51b8e415a8c6ce96f7857d6a87d6207303ab02d5d11ef0cad2274",
                "sha256:c974fb66180e58709b6fc402846f13791240d180b74de81d23913abe48e96d94",
                "sha256:c9883051c6972f58bfc4ebb2116345ee2aa151178e99c3f2b2bbe2af712abd13",
                "sha256:ca9ac61ac6db4eb6c2a0cd1d0f7e1357647b638ccc92f7e9d8d133e71ed3c6ac",
                "sha256:cb979826071c0986a5f08333a36104153478ce6018c58cba7f9caddaf63d5d67",
                "sha256:cd3db5927bf9167d5a6157ddb2f036f6b6b0ad001ac82355d43e97a4bde76d76",
                "sha256:d147004fede1b12f6013a6dbb2a26a986a671a03c6ea740ddc76500e5f1c399f",
                "sha256:d3a4834f221061624b8887090637db9ad4f61752001eae37d56c52fddade2dc8",
                "sha256:d9010032a0b9710f58012a1e9c222528763d860ba2ee1422c03473eab47703e7",
                "sha256:d97f93fdae594d886c5a866636397e2bcab146fd7a132fd6bb9ce182224452f8",
                "sha256:df23d57718f24badef8656c49743e11a89fd6f5358fa8a7b96e728fda2abf7d3",
                "sha256:df6104c009713d3a89621096f3e3e88cc323fd269dbd7c20afe18535094320be",
                "sha256:e5e5f7debc7a57af53fdf5c5009f9391d9f4c12867049d509bf7bb164a6e295b",
                "sha256:e7d2f8616f0ff60bd332022279011776c3ac0faa0f1b463f7bb12326fbc97a1c",
                "sha256:e999f0c88a458c836d5fb521814e92ed2172c649200336a6df514987c1488258",
                "sha256:eb4639f32fd4a9904ab8fb45bf3383ba71137f3d9d4ba25b3b3f3109977c5b8c",
                "sha256:ec707059ee75732b1ba130ed5f9580fe10ff75180c812bc267ded039db5128c6",
                "sha256:ecc26751323224cf8186efcf7fbcbc30f4e1d8c7970659daf25ad995e4032a56",
                "sha256:ee5e86776273de1795947d17bddd6bb19e0365fd2af4289c0d2c5454b6b1d36b",
                "sha256:f1162a1492032c82f14271e831c8f4b49f2b6078f4f5fc74de2c912fa225d51d",
                "sha256:f34ecee82858e41dd217734f0c41a532bd066bcaab636ad830f03a30b2a96f2a",
                "sha256:f85c6f327bf0b8c29da7d93b1cabb6363fb5e4e160a32fa241ed2dce21b73162",
                "sha256:f92995dfec9420bb69ae629abf422e516923ba79ba4403bc750d94fb4a6c68c1",
                "sha256:fb0540c854ac9c0c5ad495908fdfd3e332d553ec731698c0e29b1877ba0d2ec6",
                "sha256:fceedde51fbd67ee2bcc8c0b33d0126cc8b51ef3bbde2f86662bd6d5a6f10ec5",
                "sha256:fe6970addfea9e5e081401bcbadf865d2b6da045472f58af08427e108d618540",
                "sha256:fee86b7c4bd29bdaf0d53d14739b08a106fdda809ca5fe032a15f52fae5fe254"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.9'",
            "version": "==3.13.5"
        },
        "aiosignal": {
            "hashes": [
                "sha256:053243f8b92b990551949e63930a839ff0cf0b0ebbe0597b0f3fb19e1a0fe82e",
                "sha256:f47eecd9468083c2029cc99945502cb7708b082c232f9aca65da147157b251c7"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.4.0"
        },
        "asgiref": {
            "hashes": [
                "sha256:5f184dc43b7e763efe848065441eac62229c9f7b0475f41f80e207a114eda4ce",
                "sha256:e8667a091e69529631969fd45dc268fa79b99c92c5fcdda727757e52146ec133"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==3.11.1"
        },
        "attrs": {
            "hashes": [
                "sha256:c647aa4a12dfbad9333ca4e71fe62ddc36f4e63b2d260a37a8b83d2f043ac309",
                "sha256:d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==26.1.0"
        },
        "bidict": {
            "hashes": [
                "sha256:03069d763bc387bbd20e7d49914e75fc4132a41937fa3405417e1a5a2d006d71",
                "sha256:5dae8d4d79b552a71cbabc7deb25dfe8ce710b17ff41711e13010ead2abfc3e5"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.23.1"
        },
        "blinker": {
            "hashes": [
                "sha256:b4ce2265a7abece45e7cc896e98dbebe6cead56bcf805a3d23136d145f5445bf",
                "sha256:ba0efaa9080b619ff2f3459d1d500c57bddea4a6b424b60a91141db6fd2f08bc"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.9.0"
        },
        "brotli": {
            "hashes": [
                "sha256:022426c9e99fd65d9475dce5c195526f04bb8be8907607e27e747893f6ee3e24",
                "sha256:072e7624b1fc4d601036ab3f4f27942ef772887e876beff0301d261210bca97f",
                "sha256:09ac247501d1909e9ee47d309be760c89c990defbb2e0240845c892ea5ff0de4",
                "sha256:0bbd5b5ccd157ae7913750476d48099aaf507a79841c0d04a9db4415b14842de",
                "sha256:0cf8c3b8ba93d496b2fae778039e2f5ecc7cff99df84df337ca31d8f2252896c",
                "sha256:14ef29fc5f310d34fc7696426071067462c9292ed98b5ff5a27ac70a200e5470",
                "sha256:15b33fe93cedc4caaff8a0bd1eb7e3dab1c61bb22a0bf5bdfdfd97cd7da79744",
                "sha256:1b1d6a4efedd53671c793be6dd760fcf2107da3a52331ad9ea429edf0902f27a",
                "sha256:1b557b29782a643420e08d75aea889462a4a8796e9a6cf5621ab05a3f7da8ef2",
                "sha256:1b71754d5b6eda54d16fbbed7fce2d8bc6c052a1b91a35c320247946ee103502",
                "sha256:1ce223652fd4ed3eb2b7f78fbea31c52314baecfac68db44037bb4167062a937",
                "sha256:1e68cdf321ad05797ee41d1d09169e09d40fdf51a725bb148bff892ce04583d7",
                "sha256:260d3692396e1895c5034f204f0db022c056f9e2ac841593a4cf9426e2a3faca",
                "sha256:26e8d3ecb0ee458a9804f47f21b74845cc823fd1bb19f02272be70774f56e2a6",
                "sha256:2881416badd2a88a7a14d981c103a52a23a276a553a8aacc1346c2ff47c8dc17",
                "sha256:29b7e6716ee4ea0c59e3b241f682204105f7da084d6254ec61886508efeb43bc",
                "sha256:2a7f1d03727130fc875448b65b127a9ec5d06d19d0148e7554384229706f9d1b",
                "sha256:2d39b54b968f4b49b5e845758e202b1035f948b0561ff5e6385e855c96625971",
                "sha256:2e1ad3fda65ae0d93fec742a128d72e145c9c7a99ee2fcd667785d99eb25a7fe",
                "sha256:3173e1e57cebb6d1de186e46b5680afbd82fd4301d7b2465beebe83ed317066d",
                "sha256:3219bd9e69868e57183316ee19c84e03e8f8b5a1d1f2667e1aa8c2f91cb061ac",
                "sha256:350c8348f0e76fff0a0fd6c26755d2653863279d086d3aa2c290a6a7251135dd",
                "sha256:35d382625778834a7f3061b15423919aa03e4f5da34ac8e02c074e4b75ab4f84",
                "sha256:3b90b767916ac44e93a8e28ce6adf8d551e43affb512f2377c732d486ac6514e",
                "sha256:3e1b35d56856f3ed326b140d3c6d9db91740f22e14b06e840fe4bb1923439a18",
                "sha256:3ebe801e0f4e56d17cd386ca6600573e3706ce1845376307f5d2cbd32149b69a",
                "sha256:3f3c908bcc404c90c77d5a073e55271a0a498f4e0756e48127c35d91cf155947",
                "sha256:40d918bce2b427a0c4ba189df7a006ac0c7277c180aee4617d99e9ccaaf59e6a",
                "sha256:465a0d012b3d3e4f1d6146ea019b5c11e3e87f03d1676da1cc3833462e672fb0",
                "sha256:4735a10f738cb5516905a121f32b24ce196ab82cfc1e4ba2e3ad1b371085fd46",
                "sha256:4ecdb3b6dc36e6d6e14d3a1bdc6c1057c8cbf80db04031d566eb6080ce283a48",
                "sha256:50b1b799f45da91292ffaa21a473ab3a3054fa78560e8ff67082a185274431c8",
                "sha256:54a50a9dad16b32136b2241ddea9e4df159b41247b2ce6aac0b3276a66a8f1e5",
                "sha256:5732eff8973dd995549a18ecbd8acd692ac611c5c0bb3f59fa3541ae27b33be3",
                "sha256:598e88c736f63a0efec8363f9eb34e5b5536b7b6b1821e401afcb501d881f59a",
                "sha256:640fe199048f24c474ec6f3eae67c48d286de12911110437a36a87d7c89573a6",
                "sha256:66c02c187ad250513c2f4fce973ef402d22f80e0adce734ee4e4efd657b6cb64",
                "sha256:67a91c5187e1eec76a61625c77a6c8c785650f5b576ca732bd33ef58b0dff49c",
                "sha256:6be67c19e0b0c56365c6a76e393b932fb0e78b3b56b711d180dd7013cb1fd984",
                "sha256:6c12dad5cd04530323e723787ff762bac749a7b256a5bece32b2243dd5c27b21",
                "sha256:71a66c1c9be66595d628467401d5976158c97888c2c9379c034e1e2312c5b4f5",
                "sha256:7274942e69b17f9cef76691bcf38f2b2d4c8a5f5dba6ec10958363dcb3308a0a",
                "sha256:7547369c4392b47d30a3467fe8c3330b4f2e0f7730e45e3103d7d636678a808b",
                "sha256:7a47ce5c2288702e09dc22a44d0ee6152f2c7eda97b3c8482d826a1f3cfc7da7",
                "sha256:7a61c06b334bd99bc5ae84f1eeb36bfe01400264b3c352f968c6e30a10f9d08b",
                "sha256:7ad8cec81f34edf44a1c6a7edf28e7b7806dfb8886e371d95dcf789ccd4e4982",
                "sha256:7e9053f5fb4e0dfab89243079b3e217f2aea4085e4d58c5c06115fc34823707f",
                "sha256:7fa18d65a213abcfbb2f6cafbb4c58863a8bd6f2103d65203c520ac117d1944b",
                "sha256:81da1b229b1889f25adadc929aeb9dbc4e922bd18561b65b08dd9343cfccca84",
                "sha256:82676c2781ecf0ab23833796062786db04648b7aae8be139f6b8065e5e7b1518",
                "sha256:832c115a020e463c2f67664560449a7bea26b0c1fdd690352addad6d0a08714d",
                "sha256:844a8ceb8483fefafc412f85c14f2aae2fb69567bf2a0de53cdb88b73e7c43ae",
                "sha256:865cedc7c7c303df5fad14a57bc5db1d4f4f9b2b4d0a7523ddd206f00c121a16",
                "sha256:88ef7d55b7bcf3331572634c3fd0ed327d237ceb9be6066810d39020a3ebac7a",
                "sha256:898be2be399c221d2671d29eed26b6b2713a02c2119168ed914e7d00ceadb56f",
                "sha256:8d4f47f284bdd28629481c97b5f29ad67544fa258d9091a6ed1fda47c7347cd1",
                "sha256:92edab1e2fd6cd5ca605f57d4545b6599ced5dea0fd90b2bcdf8b247a12bd190",
                "sha256:9322b9f8656782414b37e6af884146869d46ab85158201d82bab9abbcb971dc7",
                "sha256:95db242754c21a88a79e01504912e537808504465974ebb92931cfca2510469e",
                "sha256:963a08f3bebd8b75ac57661045402da15991468a621f014be54e50f53a58d19e",
                "sha256:96fbe82a58cdb2f872fa5d87dedc8477a12993626c446de794ea025bbda625ea",
                "sha256:99cfa69813d79492f0e5d52a20fd18395bc82e671d5d40bd5a91d13e75e468e8",
                "sha256:9c79f57faa25d97900bfb119480806d783fba83cd09ee0b33c17623935b05fa3",
                "sha256:9e5825ba2c9998375530504578fd4d5d1059d09621a02065d1b6bfc41a8e05ab",
                "sha256:9fe11467c42c133f38d42289d0861b6b4f9da31e8087ca2c0d7ebb4543625526",
                "sha256:a1778532b978d2536e79c05dac2d8cd857f6c55cd0c95ace5b03740824e0e2f1",
                "sha256:a387225a67f619bf16bd504c37655930f910eb03675730fc2ad69d3d8b5e7e92",
                "sha256:a56ef534b66a749759ebd091c19c03ef81eb8cd96f0d1d16b59127eaf1b97a12",
                "sha256:aa47441fa3026543513139cb8926a92a8e305ee9c71a6209ef7a97d91640ea03",
                "sha256:ac27a70bda257ae3f380ec8310b0a06680236bea547756c277b5dfe55a2452a8",
                "sha256:acec55bb7c90f1dfc476126f9711a8e81c9af7fb617409a9ee2953115343f08d",
                "sha256:adedc4a67e15327dfdd04884873c6d5a01d3e3b6f61406f99b1ed4865a2f6d28",
                "sha256:af43b8711a8264bb4e7d6d9a6d004c3a2019c04c01127a868709ec29962b6036",
                "sha256:b232029d100d393ae3c603c8ffd7e3fe6f798c5e28ddca5feabb8e8fdb732997",
                "sha256:b35c13ce241abdd44cb8ca70683f20c0c079728a36a996297adb5334adfc1c44",
                "sha256:b63daa43d82f0cdabf98dee215b375b4058cce72871fd07934f179885aad16e8",
                "sha256:b908d1a7b28bc72dfb743be0d4d3f8931f8309f810af66c906ae6cd4127c93cb",
                "sha256:ba76177fd318ab7b3b9bf6522be5e84c2ae798754b6cc028665490f6e66b5533",
                "sha256:bba6e7e6cfe1e6cb6eb0b7c2736a6059461de1fa2c0ad26cf845de6c078d16c8",
                "sha256:c0d6770111d1879881432f81c369de5cde6e9467be7c682a983747ec800544e2",
                "sha256:c16ab1ef7bb55651f5836e8e62db1f711d55b82ea08c3b8083ff037157171a69",
                "sha256:c1702888c9f3383cc2f09eb3e88b8babf5965a54afb79649458ec7c3c7a63e96",
                "sha256:c25332657dee6052ca470626f18349fc1fe8855a56218e19bd7a8c6ad4952c49",
                "sha256:c8565e3cdc1808b1a34714b553b262c5de5fbda202285782173ec137fd13709f",
                "sha256:cf9cba6f5b78a2071ec6fb1e7bd39acf35071d90a81231d67e92d637776a6a63",
                "sha256:d206a36b4140fbb5373bf1eb73fb9de589bb06afd0d22376de23c5e91d0ab35f",
                "sha256:d2d085ded05278d1c7f65560aae97b3160aeb2ea2c0b3e26204856beccb60888",
                "sha256:d8c05b1dfb61af28ef37624385b0029df902ca896a639881f594060b30ffc9a7",
                "sha256:e310f77e41941c13340a95976fe66a8a95b01e783d430eeaf7a2f87e0a57dd0a",
                "sha256:e7c0af964e0b4e3412a0ebf341ea26ec767fa0b4cf81abb5e897c9338b5ad6a3",
                "sha256:e80a28f2b150774844c8b454dd288be90d76ba6109670fe33d7ff54d96eb5cb8",
                "sha256:e813da3d2d865e9793ef681d3a6b66fa4b7c19244a45b817d0cceda67e615990",
                "sha256:e85190da223337a6b7431d92c799fca3e2982abd44e7b8dec69938dcc81c8e9e",
                "sha256:e99befa0b48f3cd293dafeacdd0d191804d105d279e0b387a32054c1180f3161",
                "sha256:eda5a6d042c698e28bda2507a89b16555b9aa954ef1d750e1c20473481aff675",
                "sha256:ef87b8ab2704da227e83a246356a2b179ef826f550f794b2c52cddb4efbd0196",
                "sha256:f16dace5e4d3596eaeb8af334b4d2c820d34b8278da633ce4a00020b2eac981c",
                "sha256:f8d635cafbbb0c61327f942df2e3f474dde1cff16c3cd0580564774eaba1ee13",
                "sha256:fc1530af5c3c275b8524f2e24841cbe2599d74462455e9bae5109e9ff42e9361",
                "sha256:ff09cd8c5eec3b9d02d2408db41be150d8891c5566addce57513bf546e3d6c6d"
            ],
            "version": "==1.2.0"
        },
        "certifi": {
            "hashes": [
                "sha256:3cb2210c8f88ba2318d29b0388d1023c8492ff72ecdde4ebdaddbb13a31b1c4a",
                "sha256:8d455352a37b71bf76a79caa83a3d6c25afee4a385d632127b6afb3963f1c580"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==2026.4.22"
        },
        "cffi": {
            "hashes": [
                "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb",
                "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b",
                "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f",
                "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9",
                "sha256:0cf2d91ecc3fcc0625c2c530fe004f82c110405f101548512cce44322fa8ac44",
                "sha256:0f6084a0ea23d05d20c3edcda20c3d006f9b6f3fefeac38f59262e10cef47ee2",
                "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c",
                "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75",
                "sha256:1cd13c99ce269b3ed80b417dcd591415d3372bcac067009b6e0f59c7d4015e65",
                "sha256:1e3a615586f05fc4065a8b22b8152f0c1b00cdbc60596d187c2a74f9e3036e4e",
                "sha256:1f72fb8906754ac8a2cc3f9f5aaa298070652a0ffae577e0ea9bd480dc3c931a",
                "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e",
                "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25",
                "sha256:2081580ebb843f759b9f617314a24ed5738c51d2aee65d31e02f6f7a2b97707a",
                "sha256:21d1152871b019407d8ac3985f6775c079416c282e431a4da6afe7aefd2bccbe",
                "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b",
                "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91",
                "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592",
                "sha256:2c8f814d84194c9ea681642fd164267891702542f028a15fc97d4674b6206187",
                "sha256:2de9a304e27f7596cd03d16f1b7c72219bd944e99cc52b84d0145aefb07cbd3c",
                "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1",
                "sha256:3925dd22fa2b7699ed2617149842d2e6adde22b262fcbfada50e3d195e4b3a94",
                "sha256:3e17ed538242334bf70832644a32a7aae3d83b57567f9fd60a26257e992b79ba",
                "sha256:3e837e369566884707ddaf85fc1744b47575005c0a229de3327f8f9a20f4efeb",
                "sha256:3f4d46d8b35698056ec29bca21546e1551a205058ae1a181d871e278b0b28165",
                "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529",
                "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca",
                "sha256:4647afc2f90d1ddd33441e5b0e85b16b12ddec4fca55f0d9671fef036ecca27c",
                "sha256:4671d9dd5ec934cb9a73e7ee9676f9362aba54f7f34910956b84d727b0d73fb6",
                "sha256:53f77cbe57044e88bbd5ed26ac1d0514d2acf0591dd6bb02a3ae37f76811b80c",
                "sha256:5eda85d6d1879e692d546a078b44251cdd08dd1cfb98dfb77b670c97cee49ea0",
                "sha256:5fed36fccc0612a53f1d4d9a816b50a36702c28a2aa880cb8a122b3466638743",
                "sha256:61d028e90346df14fedc3d1e5441df818d095f3b87d286825dfcbd6459b7ef63",
                "sha256:66f011380d0e49ed280c789fbd08ff0d40968ee7b665575489afa95c98196ab5",
                "sha256:6824f87845e3396029f3820c206e459ccc91760e8fa24422f8b0c3d1731cbec5",
                "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4",
                "sha256:6d02d6655b0e54f54c4ef0b94eb6be0607b70853c45ce98bd278dc7de718be5d",
                "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b",
                "sha256:730cacb21e1bdff3ce90babf007d0a0917cc3e6492f336c2f0134101e0944f93",
                "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205",
                "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27",
                "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512",
                "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d",
                "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c",
                "sha256:81afed14892743bbe14dacb9e36d9e0e504cd204e0b165062c488942b9718037",
                "sha256:8941aaadaf67246224cee8c3803777eed332a19d909b47e29c9842ef1e79ac26",
                "sha256:89472c9762729b5ae1ad974b777416bfda4ac5642423fa93bd57a09204712322",
                "sha256:8ea985900c5c95ce9db1745f7933eeef5d314f0565b27625d9a10ec9881e1bfb",
                "sha256:8eca2a813c1cb7ad4fb74d368c2ffbbb4789d377ee5bb8df98373c2cc0dee76c",
                "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8",
                "sha256:9332088d75dc3241c702d852d4671613136d90fa6881da7d770a483fd05248b4",
                "sha256:94698a9c5f91f9d138526b48fe26a199609544591f859c870d477351dc7b2414",
                "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9",
                "sha256:9de40a7b0323d889cf8d23d1ef214f565ab154443c42737dfe52ff82cf857664",
                "sha256:a05d0c237b3349096d3981b727493e22147f934b20f6f125a3eba8f994bec4a9",
                "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775",
                "sha256:b18a3ed7d5b3bd8d9ef7a8cb226502c6bf8308df1525e1cc676c3680e7176739",
                "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc",
                "sha256:b21e08af67b8a103c71a250401c78d5e0893beff75e28c53c98f4de42f774062",
                "sha256:b4c854ef3adc177950a8dfc81a86f5115d2abd545751a304c5bcf2c2c7283cfe",
                "sha256:b882b3df248017dba09d6b16defe9b5c407fe32fc7c65a9c69798e6175601be9",
                "sha256:baf5215e0ab74c16e2dd324e8ec067ef59e41125d3eade2b863d294fd5035c92",
                "sha256:c649e3a33450ec82378822b3dad03cc228b8f5963c0c12fc3b1e0ab940f768a5",
                "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13",
                "sha256:c6638687455baf640e37344fe26d37c404db8b80d037c3d29f58fe8d1c3b194d",
                "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26",
                "sha256:cb527a79772e5ef98fb1d700678fe031e353e765d1ca2d409c92263c6d43e09f",
                "sha256:cf364028c016c03078a23b503f02058f1814320a56ad535686f90565636a9495",
                "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b",
                "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6",
                "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c",
                "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef",
                "sha256:da68248800ad6320861f129cd9c1bf96ca849a2771a59e0344e88681905916f5",
                "sha256:da902562c3e9c550df360bfa53c035b2f241fed6d9aef119048073680ace4a18",
                "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad",
                "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3",
                "sha256:de8dad4425a6ca6e4e5e297b27b5c824ecc7581910bf9aee86cb6835e6812aa7",
                "sha256:e11e82b744887154b182fd3e7e8512418446501191994dbf9c9fc1f32cc8efd5",
                "sha256:e6e73b9e02893c764e7e8d5bb5ce277f1a009cd5243f8228f75f842bf937c534",
                "sha256:f73b96c41e3b2adedc34a7356e64c8eb96e03a3782b535e043a986276ce12a49",
                "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2",
                "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5",
                "sha256:fc7de24befaeae77ba923797c7c87834c73648a05a4bde34b3b7e5588973a453",
                "sha256:fe562eb1a64e67dd297ccc4f5addea2501664954f2692b69a76449ec7913ecbf"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==2.0.0"
        },
        "charset-normalizer": {
            "hashes": [
                "sha256:007d05ec7321d12a40227aae9e2bc6dca73f3cb21058999a1df9e193555a9dcc",
                "sha256:03853ed82eeebbce3c2abfdbc98c96dc205f32a79627688ac9a27370ea61a49c",
                "sha256:07d9e39b01743c3717745f4c530a6349eadbfa043c7577eef86c502c15df2c67",
                "sha256:08e721811161356f97b4059a9ba7bafb23ea5ee2255402c42881c214e173c6b4",
                "sha256:0c96c3b819b5c3e9e165495db84d41914d6894d55181d2d108cc1a69bfc9cce0",
                "sha256:0ea948db76d31190bf08bd371623927ee1339d5f2a0b4b1b4a4439a65298703c",
                "sha256:0f7eb884681e3938906ed0434f20c63046eacd0111c4ba96f27b76084cd679f5",
                "sha256:12a6fff75f6bc66711b73a2f0addfc4c8c15a20e805146a02d147a318962c444",
                "sha256:12d8baf840cc7889b37c7c770f478adea7adce3dcb3944d02ec87508e2dcf153",
                "sha256:14265bfe1f09498b9d8ec91e9ec9fa52775edf90fcbde092b25f4a33d444fea9",
                "sha256:16d971e29578a5e97d7117866d15889a4a07befe0e87e703ed63cd90cb348c01",
                "sha256:177a0ba5f0211d488e295aaf82707237e331c24788d8d76c96c5a41594723217",
                "sha256:1a87ca9d5df6fe460483d9a5bbf2b18f620cbed41b432e2bddb686228282d10b",
                "sha256:1c2a768fdd44ee4a9339a9b0b130049139b8ce3c01d2ce09f67f5a68048d477c",
                "sha256:1c2aed2e5e41f24ea8ef1590b8e848a79b56f3a5564a65ceec43c9d692dc7d8a",
                "sha256:1dc8b0ea451d6e69735094606991f32867807881400f808a106ee1d963c46a83",
                "sha256:1efde3cae86c8c273f1eb3b287be7d8499420cf2fe7585c41d370d3e790054a5",
                "sha256:202389074300232baeb53ae2569a60901f7efadd4245cf3a3bf0617d60b439d7",
                "sha256:203104ed3e428044fd943bc4bf45fa73c0730391f9621e37fe39ecf477b128cb",
                "sha256:2257141f39fe65a3fdf38aeccae4b953e5f3b3324f4ff0daf9f15b8518666a2c",
                "sha256:298930cec56029e05497a76988377cbd7457ba864beeea92ad7e844fe74cd1f1",
                "sha256:2cd4a60d0e2fb04537162c62bbbb4182f53541fe0ede35cdf270a1c1e723cc42",
                "sha256:2d6eb928e13016cea4f1f21d1e10c1cebd5a421bc57ddf5b1142ae3f86824fab",
                "sha256:2fe249cb4651fd12605b7288b24751d8bfd46d35f12a20b1ba33dea122e690df",
                "sha256:30b8d1d8c52a48c2c5690e152c169b673487a2a58de1ec7393196753063fcd5e",
                "sha256:320ade88cfb846b8cd6b4ddf5ee9e80ee0c1f52401f2456b84ae1ae6a1a5f207",
                "sha256:3534e7dcbdcf757da6b85a0bbf5b6868786d5982dd959b065e65481644817a18",
                "sha256:36836d6ff945a00b88ba1e4572d721e60b5b8c98c155d465f56ad19d68f23734",
                "sha256:38c0109396c4cfc574d502df99742a45c72c08eff0a36158b6f04000043dbf38",
                "sha256:3946fa46a0cf3e4c8cb1cc52f56bb536310d34f25f01ca9b6c16afa767dab110",
                "sha256:3bec022aec2c514d9cf199522a802bd007cd588ab17ab2525f20f9c34d067c18",
                "sha256:3c9a494bc5ec77d43cea229c4f6db1e4d8fe7e1bbffa8b6f0f0032430ff8ab44",
                "sha256:3dce51d0f5e7951f8bb4900c257dad282f49190fdbebecd4ba99bcc41fef404d",
                "sha256:3dedcc22d73ec993f42055eff4fcfed9318d1eeb9a6606c55892a26964964e48",
                "sha256:4042d5c8f957e15221d423ba781e85d553722fc4113f523f2feb7b188cc34c5e",
                "sha256:481551899c856c704d58119b5025793fa6730adda3571971af568f66d2424bb5",
                "sha256:4dc1e73c36828f982bfe79fadf5919923f8a6f4df2860804db9a98c48824ce8d",
                "sha256:4e5163c14bffd570ef2affbfdd77bba66383890797df43dc8b4cc7d6f500bf53",
                "sha256:511ef87c8aec0783e08ac18565a16d435372bc1ac25a91e6ac7f5ef2b0bff790",
                "sha256:532bc9bf33a68613fd7d65e4b1c71a6a38d7d42604ecf239c77392e9b4e8998c",
                "sha256:54523e136b8948060c0fa0bc7b1b50c32c186f2fceee897a495406bb6e311d2b",
                "sha256:5649fd1c7bade02f320a462fdefd0b4bd3ce036065836d4f42e0de958038e116",
                "sha256:56be790f86bfb2c98fb742ce566dfb4816e5a83384616ab59c49e0604d49c51d",
                "sha256:5b77459df20e08151cd6f8b9ef8ef1f961ef73d85c21a555c7eed5b79410ec10",
                "sha256:5ed6ab538499c8644b8a3e18debabcd7ce684f3fa91cf867521a7a0279cab2d6",
                "sha256:6178f72c5508bfc5fd446a5905e698c6212932f25bcdd4b47a757a50605a90e2",
                "sha256:6370e8686f662e6a3941ee48ed4742317cafbe5707e36406e9df792cdb535776",
                "sha256:64f02c6841d7d83f832cd97ccf8eb8a906d06eb95d5276069175c696b024b60a",
                "sha256:65bcd23054beab4d166035cabbc868a09c1a49d1efe458fe8e4361215df40265",
                "sha256:66671f93accb62ed07da56613636f3641f1a12c13046ce91ffc923721f23c008",
                "sha256:6696b7688f54f5af4462118f0bfa7c1621eeb87154f77fa04b9295ce7a8f2943",
                "sha256:6785f414ae0f3c733c437e0f3929197934f526d19dfaa75e18fdb4f94c6fb374",
                "sha256:67f6279d125ca0046a7fd386d01b311c6363844deac3e5b069b514ba3e63c246",
                "sha256:6c114670c45346afedc0d947faf3c7f701051d2518b943679c8ff88befe14f8e",
                "sha256:6e0d51f618228538a3e8f46bd246f87a6cd030565e015803691603f55e12afb5",
                "sha256:6ed74185b2db44f41ef35fd1617c5888e59792da9bbc9190d6c7300617182616",
                "sha256:708838739abf24b2ceb208d0e22403dd018faeef86ddac04319a62ae884c4f15",
                "sha256:715479b9a2802ecac752a3b0efa2b0b60285cf962ee38414211abdfccc233b41",
                "sha256:733784b6d6def852c814bce5f318d25da2ee65dd4839a0718641c696e09a2960",
                "sha256:750e02e074872a3fad7f233b47734166440af3cdea0add3e95163110816d6752",
                "sha256:752a45dc4a6934060b3b0dab47e04edc3326575f82be64bc4fc293914566503e",
                "sha256:7579e913a5339fb8fa133f6bbcfd8e6749696206cf05acdbdca71a1b436d8e72",
                "sha256:7641bb8895e77f921102f72833904dcd9901df5d6d72a2ab8f31d04b7e51e4e7",
                "sha256:7804338df6fcc08105c7745f1502ba68d900f45fd770d5bdd5288ddccb8a42d8",
                "sha256:80d04837f55fc81da168b98de4f4b797ef007fc8a79ab71c6ec9bc4dd662b15b",
                "sha256:813c0e0132266c08eb87469a642cb30aaff57c5f426255419572aaeceeaa7bf4",
                "sha256:82b271f5137d07749f7bf32f70b17ab6eaabedd297e75dce75081a24f76eb545",
                "sha256:84c018e49c3bf790f9c2771c45e9313a08c2c2a6342b162cd650258b57817706",
                "sha256:8751d2787c9131302398b11e6c8068053dcb55d5a8964e114b6e196cf16cb366",
                "sha256:8778f0c7a52e56f75d12dae53ae320fae900a8b9b4164b981b9c5ce059cd1fcb",
                "sha256:87fad7d9ba98c86bcb41b2dc8dbb326619be2562af1f8ff50776a39e55721c5a",
                "sha256:8d828b6667a32a728a1ad1d93957cdf37489c57b97ae6c4de2860fa749b8fc1e",
                "sha256:8e385e4267ab76874ae30db04c627faaaf0b509e1ccc11a95b3fc3e83f855c00",
                "sha256:92a0a01ead5e668468e952e4238cccd7c537364eb7d851ab144ab6627dbbe12f",
                "sha256:94e1885b270625a9a828c9793b4d52a64445299baa1fea5a173bf1d3dd9a1a5a",
                "sha256:a180c5e59792af262bf263b21a3c49353f25945d8d9f70628e73de370d55e1e1",
                "sha256:a277ab8928b9f299723bc1a2dabb1265911b1a76341f90a510368ca44ad9ab66",
                "sha256:a5fe03b42827c13cdccd08e6c0247b6a6d4b5e3cdc53fd1749f5896adcdc2356",
                "sha256:a6c5863edfbe888d9eff9c8b8087354e27618d9da76425c119293f11712a6319",
                "sha256:a89c23ef8d2c6b27fd200a42aa4ac72786e7c60d40efdc76e6011260b6e949c4",
                "sha256:adb2597b428735679446b46c8badf467b4ca5f5056aae4d51a19f9570301b1ad",
                "sha256:ae196f021b5e7c78e918242d217db021ed2a6ace2bc6ae94c0fc596221c7f58d",
                "sha256:ae89db9e5f98a11a4bf50407d4363e7b09b31e55bc117b4f7d80aab97ba009e5",
                "sha256:aed52fea0513bac0ccde438c188c8a471c4e0f457c2dd20cdbf6ea7a450046c7",
                "sha256:aef65cd602a6d0e0ff6f9930fcb1c8fec60dd2cfcb6facaf4bdb0e5873042db0",
                "sha256:af21eb4409a119e365397b2adbaca4c9ccab56543a65d5dbd9f920d6ac29f686",
                "sha256:b14b2d9dac08e28bb8046a1a0434b1750eb221c8f5b87a68f4fa11a6f97b5e34",
                "sha256:bb6d88045545b26da47aa879dd4a89a71d1dce0f0e549b1abcb31dfe4a8eac49",
                "sha256:bb8cc7534f51d9a017b93e3e85b260924f909601c3df002bcdb58ddb4dc41a5c",
                "sha256:bc17a677b21b3502a21f66a8cc64f5bfad4df8a0b8434d661666f8ce90ac3af1",
                "sha256:bd6c2a1c7573c64738d716488d2cdd3c00e340e4835707d8fdb8dc1a66ef164e",
                "sha256:bd9b23791fe793e4968dba0c447e12f78e425c59fc0e3b97f6450f4781f3ee60",
                "sha256:c03a41a8784091e67a39648f70c5f97b5b6a37f216896d44d2cdcb82615339a0",
                "sha256:c0f081d69a6e58272819b70288d3221a6ee64b98df852631c80f293514d3b274",
                "sha256:c35abb8bfff0185efac5878da64c45dafd2b37fb0383add1be155a763c1f083d",
                "sha256:c36c333c39be2dbca264d7803333c896ab8fa7d4d6f0ab7edb7dfd7aea6e98c0",
                "sha256:c45e9440fb78f8ddabcf714b68f936737a121355bf59f3907f4e17721b9d1aae",
                "sha256:c593052c465475e64bbfe5dbd81680f64a67fdc752c56d7a0ae205dc8aeefe0f",
                "sha256:cdd68a1fb318e290a2077696b7eb7a21a49163c455979c639bf5a5dcdc46617d",
                "sha256:ce3412fbe1e31eb81ea42f4169ed94861c56e643189e1e75f0041f3fe7020abe",
                "sha256:cf1493cd8607bec4d8a7b9b004e699fcf8f9103a9284cc94962cb73d20f9d4a3",
                "sha256:cf29836da5119f3c8a8a70667b0ef5fdca3bb12f80fd06487cfa575b3909b393",
                "sha256:d4a48e5b3c2a489fae013b7589308a40146ee081f6f509e047e0e096084ceca1",
                "sha256:d560742f3c0d62afaccf9f41fe485ed69bd7661a241f86a3ef0f0fb8b1a397af",
                "sha256:d6038d37043bced98a66e68d3aa2b6a35505dc01328cd65217cefe82f25def44",
                "sha256:d61f00a0869d77422d9b2aba989e2d24afa6ffd552af442e0e58de4f35ea6d00",
                "sha256:d635aab80466bc95771bb78d5370e74d36d1fe31467b6b29b8b57b2a3cd7d22c",
                "sha256:dca4bbc466a95ba9c0234ef56d7dd9509f63da22274589ebd4ed7f1f4d4c54e3",
                "sha256:dd915403e231e6b1809fe9b6d9fc55cf8fb5e02765ac625d9cd623342a7905d7",
                "sha256:e044c39e41b92c845bc815e5ae4230804e8e7bc29e399b0437d64222d92809dd",
                "sha256:e060d01aec0a910bdccb8be71faf34e7799ce36950f8294c8bf612cba65a2c9e",
                "sha256:e1421b502d83040e6d7fb2fb18dff63957f720da3d77b2fbd3187ceb63755d7b",
                "sha256:e17b8d5d6a8c47c85e68ca8379def1303fd360c3e22093a807cd34a71cd082b8",
                "sha256:e5f4d355f0a2b1a31bc3edec6795b46324349c9cb25eed068049e4f472fb4259",
                "sha256:e712b419df8ba5e42b226c510472b37bd57b38e897d3eca5e8cfd410a29fa859",
                "sha256:e74327fb75de8986940def6e8dee4f127cc9752bee7355bb323cc5b2659b6d46",
                "sha256:e80c8378d8f3d83cd3164da1ad2df9e37a666cdde7b1cb2298ed0b558064be30",
                "sha256:e8ac484bf18ce6975760921bb6148041faa8fef0547200386ea0b52b5d27bf7b",
                "sha256:eca9705049ad3c7345d574e3510665cb2cf844c2f2dcfe675332677f081cbd46",
                "sha256:ed065083d0898c9d5b4bbec7b026fd755ff7454e6e8b73a67f8c744b13986e24",
                "sha256:edac0f1ab77644605be2cbba52e6b7f630731fc42b34cb0f634be1a6eface56a",
                "sha256:effc3f449787117233702311a1b7d8f59cba9ced946ba727bdc329ec69028e24",
                "sha256:f22dec1690b584cea26fade98b2435c132c1b5f68e39f5a0b7627cd7ae31f1dc",
                "sha256:f495a1652cf3fbab2eb0639776dad966c2fb874d79d87ca07f9d5f059b8bd215",
                "sha256:f496c9c3cc02230093d8330875c4c3cdfc3b73612a5fd921c65d39cbcef08063",
                "sha256:f59099f9b66f0d7145115e6f80dd8b1d847176df89b234a5a6b3f00437aa0832",
                "sha256:f59ad4c0e8f6bba240a9bb85504faa1ab438237199d4cce5f622761507b8f6a6",
                "sha256:fbccdc05410c9ee21bbf16a35f4c1d16123dcdeb8a1d38f33654fa21d0234f79",
                "sha256:fea24543955a6a729c45a73fe90e08c743f0b3334bbf3201e6c4bc1b0c7fa464"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==3.4.7"
        },
        "click": {
            "hashes": [
                "sha256:40c50b7c6c6adac2823d411041ec84f3f103f1b280d5e9ce0d7f998995832f81",
                "sha256:638f1338fe1235c8f4e008e4a8a254fb5c5fbdcbb40ece3c9142ebb78e792973"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==8.4.0"
        },
        "colorama": {
            "hashes": [
                "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44",
                "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6'",
            "version": "==0.4.6"
        },
        "configargparse": {
            "hashes": [
                "sha256:1e63fdffedf94da9cd435fc13a1cd24777e76879dd2343912c1f871d4ac8c592",
                "sha256:e3f9a7bb6be34d66b2e3c4a2f58e3045f8dfae47b0dc039f87bcfaa0f193fb0f"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==1.7.5"
        },
        "django": {
            "hashes": [
                "sha256:9d58a7cb49244e74c8e161d5e403a46d6209f1009ba40f5a66d6aa0d0786a8f0",
                "sha256:bc6d6872e98a2864c836e42edd644b362db311147dd5aa8d5b82ba7a032f5269"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.12'",
            "version": "==6.0.5"
        },
        "djangorestframework": {
            "hashes": [
                "sha256:a6def5f447fe78ff853bff1d47a3c59bf38f5434b031780b351b0c73a62db1a5",
                "sha256:c3c74dd3e83a5a3efc37b3c18d92bd6f86a6791c7b7d4dff62bb068500e76457"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.10'",
            "version": "==3.17.1"
        },
        "djangorestframework-simplejwt": {
            "hashes": [
                "sha256:2c30f3707053d384e9f315d11c2daccfcb548d4faa453111ca19a542b732e469",
                "sha256:e72c5572f51d7803021288e2057afcbd03f17fe11d484096f40a460abc76e87f"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.9'",
            "version": "==5.5.1"
        },
        "drf-nested-routers": {
            "hashes": [
                "sha256:815978f802e578fd7035c74040c104909cbe97615de89a275d77e928f4029891",
                "sha256:dd489c33d667aaa81383ffaa8c74781d2b353d8f0795716ae37fc59ee297b7c4"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.8'",
            "version": "==0.95.0"
        },
        "flask": {
            "hashes": [
                "sha256:0ef0e52b8a9cd932855379197dd8f94047b359ca0a78695144304cb45f87c9eb",
                "sha256:f4bcbefc124291925f1a26446da31a5178f9483862233b23c0c96a20701f670c"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==3.1.3"
        },
        "flask-cors": {
            "hashes": [
                "sha256:6e118f3698249ae33e429760db98ce032a8bf9913638d085ca0f4c5534ad2423",
                "sha256:e57544d415dfd7da89a9564e1e3a9e515042df76e12130641ca6f3f2f03b699a"
            ],
            "markers": "python_version >= '3.9' and python_version < '4.0'",
            "version": "==6.0.2"
        },
        "flask-login": {
            "hashes": [
                "sha256:5e23d14a607ef12806c699590b89d0f0e0d67baeec599d75947bf9c147330333",
                "sha256:849b25b82a436bf830a054e74214074af59097171562ab10bfa999e6b78aae5d"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==0.6.3"
        },
        "frozenlist": {
            "hashes": [
                "sha256:0325024fe97f94c41c08872db482cf8ac4800d80e79222c6b0b7b162d5b13686",
                "sha256:032efa2674356903cd0261c4317a561a6850f3ac864a63fc1583147fb05a79b0",
                "sha256:03ae967b4e297f58f8c774c7eabcce57fe3c2434817d4385c50661845a058121",
                "sha256:06be8f67f39c8b1dc671f5d83aaefd3358ae5cdcf8314552c57e7ed3e6475bdd",
                "sha256:073f8bf8becba60aa931eb3bc420b217bb7d5b8f4750e6f8b3be7f3da85d38b7",
                "sha256:07cdca25a91a4386d2e76ad992916a85038a9b97561bf7a3fd12d5d9ce31870c",
                "sha256:09474e9831bc2b2199fad6da3c14c7b0fbdd377cce9d3d77131be28906cb7d84",
                "sha256:0c18a16eab41e82c295618a77502e17b195883241c563b00f0aa5106fc4eaa0d",
                "sha256:0f96534f8bfebc1a394209427d0f8a63d343c9779cda6fc25e8e121b5fd8555b",
                "sha256:102e6314ca4da683dca92e3b1355490fed5f313b768500084fbe6371fddfdb79",
                "sha256:11847b53d722050808926e785df837353bd4d75f1d494377e59b23594d834967",
                "sha256:119fb2a1bd47307e899c2fac7f28e85b9a543864df47aa7ec9d3c1b4545f096f",
                "sha256:13d23a45c4cebade99340c4165bd90eeb4a56c6d8a9d8aa49568cac19a6d0dc4",
                "sha256:154e55ec0655291b5dd1b8731c637ecdb50975a2ae70c606d100750a540082f7",
                "sha256:168c0969a329b416119507ba30b9ea13688fafffac1b7822802537569a1cb0ef",
                "sha256:17c883ab0ab67200b5f964d2b9ed6b00971917d5d8a92df149dc2c9779208ee9",
                "sha256:1a7607e17ad33361677adcd1443edf6f5da0ce5e5377b798fba20fae194825f3",
                "sha256:1a7fa382a4a223773ed64242dbe1c9c326ec09457e6b8428efb4118c685c3dfd",
                "sha256:1aa77cb5697069af47472e39612976ed05343ff2e84a3dcf15437b232cbfd087",
                "sha256:1b9290cf81e95e93fdf90548ce9d3c1211cf574b8e3f4b3b7cb0537cf2227068",
                "sha256:20e63c9493d33ee48536600d1a5c95eefc870cd71e7ab037763d1fbb89cc51e7",
                "sha256:21900c48ae04d13d416f0e1e0c4d81f7931f73a9dfa0b7a8746fb2fe7dd970ed",
                "sha256:229bf37d2e4acdaf808fd3f06e854a4a7a3661e871b10dc1f8f1896a3b05f18b",
                "sha256:2552f44204b744fba866e573be4c1f9048d6a324dfe14475103fd51613eb1d1f",
                "sha256:27c6e8077956cf73eadd514be8fb04d77fc946a7fe9f7fe167648b0b9085cc25",
                "sha256:28bd570e8e189d7f7b001966435f9dac6718324b5be2990ac496cf1ea9ddb7fe",
                "sha256:294e487f9ec720bd8ffcebc99d575f7eff3568a08a253d1ee1a0378754b74143",
                "sha256:29548f9b5b5e3460ce7378144c3010363d8035cea44bc0bf02d57f5a685e084e",
                "sha256:2c5dcbbc55383e5883246d11fd179782a9d07a986c40f49abe89ddf865913930",
                "sha256:2dc43a022e555de94c3b68a4ef0b11c4f747d12c024a520c7101709a2144fb37",
                "sha256:2f05983daecab868a31e1da44462873306d3cbfd76d1f0b5b69c473d21dbb128",
                "sha256:33139dc858c580ea50e7e60a1b0ea003efa1fd42e6ec7fdbad78fff65fad2fd2",
                "sha256:332db6b2563333c5671fecacd085141b5800cb866be16d5e3eb15a2086476675",
                "sha256:33f48f51a446114bc5d251fb2954ab0164d5be02ad3382abcbfe07e2531d650f",
                "sha256:34187385b08f866104f0c0617404c8eb08165ab1272e884abc89c112e9c00746",
                "sha256:342c97bf697ac5480c0a7ec73cd700ecfa5a8a40ac923bd035484616efecc2df",
                "sha256:3462dd9475af2025c31cc61be6652dfa25cbfb56cbbf52f4ccfe029f38decaf8",
                "sha256:39ecbc32f1390387d2aa4f5a995e465e9e2f79ba3adcac92d68e3e0afae6657c",
                "sha256:3e0761f4d1a44f1d1a47996511752cf3dcec5bbdd9cc2b4fe595caf97754b7a0",
                "sha256:3ede829ed8d842f6cd48fc7081d7a41001a56f1f38603f9d49bf3020d59a31ad",
                "sha256:3ef2d026f16a2b1866e1d86fc4e1291e1ed8a387b2c333809419a2f8b3a77b82",
                "sha256:405e8fe955c2280ce66428b3ca55e12b3c4e9c336fb2103a4937e891c69a4a29",
                "sha256:42145cd2748ca39f32801dad54aeea10039da6f86e303659db90db1c4b614c8c",
                "sha256:4314debad13beb564b708b4a496020e5306c7333fa9a3ab90374169a20ffab30",
                "sha256:433403ae80709741ce34038da08511d4a77062aa924baf411ef73d1146e74faf",
                "sha256:44389d135b3ff43ba8cc89ff7f51f5a0bb6b63d829c8300f79a2fe4fe61bcc62",
                "sha256:48e6d3f4ec5c7273dfe83ff27c91083c6c9065af655dc2684d2c200c94308bb5",
                "sha256:494a5952b1c597ba44e0e78113a7266e656b9794eec897b19ead706bd7074383",
                "sha256:4970ece02dbc8c3a92fcc5228e36a3e933a01a999f7094ff7c23fbd2beeaa67c",
                "sha256:4e0c11f2cc6717e0a741f84a527c52616140741cd812a50422f83dc31749fb52",
                "sha256:50066c3997d0091c411a66e710f4e11752251e6d2d73d70d8d5d4c76442a199d",
                "sha256:517279f58009d0b1f2e7c1b130b377a349405da3f7621ed6bfae50b10adf20c1",
                "sha256:54b2077180eb7f83dd52c40b2750d0a9f175e06a42e3213ce047219de902717a",
                "sha256:5500ef82073f599ac84d888e3a8c1f77ac831183244bfd7f11eaa0289fb30714",
                "sha256:581ef5194c48035a7de2aefc72ac6539823bb71508189e5de01d60c9dcd5fa65",
                "sha256:59a6a5876ca59d1b63af8cd5e7ffffb024c3dc1e9cf9301b21a2e76286505c95",
                "sha256:5a3a935c3a4e89c733303a2d5a7c257ea44af3a56c8202df486b7f5de40f37e1",
                "sha256:5c1c8e78426e59b3f8005e9b19f6ff46e5845895adbde20ece9218319eca6506",
                "sha256:5d63a068f978fc69421fb0e6eb91a9603187527c86b7cd3f534a5b77a592b888",
                "sha256:667c3777ca571e5dbeb76f331562ff98b957431df140b54c85fd4d52eea8d8f6",
                "sha256:6da155091429aeba16851ecb10a9104a108bcd32f6c1642867eadaee401c1c41",
                "sha256:6dc4126390929823e2d2d9dc79ab4046ed74680360fc5f38b585c12c66cdf459",
                "sha256:7398c222d1d405e796970320036b1b563892b65809d9e5261487bb2c7f7b5c6a",
                "sha256:74c51543498289c0c43656701be6b077f4b265868fa7f8a8859c197006efb608",
                "sha256:776f352e8329135506a1d6bf16ac3f87bc25b28e765949282dcc627af36123aa",
                "sha256:778a11b15673f6f1df23d9586f83c4846c471a8af693a22e066508b77d201ec8",
                "sha256:78f7b9e5d6f2fdb88cdde9440dc147259b62b9d3b019924def9f6478be254ac1",
                "sha256:799345ab092bee59f01a915620b5d014698547afd011e691a208637312db9186",
                "sha256:7bf6cdf8e07c8151fba6fe85735441240ec7f619f935a5205953d58009aef8c6",
                "sha256:8009897cdef112072f93a0efdce29cd819e717fd2f649ee3016efd3cd885a7ed",
                "sha256:80f85f0a7cc86e7a54c46d99c9e1318ff01f4687c172ede30fd52d19d1da1c8e",
                "sha256:8585e3bb2cdea02fc88ffa245069c36555557ad3609e83be0ec71f54fd4abb52",
                "sha256:878be833caa6a3821caf85eb39c5ba92d28e85df26d57afb06b35b2efd937231",
                "sha256:8a76ea0f0b9dfa06f254ee06053d93a600865b3274358ca48a352ce4f0798450",
                "sha256:8b7b94a067d1c504ee0b16def57ad5738701e4ba10cec90529f13fa03c833496",
                "sha256:8d92f1a84bb12d9e56f818b3a746f3efba93c1b63c8387a73dde655e1e42282a",
                "sha256:908bd3f6439f2fef9e85031b59fd4f1297af54415fb60e4254a95f75b3cab3f3",
                "sha256:92db2bf818d5cc8d9c1f1fc56b897662e24ea5adb36ad1f1d82875bd64e03c24",
                "sha256:940d4a017dbfed9daf46a3b086e1d2167e7012ee297fef9e1c545c4d022f5178",
                "sha256:957e7c38f250991e48a9a73e6423db1bb9dd14e722a10f6b8bb8e16a0f55f695",
                "sha256:96153e77a591c8adc2ee805756c61f59fef4cf4073a9275ee86fe8cba41241f7",
                "sha256:96f423a119f4777a4a056b66ce11527366a8bb92f54e541ade21f2374433f6d4",
                "sha256:97260ff46b207a82a7567b581ab4190bd4dfa09f4db8a8b49d1a958f6aa4940e",
                "sha256:974b28cf63cc99dfb2188d8d222bc6843656188164848c4f679e63dae4b0708e",
                "sha256:9ff15928d62a0b80bb875655c39bf517938c7d589554cbd2669be42d97c2cb61",
                "sha256:a6483e309ca809f1efd154b4d37dc6d9f61037d6c6a81c2dc7a15cb22c8c5dca",
                "sha256:a88f062f072d1589b7b46e951698950e7da00442fc1cacbe17e19e025dc327ad",
                "sha256:ac913f8403b36a2c8610bbfd25b8013488533e71e62b4b4adce9c86c8cea905b",
                "sha256:adbeebaebae3526afc3c96fad434367cafbfd1b25d72369a9e5858453b1bb71a",
                "sha256:b2a095d45c5d46e5e79ba1e5b9cb787f541a8dee0433836cea4b96a2c439dcd8",
                "sha256:b3210649ee28062ea6099cfda39e147fa1bc039583c8ee4481cb7811e2448c51",
                "sha256:b37f6d31b3dcea7deb5e9696e529a6aa4a898adc33db82da12e4c60a7c4d2011",
                "sha256:b4dec9482a65c54a5044486847b8a66bf10c9cb4926d42927ec4e8fd5db7fed8",
                "sha256:b4f3b365f31c6cd4af24545ca0a244a53688cad8834e32f56831c4923b50a103",
                "sha256:b6db2185db9be0a04fecf2f241c70b63b1a242e2805be291855078f2b404dd6b",
                "sha256:b9be22a69a014bc47e78072d0ecae716f5eb56c15238acca0f43d6eb8e4a5bda",
                "sha256:bac9c42ba2ac65ddc115d930c78d24ab8d4f465fd3fc473cdedfccadb9429806",
                "sha256:bf0a7e10b077bf5fb9380ad3ae8ce20ef919a6ad93b4552896419ac7e1d8e042",
                "sha256:c23c3ff005322a6e16f71bf8692fcf4d5a304aaafe1e262c98c6d4adc7be863e",
                "sha256:c4c800524c9cd9bac5166cd6f55285957fcfc907db323e193f2afcd4d9abd69b",
                "sha256:c7366fe1418a6133d5aa824ee53d406550110984de7637d65a178010f759c6ef",
                "sha256:c8d1634419f39ea6f5c427ea2f90ca85126b54b50837f31497f3bf38266e853d",
                "sha256:c9a63152fe95756b85f31186bddf42e4c02c6321207fd6601a1c89ebac4fe567",
                "sha256:cb89a7f2de3602cfed448095bab3f178399646ab7c61454315089787df07733a",
                "sha256:cba69cb73723c3f329622e34bdbf5ce1f80c21c290ff04256cff1cd3c2036ed2",
                "sha256:cee686f1f4cadeb2136007ddedd0aaf928ab95216e7691c63e50a8ec066336d0",
                "sha256:cf253e0e1c3ceb4aaff6df637ce033ff6535fb8c70a764a8f46aafd3d6ab798e",
                "sha256:d1eaff1d00c7751b7c6662e9c5ba6eb2c17a2306ba5e2a37f24ddf3cc953402b",
                "sha256:d3bb933317c52d7ea5004a1c442eef86f426886fba134ef8cf4226ea6ee1821d",
                "sha256:d4d3214a0f8394edfa3e303136d0575eece0745ff2b47bd2cb2e66dd92d4351a",
                "sha256:d6a5df73acd3399d893dafc71663ad22534b5aa4f94e8a2fabfe856c3c1b6a52",
                "sha256:d8b7138e5cd0647e4523d6685b0eac5d4be9a184ae9634492f25c6eb38c12a47",
                "sha256:db1e72ede2d0d7ccb213f218df6a078a9c09a7de257c2fe8fcef16d5925230b1",
                "sha256:e25ac20a2ef37e91c1b39938b591457666a0fa835c7783c3a8f33ea42870db94",
                "sha256:e2de870d16a7a53901e41b64ffdf26f2fbb8917b3e6ebf398098d72c5b20bd7f",
                "sha256:e4a3408834f65da56c83528fb52ce7911484f0d1eaf7b761fc66001db1646eff",
                "sha256:eaa352d7047a31d87dafcacbabe89df0aa506abb5b1b85a2fb91bc3faa02d822",
                "sha256:eab8145831a0d56ec9c4139b6c3e594c7a83c2c8be25d5bcf2d86136a532287a",
                "sha256:ec3cc8c5d4084591b4237c0a272cc4f50a5b03396a47d9caaf76f5d7b38a4f11",
                "sha256:edee74874ce20a373d62dc28b0b18b93f645633c2943fd90ee9d898550770581",
                "sha256:eefdba20de0d938cec6a89bd4d70f346a03108a19b9df4248d3cf0d88f1b0f51",
                "sha256:ef2b7b394f208233e471abc541cc6991f907ffd47dc72584acee3147899d6565",
                "sha256:f21f00a91358803399890ab167098c131ec2ddd5f8f5fd5fe9c9f2c6fcd91e40",
                "sha256:f4be2e3d8bc8aabd566f8d5b8ba7ecc09249d74ba3c9ed52e54dc23a293f0b92",
                "sha256:f57fb59d9f385710aa7060e89410aeb5058b99e62f4d16b08b91986b9a2140c2",
                "sha256:f6292f1de555ffcc675941d65fffffb0a5bcd992905015f85d0592201793e0e5",
                "sha256:f833670942247a14eafbb675458b4e61c82e002a148f49e68257b79296e865c4",
                "sha256:fa47e444b8ba08fffd1c18e8cdb9a75db1b6a27f17507522834ad13ed5922b93",
                "sha256:fb30f9626572a76dfe4293c7194a09fb1fe93ba94c7d4f720dfae3b646b45027",
                "sha256:fe3c58d2f5db5fbd18c2987cba06d51b0529f52bc3a6cdc33d3f4eab725104bd"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.8.0"
        },
        "gevent": {
            "hashes": [
                "sha256:012a44b0121f3d7c800740ff80351c897e85e76a7e4764690f35c5ad9ec17de5",
                "sha256:03c74fec58eda4b4edc043311fca8ba4f8744ad1632eb0a41d5ec25413581975",
                "sha256:0adb937f13e5fb90cca2edf66d8d7e99d62a299687400ce2edee3f3504009356",
                "sha256:18e5aff9e8342dc954adb9c9c524db56c2f3557999463445ba3d9cbe3dada7b7",
                "sha256:1a3fe4ea1c312dbf6b375b416925036fe79a40054e6bf6248ee46526ea628be1",
                "sha256:1cdf6db28f050ee103441caa8b0448ace545364f775059d5e2de089da975c457",
                "sha256:1d0f5d8d73f97e24ea8d24d8be0f51e0cf7c54b8021c1fddb580bf239474690f",
                "sha256:2951bb070c0ee37b632ac9134e4fdaad70d2e660c931bb792983a0837fe5b7d7",
                "sha256:323a27192ec4da6b22a9e51c3d9d896ff20bc53fdc9e45e56eaab76d1c39dd74",
                "sha256:34e01e50c71eaf67e92c186ee0196a039d6e4f4b35670396baed4a2d8f1b347f",
                "sha256:427f869a2050a4202d93cf7fd6ab5cffb06d3e9113c10c967b6e2a0d45237cb8",
                "sha256:46b188248c84ffdec18a686fcac5dbb32365d76912e14fda350db5dc0bfd4f86",
                "sha256:4acd6bcd5feabf22c7c5174bd3b9535ee9f088d2bbce789f740ad8d6554b18f3",
                "sha256:4f84591d13845ee31c13f44bdf6bd6c3dbf385b5af98b2f25ec328213775f2ed",
                "sha256:5e4b6278b37373306fc6b1e5f0f1cf56339a1377f67c35972775143d8d7776ff",
                "sha256:6ea78b39a2c51d47ff0f130f4c755a9a4bbb2dd9721149420ad4712743911a51",
                "sha256:72152517ecf548e2f838c61b4be76637d99279dbaa7e01b3924df040aa996586",
                "sha256:7a834804ac00ed8a92a69d3826342c677be651b1c3cd66cc35df8bc711057aa2",
                "sha256:812debe235a8295be3b2a63b136c2474241fa5c58af55e6a0f8cfc29d4936235",
                "sha256:856b990be5590e44c3a3dc6c8d48a40eaccbb42e99d2b791d11d1e7711a4297e",
                "sha256:88b6c07169468af631dcf0fdd3658f9246d6822cc51461d43f7c44f28b0abb82",
                "sha256:8d94936f8f8b23d9de2251798fcb603b84f083fdf0d7f427183c1828fb64f117",
                "sha256:9cdbb24c276a2d0110ad5c978e49daf620b153719ac8a548ce1250a7eb1b9245",
                "sha256:a8ae9f895e8651d10b0a8328a61c9c53da11ea51b666388aa99b0ce90f9fdc27",
                "sha256:adf9cd552de44a4e6754c51ff2e78d9193b7fa6eab123db9578a210e657235dd",
                "sha256:b274a53e818124a281540ebb4e7a2c524778f745b7a99b01bdecf0ca3ac0ddb0",
                "sha256:b28b61ff9216a3d73fe8f35669eefcafa957f143ac534faf77e8a19eb9e6883a",
                "sha256:b56cbc820e3136ba52cd690bdf77e47a4c239964d5f80dc657c1068e0fe9521c",
                "sha256:b5a67a0974ad9f24721034d1e008856111e0535f1541499f72a733a73d658d1c",
                "sha256:b7bb0e29a7b3e6ca9bed2394aa820244069982c36dc30b70eb1004dd67851a48",
                "sha256:bb63c0d6cb9950cc94036a4995b9cc4667b8915366613449236970f4394f94d7",
                "sha256:c049880175e8c93124188f9d926af0a62826a3b81aa6d3074928345f8238279e",
                "sha256:c5fa9ce5122c085983e33e0dc058f81f5264cebe746de5c401654ab96dddfca8",
                "sha256:c6c91f7e33c7f01237755884316110ee7ea076f5bdb9aa0982b6dc63243c0a38",
                "sha256:d99f0cb2ce43c2e8305bf75bee61a8bde06619d21b9d0316ea190fc7a0620a56",
                "sha256:dc45cd3e1cc07514a419960af932a62eb8515552ed004e56755e4bf20bad30c5",
                "sha256:ddd3ff26e5c4240d3fbf5516c2d9d5f2a998ef87cfb73e1429cfaeaaec860fa6",
                "sha256:e4e17c2d57e9a42e25f2a73d297b22b60b2470a74be5a515b36c984e1a246d47",
                "sha256:eb51c5f9537b07da673258b4832f6635014fee31690c3f0944d34741b69f92fa",
                "sha256:f0d8b64057b4bf1529b9ef9bd2259495747fba93d1f836c77bfeaacfec373fd0",
                "sha256:f18f80aef6b1f6907219affe15b36677904f7cfeed1f6a6bc198616e507ae2d7",
                "sha256:f2b54ea3ca6f0c763281cd3f96010ac7e98c2e267feb1221b5a26e2ca0b9a692",
                "sha256:fe1599d0b30e6093eb3213551751b24feeb43db79f07e89d98dd2f3330c9063e"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==25.9.1"
        },
        "geventhttpclient": {
            "hashes": [
                "sha256:02e06a2f78a225b70e616b493317073f3e2fddd4e51ddfc44569d188f368bd8d",
                "sha256:04b8feec69fd662eb46b4f81013206f5a23d179b195cbaf590d4a59f641ed0fc",
                "sha256:0658266fa594931e5260f17c6f52f867597e5cb257e85f73990b2f61bad58ec7",
                "sha256:06df5597edf65d4c691052fce3e37620cbc037879a3b872bc16a7b2a0941d59a",
                "sha256:08f0df30086a0ce05d75180753095b913a5e676c83ff92f8f9779bd064536d3c",
                "sha256:09b82815247a1044c648bac1cee1e766e03e762950cae49cf61efffaeff667c4",
                "sha256:0f66a33c95e4d6d343fc6ace458b13c613684bf7cfd6832b61cc9c42eaf394f3",
                "sha256:0ff40ca5b848f96c6390bd8cc3a4c4598c119be08125cf1c30103201adc00940",
                "sha256:14daf2f0361f19b0221f900d7e9d563c184bb7186676e61fe848495b1f2483d3",
                "sha256:14eaa836bde26a70952e95ca462018f3a47c1c92642327315aa6502e54141016",
                "sha256:16807578dc4a175e8d97e6e39d65a10b04b5237a8c55f7a5ef39044e869baeb8",
                "sha256:1d0c2af2aff5b802cdec4b6b216348a32a2452f4e5f5f2e19fc5f84d77443649",
                "sha256:1dac4df42a954e19d3e737c4c4351332cf27e415c0e7b8850070fd8056237a04",
                "sha256:1e82a219e9f3d644832c8ed18dd0bc615f21ed18659e1d26e187b29f81dff9e1",
                "sha256:1ed08b02b7c275397a528028d526d28f056bce3dc5cd285a7a9d7d78b0975f5a",
                "sha256:224e4a959ece6673f4c57113013fc20ed020e661d6de3c820aa3afe2f1cf2e99",
                "sha256:25c03073a1136c2b93189488bb1bfc0868d90aa106dd49f15ac964d2454296c6",
                "sha256:269e861e7fc38994b315b50469c8e629e3a78321a049598c4f4a0f21053e5503",
                "sha256:2b244adcbf5814a29d5cea8b2fc079f9242d92765191faa4dc5eccc0421840ae",
                "sha256:2b91fb31523725ddc777c14b444ccedaf2043dcb9af0ede29056a9b8146c79a7",
                "sha256:2c71796fda35bfe5b4ae93cdca62fd4932ee95c2b36812ce65878183ca7da517",
                "sha256:31b463324d5fde983657247b2faea77f8f8a40f3f7ac0c2897a2fe3afa27d610",
                "sha256:38535589a564822c64d1b4c2a5d6dcc27159d0d7d76500f2c8c8d21d9dd54880",
                "sha256:39011c8cdd7ef8b6ab07592525f83018cd1504e8133cce5114bfcee5547b9bb5",
                "sha256:39afb8046fe04358a85956555aa6a1d931710bac386a2fceb5c24bbd4d7c10e7",
                "sha256:3eec8e442214d4086e40a3ae7fe1e1e3ecbc422157d8d2118059cf9977336d9f",
                "sha256:3fc084a475eca84257b1f77dd584678c7e4bdc625f66b0279f2cfa54901a5ef8",
                "sha256:4110273531fc9ac2ec197a44a90d9c7b4266b51a070747368e38213be281d5c2",
                "sha256:47a303bcac3d69569f025d0c81781c5f0c1a48c9f225e43082d1b56e4c0440f8",
                "sha256:47be91fae0e9cd6eb9eab821278994d519cf27678f9e47eb302d41efcc6cae1a",
                "sha256:4b9587beaccac950619f1defe0e1b9499a275edf8d912095f041060c62cb1aa3",
                "sha256:4f35a5adbb0770824e98372dcec6805180c3ee99287e52598a4fb3b5d1a2b8aa",
                "sha256:5000c9fb0553818c4e4c1de248ee4e9a56de0a245a30ef76b687542a935f4645",
                "sha256:52516d5c153fcef0d3d2447e533244dc6360e8c2a190b958861137db6f227605",
                "sha256:53977ca41809eaef73cf38af170484baa53bde5f16bafbca7b77b670c343f48f",
                "sha256:549155d557de403612336ca36cd93a049e67acbf9a29e6b6b971d0f4cb56786d",
                "sha256:5b542025a0c9905c847d1459e598ccbdcd21dc0dd050cc1d3813ce7e01bd350f",
                "sha256:5c824839aae388636a0496c71d71d7de0487c0458bfdd366da252265539aa88c",
                "sha256:61b046492e5a831c97b8c47623f980f2d1f9f36fdc94e858bc786fa7e4dffca5",
                "sha256:6c06e243de53f54942b098f81622917f4a33c16f44733c9371ea98a2cd5ce12e",
                "sha256:7b60c0b650c77d2644374149c38dfee34510e88e569ca85f38fe15f40ecaea1c",
                "sha256:829454480d001f43bce4a8373bfe282a418b09817c32ce9b369ce637ae5240ab",
                "sha256:83da9a0cab4c990ac48316bed696aa1ffc0e678cbca725c3e904b84ee9c5d3e1",
                "sha256:83dc6f037a50b7d2dc45af58a7e7978016a06320a5f823d1bd544c85d69f2058",
                "sha256:8e3b279da39ad3eee69a5df9e1b602f87bcd2cec7eb258d3cc801e2170682383",
                "sha256:90c1f2ca4d378a19005eb2a60376cfff4d6bceca4a569ca7bfec645b7a572c59",
                "sha256:98f3582a1c9effb56bc2db4f43d382cedd921217a139d5737eeaad3a1e307047",
                "sha256:98ff3350d8be75586076140bde565c35ccdd72a6840b88f94037ec6595407383",
                "sha256:9b16e30dbbc528453a4130210d83638444229357c073eb911421eb44e3367359",
                "sha256:9d0568d38cf74cecd37fd1ef65459f60ecd26dbc0d33bc2a1e0d8df4af24f07d",
                "sha256:a18b28d2f8bc7fcfc721227733bccb647602399db6b0fd093c00ff9699717b74",
                "sha256:a6436cd77885a8ef7cdc6d225cddd732560a17e92969c74e997836cf3135baa0",
                "sha256:a9757738669caebc4c96b529372362abc0c2cfe326b27bb9e67b5601fd5651f1",
                "sha256:ae44cec808193bb70b634fabdfdd89f0850744ace5668dc98063d633cf50c417",
                "sha256:af7931f55522cddedf84e837769c66d9ceb130b29182ad1e2d0201f501df899f",
                "sha256:b1f6c26e10b367629a2675bbd43ddedce1ba7ade13eb9ae3b3418e651c98fd9c",
                "sha256:b9bbcbc7d5d875e5180f2b1f1c6fa8e092ef80d9debfb6ba22a4ec28f0565395",
                "sha256:c4d5e1b9b1ac9baab42a1789bbfae7e97e40e8e83e09a32b353c6eb985f36071",
                "sha256:c582a6697c82a948d3d42094da941544606a0ebee31fc0aa6731e248eeba0e9b",
                "sha256:c840b05ec56d16783f24926de25ce38d3453673ce4786896c63febd2fb34a6cf",
                "sha256:c9091db18eeb53626a81e9280d602ae9e29706ee4c1e7a05edc8b07cc632b3fc",
                "sha256:caf8779ca686497e0fab1048b026b4e48fb14fb9e88ddbfd14ca1a1a4c4bfa89",
                "sha256:cd4efebba798c7f585aa1ceb9aba9524b12ebc51b26ad62de5234b8264d9b94d",
                "sha256:cf18417cabb210be64d1b610ced94387f4222fa4e0942486d5d5a6237d2dd9fa",
                "sha256:cfe23d419aa676492677374bdd37e364c921895d1090a180173be5d5f87f82b9",
                "sha256:d3d24480c3a2cc88311c41a042bc12ab8e4104dad6029591ecbf5a1e933e8a44",
                "sha256:d91139a4fafd77fa985535966d7a6c2e64753f340ab1395508ee83cd8de70c38",
                "sha256:d980c54f98bc623e10f94595de633690bbf690b915e6ef2298df6728b31f0285",
                "sha256:e1ac3a39e3c4ae36024ddf1694eb82b0cc22c4516f176477f94f98bcd56ce6cf",
                "sha256:e1e711eb91085585f61445c7313e1a0acb159b5dc11327930e673b4899ebd84f",
                "sha256:e3d120c2dbaf931fb1690ede4b7022bcaad82fa181e288b04d2f8a5e2d3d7eab",
                "sha256:e73b25415e83064f5a334e83495d97b138e66f67a98cfcad154068c257733973",
                "sha256:e8b30889ee4d5629904321da2a068ffb3a6114c7bcd46416051e869911b20a90",
                "sha256:ec656fd34f10fb0442446faece025dae848fc51e0b22f0ba1fc14c93e0f06ebb",
                "sha256:ecd2e843d1649cb5fba678240bb9778f6229b7315faa07a3696ccabcf289f609",
                "sha256:f74053954f4599afb48b2c7765532c7e0cb5b0f1d0a62da8342ac4b5aadb76f9",
                "sha256:f7cf60062d3aebd5e83f4d197a59609194effe25a25bcab01ae3775be18c877e",
                "sha256:f9d32fc9ba6d82c4f8586a6bd6e99c7e15a25404f94743dce00367aec826809d"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==2.3.9"
        },
        "greenlet": {
            "hashes": [
                "sha256:0ecec963079cd58cbd14723582384f11f166fd58883c15dcbfb342e0bc9b5846",
                "sha256:0ed006e4b86c59de7467eb2601cd1b77b5a7d657d1ee55e30fe30d76451edba4",
                "sha256:0ff251e9a0279522e62f6176412869395a64ddf2b5c5f782ff609a8216a4e662",
                "sha256:1aa4ce8debcd4ea7fb2e150f3036588c41493d1d52c43538924ae1819003f4ce",
                "sha256:1bae92a1dd94c5f9d9493c3a212dd874c202442047cf96446412c862feca83a2",
                "sha256:1eb67d5adefb5bd2e182d42678a328979a209e4e82eb93575708185d31d1f588",
                "sha256:2094acd54b272cb6eae8c03dd87b3fa1820a4cef18d6889c378d503500a1dc13",
                "sha256:2628d6c86f6cb0cb45e0c3c54058bbec559f57eaae699447748cb3928150577e",
                "sha256:29ea813b2e1f45fa9649a17853b2b5465c4072fbcb072e5af6cd3a288216574a",
                "sha256:362624e6a8e5bca3b8233e45eef33903a100e9539a2b995c364d595dbc4018b3",
                "sha256:3a717fbc46d8a354fa675f7c1e813485b6ba3885f9bef0cd56e5ba27d758ff5b",
                "sha256:3bc59be3945ae9750b9e7d45067d01ae3fe90ea5f9ade99239dabdd6e28a5033",
                "sha256:3ec9ea74e7268ace7f9aab1b1a4e730193fc661b39a993cd91c606c32d4a3628",
                "sha256:41353ec2ecedf7aa8f682753a41919f8718031a6edac46b8d3dc7ed9e1ceb136",
                "sha256:47422135b1d308c14b2c6e758beedb1acd33bb91679f5670edf77bf46244722b",
                "sha256:4964101b8585c144cbda5532b1aa644255126c08a265dae90c16e7a0e63aaa9d",
                "sha256:4a448128607be0de65342dc9b31be7f948ef4cc0bc8832069350abefd310a8f2",
                "sha256:4b28037cb07768933c54d81bfe47a85f9f402f57d7d69743b991a713b63954eb",
                "sha256:4d0eadc7e4d9ffb2af4247b606cae307be8e448911e5a0d0b16d72fc3d224cfd",
                "sha256:54d243512da35485fc7a6bf3c178fdda6327a9d6506fcdd62b1abd1e41b2927b",
                "sha256:55fa7ea52771be44af0de27d8b80c02cd18c2c3cddde6c847ecebdf72418b6a1",
                "sha256:57a43c6079a89713522bc4bcb9f75070ecf5d3dbad7792bfe42239362cbf2a16",
                "sha256:58c1c374fe2b3d852f9b6b11a7dff4c85404e51b9a596fd9e89cf904eb09866d",
                "sha256:5a5ed18de6a0f6cc7087f1563f6bd93fc7df1c19165ca01e9bde5a5dc281d106",
                "sha256:5e05ba267789ea87b5a155cf0e810b1ab88bf18e9e8740813945ceb8ee4350ba",
                "sha256:5ecd83806b0f4c2f53b1018e0005cd82269ea01d42befc0368730028d850ed1c",
                "sha256:64d6ac45f7271f48e45f67c95b54ef73534c52ec041fcda8edf520c6d811f4bc",
                "sha256:680bd0e7ad5e8daa8a4aa89f68fd6adc834b8a8036dc256533f7e08f4a4b01f7",
                "sha256:6c18dfb59c70f5a94acd271c72e90128c3c776e41e5f07767908c8c1b74ad339",
                "sha256:6d874e79afd41a96e11ff4c5d0bc90a80973e476fda1c2c64985667397df432b",
                "sha256:7022615368890680e67b9965d33f5773aade330d5343bbe25560135aaa849eae",
                "sha256:703cb211b820dbffbbc55a16bfc6e4583a6e6e990f33a119d2cc8b83211119c8",
                "sha256:728a73687e39ae9ca34e4694cbf2f049d3fbc7174639468d0f67200a97d8f9e2",
                "sha256:728d9667d8f2f586644b748dbd9bb67e50d6a9381767d1357714ea6825bb3bf5",
                "sha256:762612baf1161ccb8437c0161c668a688223cba28e1bf038f4eb47b13e39ccdf",
                "sha256:7fc391b1566f2907d17aaebe78f8855dc45675159a775fcf9e61f8ee0078e87f",
                "sha256:804a70b328e706b785c6ef16187051c394a63dd1a906d89be24b6ad77759f13f",
                "sha256:83ed9f27f1680b50e89f40f6df348a290ea234b249a4003d366663a12eab94f2",
                "sha256:884f649de075b84739713d41dd4dfd41e2b910bfb769c4a3ea02ec1da52cd9bb",
                "sha256:8f1cc966c126639cd152fdaa52624d2655f492faa79e013fea161de3e6dda082",
                "sha256:8f52a464e4ed91780bdfbbdd2b97197f3accaa629b98c200f4dffada759f3ae7",
                "sha256:9c615f869163e14bb1ced20322d8038fb680b08236521ac3f30cd4c1288785a0",
                "sha256:9d280a7f5c331622c69f97eb167f33577ff2d1df282c41cd15907fc0a3ca198c",
                "sha256:a10a732421ab4fec934783ce3e54763470d0181db6e3468f9103a275c3ed1853",
                "sha256:a96fcee45e03fe30a62669fd16ab5c9d3c172660d3085605cb1e2d1280d3c988",
                "sha256:a97e4821aa710603f94de0da25f25096454d78ffdace5dc77f3a006bc01abba3",
                "sha256:ba8f0bdc2fae6ce915dfd0c16d2d00bca7e4247c1eae4416e06430e522137858",
                "sha256:bf2d8a80bec89ab46221ae45c5373d5ba0bd36c19aa8508e85c6cd7e5106cd37",
                "sha256:cda05425526240807408156b6960a17a79a0c760b813573b67027823be760977",
                "sha256:d419647372241bc68e957bf38d5c1f98852155e4146bd1e4121adea81f4f01e4",
                "sha256:d4d9f0624c775f2dfc56ba54d515a8c771044346852a918b405914f6b19d7fd8",
                "sha256:d60097128cb0a1cab9ea541186ea13cd7b847b8449a7787c2e2350da0cb82d86",
                "sha256:db2910d3c809444e0a20147361f343fe2798e106af8d9d8506f5305302655a9f",
                "sha256:ddb36c7d6c9c0a65f18c7258634e0c416c6ab59caac8c987b96f80c2ebda0112",
                "sha256:ddc090c5c1792b10246a78e8c2163ebbe04cf877f9d785c230a7b27b39ad038e",
                "sha256:e5ddf316ced87539144621453c3aef229575825fe60c604e62bedc4003f372b2",
                "sha256:f35807464c4c58c55f0d31dfa83c541a5615d825c2fe3d2b95360cf7c4e3c0a8",
                "sha256:f8c30c2225f40dd76c50790f0eb3b5c7c18431efb299e2782083e1981feed243",
                "sha256:fa94cb2288681e3a11645958f1871d48ee9211bd2f66628fdace505927d6e564"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==3.5.0"
        },
        "gunicorn": {
            "hashes": [
                "sha256:40233d26a5f0d1872916188c276e21641155111c2853f0c2cd55260aec0d24fc",
                "sha256:ca9346f85e3a4aeeb64d491045c16b9a35647abd37ea15efe53080eb8b090baf"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.10'",
            "version": "==26.0.0"
        },
        "h11": {
            "hashes": [
                "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1",
                "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.16.0"
        },
        "idna": {
            "hashes": [
                "sha256:048adeaf8c2d788c40fee287673ccaa74c24ffd8dcf09ffa555a2fbb59f10ac8",
                "sha256:ca962446ea538f7092a95e057da437618e886f4d349216d2b1e294abfdb65fdc"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==3.15"
        },
        "iniconfig": {
            "hashes": [
                "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730",
                "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==2.3.0"
        },
        "itsdangerous": {
            "hashes": [
                "sha256:c6242fc49e35958c8b15141343aa660db5fc54d4f13a1db01a3f5891b98700ef",
                "sha256:e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==2.2.0"
        },
        "jinja2": {
            "hashes": [
                "sha256:0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d",
                "sha256:85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==3.1.6"
        },
        "locust": {
            "hashes": [
                "sha256:338a9fd5389b30df96439baba8299193b5efc1f129763cd9bc6108354fb52547",
                "sha256:5dd69aae3dfca8e25c2565e5c4491b21984b41877406b8172ea96cfa9d76c0e5"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.10'",
            "version": "==2.44.0"
        },
        "markupsafe": {
            "hashes": [
                "sha256:0303439a41979d9e74d18ff5e2dd8c43ed6c6001fd40e5bf2e43f7bd9bbc523f",
                "sha256:068f375c472b3e7acbe2d5318dea141359e6900156b5b2ba06a30b169086b91a",
                "sha256:0bf2a864d67e76e5c9a34dc26ec616a66b9888e25e7b9460e1c76d3293bd9dbf",
                "sha256:0db14f5dafddbb6d9208827849fad01f1a2609380add406671a26386cdf15a19",
                "sha256:0eb9ff8191e8498cca014656ae6b8d61f39da5f95b488805da4bb029cccbfbaf",
                "sha256:0f4b68347f8c5eab4a13419215bdfd7f8c9b19f2b25520968adfad23eb0ce60c",
                "sha256:1085e7fbddd3be5f89cc898938f42c0b3c711fdcb37d75221de2666af647c175",
                "sha256:116bb52f642a37c115f517494ea5feb03889e04df47eeff5b130b1808ce7c219",
                "sha256:12c63dfb4a98206f045aa9563db46507995f7ef6d83b2f68eda65c307c6829eb",
                "sha256:133a43e73a802c5562be9bbcd03d090aa5a1fe899db609c29e8c8d815c5f6de6",
                "sha256:1353ef0c1b138e1907ae78e2f6c63ff67501122006b0f9abad68fda5f4ffc6ab",
                "sha256:15d939a21d546304880945ca1ecb8a039db6b4dc49b2c5a400387cdae6a62e26",
                "sha256:177b5253b2834fe3678cb4a5f0059808258584c559193998be2601324fdeafb1",
                "sha256:1872df69a4de6aead3491198eaf13810b565bdbeec3ae2dc8780f14458ec73ce",
                "sha256:1b4b79e8ebf6b55351f0d91fe80f893b4743f104bff22e90697db1590e47a218",
                "sha256:1b52b4fb9df4eb9ae465f8d0c228a00624de2334f216f178a995ccdcf82c4634",
                "sha256:1ba88449deb3de88bd40044603fafffb7bc2b055d626a330323a9ed736661695",
                "sha256:1cc7ea17a6824959616c525620e387f6dd30fec8cb44f649e31712db02123dad",
                "sha256:218551f6df4868a8d527e3062d0fb968682fe92054e89978594c28e642c43a73",
                "sha256:26a5784ded40c9e318cfc2bdb30fe164bdb8665ded9cd64d500a34fb42067b1c",
                "sha256:2713baf880df847f2bece4230d4d094280f4e67b1e813eec43b4c0e144a34ffe",
                "sha256:2a15a08b17dd94c53a1da0438822d70ebcd13f8c3a95abe3a9ef9f11a94830aa",
                "sha256:2f981d352f04553a7171b8e44369f2af4055f888dfb147d55e42d29e29e74559",
                "sha256:32001d6a8fc98c8cb5c947787c5d08b0a50663d139f1305bac5885d98d9b40fa",
                "sha256:3524b778fe5cfb3452a09d31e7b5adefeea8c5be1d43c4f810ba09f2ceb29d37",
                "sha256:3537e01efc9d4dccdf77221fb1cb3b8e1a38d5428920e0657ce299b20324d758",
                "sha256:35add3b638a5d900e807944a078b51922212fb3dedb01633a8defc4b01a3c85f",
                "sha256:38664109c14ffc9e7437e86b4dceb442b0096dfe3541d7864d9cbe1da4cf36c8",
                "sha256:3a7e8ae81ae39e62a41ec302f972ba6ae23a5c5396c8e60113e9066ef893da0d",
                "sha256:3b562dd9e9ea93f13d53989d23a7e775fdfd1066c33494ff43f5418bc8c58a5c",
                "sha256:457a69a9577064c05a97c41f4e65148652db078a3a509039e64d3467b9e7ef97",
                "sha256:4bd4cd07944443f5a265608cc6aab442e4f74dff8088b0dfc8238647b8f6ae9a",
                "sha256:4e885a3d1efa2eadc93c894a21770e4bc67899e3543680313b09f139e149ab19",
                "sha256:4faffd047e07c38848ce017e8725090413cd80cbc23d86e55c587bf979e579c9",
                "sha256:509fa21c6deb7a7a273d629cf5ec029bc209d1a51178615ddf718f5918992ab9",
                "sha256:5678211cb9333a6468fb8d8be0305520aa073f50d17f089b5b4b477ea6e67fdc",
                "sha256:591ae9f2a647529ca990bc681daebdd52c8791ff06c2bfa05b65163e28102ef2",
                "sha256:5a7d5dc5140555cf21a6fefbdbf8723f06fcd2f63ef108f2854de715e4422cb4",
                "sha256:69c0b73548bc525c8cb9a251cddf1931d1db4d2258e9599c28c07ef3580ef354",
                "sha256:6b5420a1d9450023228968e7e6a9ce57f65d148ab56d2313fcd589eee96a7a50",
                "sha256:722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698",
                "sha256:729586769a26dbceff69f7a7dbbf59ab6572b99d94576a5592625d5b411576b9",
                "sha256:77f0643abe7495da77fb436f50f8dab76dbc6e5fd25d39589a0f1fe6548bfa2b",
                "sha256:795e7751525cae078558e679d646ae45574b47ed6e7771863fcc079a6171a0fc",
                "sha256:7be7b61bb172e1ed687f1754f8e7484f1c8019780f6f6b0786e76bb01c2ae115",
                "sha256:7c3fb7d25180895632e5d3148dbdc29ea38ccb7fd210aa27acbd1201a1902c6e",
                "sha256:7e68f88e5b8799aa49c85cd116c932a1ac15caaa3f5db09087854d218359e485",
                "sha256:83891d0e9fb81a825d9a6d61e3f07550ca70a076484292a70fde82c4b807286f",
                "sha256:8485f406a96febb5140bfeca44a73e3ce5116b2501ac54fe953e488fb1d03b12",
                "sha256:8709b08f4a89aa7586de0aadc8da56180242ee0ada3999749b183aa23df95025",
                "sha256:8f71bc33915be5186016f675cd83a1e08523649b0e33efdb898db577ef5bb009",
                "sha256:915c04ba3851909ce68ccc2b8e2cd691618c4dc4c4232fb7982bca3f41fd8c3d",
                "sha256:949b8d66bc381ee8b007cd945914c721d9aba8e27f71959d750a46f7c282b20b",
                "sha256:94c6f0bb423f739146aec64595853541634bde58b2135f27f61c1ffd1cd4d16a",
                "sha256:9a1abfdc021a164803f4d485104931fb8f8c1efd55bc6b748d2f5774e78b62c5",
                "sha256:9b79b7a16f7fedff2495d684f2b59b0457c3b493778c9eed31111be64d58279f",
                "sha256:a320721ab5a1aba0a233739394eb907f8c8da5c98c9181d1161e77a0c8e36f2d",
                "sha256:a4afe79fb3de0b7097d81da19090f4df4f8d3a2b3adaa8764138aac2e44f3af1",
                "sha256:ad2cf8aa28b8c020ab2fc8287b0f823d0a7d8630784c31e9ee5edea20f406287",
                "sha256:b8512a91625c9b3da6f127803b166b629725e68af71f8184ae7e7d54686a56d6",
                "sha256:bc51efed119bc9cfdf792cdeaa4d67e8f6fcccab66ed4bfdd6bde3e59bfcbb2f",
                "sha256:bdc919ead48f234740ad807933cdf545180bfbe9342c2bb451556db2ed958581",
                "sha256:bdd37121970bfd8be76c5fb069c7751683bdf373db1ed6c010162b2a130248ed",
                "sha256:be8813b57049a7dc738189df53d69395eba14fb99345e0a5994914a3864c8a4b",
                "sha256:c0c0b3ade1c0b13b936d7970b1d37a57acde9199dc2aecc4c336773e1d86049c",
                "sha256:c47a551199eb8eb2121d4f0f15ae0f923d31350ab9280078d1e5f12b249e0026",
                "sha256:c4ffb7ebf07cfe8931028e3e4c85f0357459a3f9f9490886198848f4fa002ec8",
                "sha256:ccfcd093f13f0f0b7fdd0f198b90053bf7b2f02a3927a30e63f3ccc9df56b676",
                "sha256:d2ee202e79d8ed691ceebae8e0486bd9a2cd4794cec4824e1c99b6f5009502f6",
                "sha256:d53197da72cc091b024dd97249dfc7794d6a56530370992a5e1a08983ad9230e",
                "sha256:d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d",
                "sha256:d88b440e37a16e651bda4c7c2b930eb586fd15ca7406cb39e211fcff3bf3017d",
                "sha256:de8a88e63464af587c950061a5e6a67d3632e36df62b986892331d4620a35c01",
                "sha256:df2449253ef108a379b8b5d6b43f4b1a8e81a061d6537becd5582fba5f9196d7",
                "sha256:e1c1493fb6e50ab01d20a22826e57520f1284df32f2d8601fdd90b6304601419",
                "sha256:e1cf1972137e83c5d4c136c43ced9ac51d0e124706ee1c8aa8532c1287fa8795",
                "sha256:e2103a929dfa2fcaf9bb4e7c091983a49c9ac3b19c9061b6d5427dd7d14d81a1",
                "sha256:e56b7d45a839a697b5eb268c82a71bd8c7f6c94d6fd50c3d577fa39a9f1409f5",
                "sha256:e8afc3f2ccfa24215f8cb28dcf43f0113ac3c37c2f0f0806d8c70e4228c5cf4d",
                "sha256:e8fc20152abba6b83724d7ff268c249fa196d8259ff481f3b1476383f8f24e42",
                "sha256:eaa9599de571d72e2daf60164784109f19978b327a3910d3e9de8c97b5b70cfe",
                "sha256:ec15a59cf5af7be74194f7ab02d0f59a62bdcf1a537677ce67a2537c9b87fcda",
                "sha256:f190daf01f13c72eac4efd5c430a8de82489d9cff23c364c3ea822545032993e",
                "sha256:f34c41761022dd093b4b6896d4810782ffbabe30f2d443ff5f083e0cbbb8c737",
                "sha256:f3e98bb3798ead92273dc0e5fd0f31ade220f59a266ffd8a4f6065e0a3ce0523",
                "sha256:f42d0984e947b8adf7dd6dde396e720934d12c506ce84eea8476409563607591",
                "sha256:f71a396b3bf33ecaa1626c255855702aca4d3d9fea5e051b41ac59a9c1c41edc",
                "sha256:f9e130248f4462aaa8e2552d547f36ddadbeaa573879158d721bbd33dfe4743a",
                "sha256:fed51ac40f757d41b7c48425901843666a6677e3e8eb0abcff09e4ba6e664f50"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==3.0.3"
        },
        "msgpack": {
            "hashes": [
                "sha256:0051fffef5a37ca2cd16978ae4f0aef92f164df86823871b5162812bebecd8e2",
                "sha256:04fb995247a6e83830b62f0b07bf36540c213f6eac8e851166d8d86d83cbd014",
                "sha256:180759d89a057eab503cf62eeec0aa61c4ea1200dee709f3a8e9397dbb3b6931",
                "sha256:1d1418482b1ee984625d88aa9585db570180c286d942da463533b238b98b812b",
                "sha256:1de460f0403172cff81169a30b9a92b260cb809c4cb7e2fc79ae8d0510c78b6b",
                "sha256:1fdf7d83102bf09e7ce3357de96c59b627395352a4024f6e2458501f158bf999",
                "sha256:1fff3d825d7859ac888b0fbda39a42d59193543920eda9d9bea44d958a878029",
                "sha256:283ae72fc89da59aa004ba147e8fc2f766647b1251500182fac0350d8af299c0",
                "sha256:2929af52106ca73fcb28576218476ffbb531a036c2adbcf54a3664de124303e9",
                "sha256:2e86a607e558d22985d856948c12a3fa7b42efad264dca8a3ebbcfa2735d786c",
                "sha256:350ad5353a467d9e3b126d8d1b90fe05ad081e2e1cef5753f8c345217c37e7b8",
                "sha256:354e81bcdebaab427c3df4281187edc765d5d76bfb3a7c125af9da7a27e8458f",
                "sha256:365c0bbe981a27d8932da71af63ef86acc59ed5c01ad929e09a0b88c6294e28a",
                "sha256:372839311ccf6bdaf39b00b61288e0557916c3729529b301c52c2d88842add42",
                "sha256:3b60763c1373dd60f398488069bcdc703cd08a711477b5d480eecc9f9626f47e",
                "sha256:41d1a5d875680166d3ac5c38573896453bbbea7092936d2e107214daf43b1d4f",
                "sha256:42eefe2c3e2af97ed470eec850facbe1b5ad1d6eacdbadc42ec98e7dcf68b4b7",
                "sha256:446abdd8b94b55c800ac34b102dffd2f6aa0ce643c55dfc017ad89347db3dbdb",
                "sha256:454e29e186285d2ebe65be34629fa0e8605202c60fbc7c4c650ccd41870896ef",
                "sha256:4efd7b5979ccb539c221a4c4e16aac1a533efc97f3b759bb5a5ac9f6d10383bf",
                "sha256:5559d03930d3aa0f3aacb4c42c776af1a2ace2611871c84a75afe436695e6245",
                "sha256:5928604de9b032bc17f5099496417f113c45bc6bc21b5c6920caf34b3c428794",
                "sha256:59415c6076b1e30e563eb732e23b994a61c159cec44deaf584e5cc1dd662f2af",
                "sha256:5a46bf7e831d09470ad92dff02b8b1ac92175ca36b087f904a0519857c6be3ff",
                "sha256:602b6740e95ffc55bfb078172d279de3773d7b7db1f703b2f1323566b878b90e",
                "sha256:61c8aa3bd513d87c72ed0b37b53dd5c5a0f58f2ff9f26e1555d3bd7948fb7296",
                "sha256:67016ae8c8965124fdede9d3769528ad8284f14d635337ffa6a713a580f6c030",
                "sha256:6bde749afe671dc44893f8d08e83bf475a1a14570d67c4bb5cec5573463c8833",
                "sha256:6c15b7d74c939ebe620dd8e559384be806204d73b4f9356320632d783d1f7939",
                "sha256:70a0dff9d1f8da25179ffcf880e10cf1aad55fdb63cd59c9a49a1b82290062aa",
                "sha256:70c5a7a9fea7f036b716191c29047374c10721c389c21e9ffafad04df8c52c90",
                "sha256:7bc8813f88417599564fafa59fd6f95be417179f76b40325b500b3c98409757c",
                "sha256:80a0ff7d4abf5fecb995fcf235d4064b9a9a8a40a3ab80999e6ac1e30b702717",
                "sha256:86f8136dfa5c116365a8a651a7d7484b65b13339731dd6faebb9a0242151c406",
                "sha256:897c478140877e5307760b0ea66e0932738879e7aa68144d9b78ea4c8302a84a",
                "sha256:8b696e83c9f1532b4af884045ba7f3aa741a63b2bc22617293a2c6a7c645f251",
                "sha256:8e22ab046fa7ede9e36eeb4cfad44d46450f37bb05d5ec482b02868f451c95e2",
                "sha256:94fd7dc7d8cb0a54432f296f2246bc39474e017204ca6f4ff345941d4ed285a7",
                "sha256:99e2cb7b9031568a2a5c73aa077180f93dd2e95b4f8d3b8e14a73ae94a9e667e",
                "sha256:9ade919fac6a3e7260b7f64cea89df6bec59104987cbea34d34a2fa15d74310b",
                "sha256:9fba231af7a933400238cb357ecccf8ab5d51535ea95d94fc35b7806218ff844",
                "sha256:a465f0dceb8e13a487e54c07d04ae3ba131c7c5b95e2612596eafde1dccf64a9",
                "sha256:a605409040f2da88676e9c9e5853b3449ba8011973616189ea5ee55ddbc5bc87",
                "sha256:a668204fa43e6d02f89dbe79a30b0d67238d9ec4c5bd8a940fc3a004a47b721b",
                "sha256:a7787d353595c7c7e145e2331abf8b7ff1e6673a6b974ded96e6d4ec09f00c8c",
                "sha256:a8f6e7d30253714751aa0b0c84ae28948e852ee7fb0524082e6716769124bc23",
                "sha256:ad09b984828d6b7bb52d1d1d0c9be68ad781fa004ca39216c8a1e63c0f34ba3c",
                "sha256:bafca952dc13907bdfdedfc6a5f579bf4f292bdd506fadb38389afa3ac5b208e",
                "sha256:be52a8fc79e45b0364210eef5234a7cf8d330836d0a64dfbb878efa903d84620",
                "sha256:be5980f3ee0e6bd44f3a9e9dea01054f175b50c3e6cdb692bc9424c0bbb8bf69",
                "sha256:c63eea553c69ab05b6747901b97d620bb2a690633c77f23feb0c6a947a8a7b8f",
                "sha256:d198d275222dc54244bf3327eb8cbe00307d220241d9cec4d306d49a44e85f68",
                "sha256:d62ce1f483f355f61adb5433ebfd8868c5f078d1a52d042b0a998682b4fa8c27",
                "sha256:d99ef64f349d5ec3293688e91486c5fdb925ed03807f64d98d205d2713c60b46",
                "sha256:db6192777d943bdaaafb6ba66d44bf65aa0e9c5616fa1d2da9bb08828c6b39aa",
                "sha256:e23ce8d5f7aa6ea6d2a2b326b4ba46c985dbb204523759984430db7114f8aa00",
                "sha256:e64c8d2f5e5d5fda7b842f55dec6133260ea8f53c4257d64494c534f306bf7a9",
                "sha256:e69b39f8c0aa5ec24b57737ebee40be647035158f14ed4b40e6f150077e21a84",
                "sha256:ea5405c46e690122a76531ab97a079e184c0daf491e588592d6a23d3e32af99e",
                "sha256:f2cb069d8b981abc72b41aea1c580ce92d57c673ec61af4c500153a626cb9e20",
                "sha256:fac4be746328f90caa3cd4bc67e6fe36ca2bf61d5c6eb6d895b6527e3f05071e",
                "sha256:fffee09044073e69f2bad787071aeec727183e7580443dfeb8556cbf1978d162"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.1.2"
        },
        "multidict": {
            "hashes": [
                "sha256:026d264228bcd637d4e060844e39cdc60f86c479e463d49075dedc21b18fbbe0",
                "sha256:03ede2a6ffbe8ef936b92cb4529f27f42be7f56afcdab5ab739cd5f27fb1cbf9",
                "sha256:0458c978acd8e6ea53c81eefaddbbee9c6c5e591f41b3f5e8e194780fe026581",
                "sha256:067343c68cd6612d375710f895337b3a98a033c94f14b9a99eff902f205424e2",
                "sha256:08ccb2a6dc72009093ebe7f3f073e5ec5964cba9a706fa94b1a1484039b87941",
                "sha256:0b38ebffd9be37c1170d33bc0f36f4f262e0a09bc1aac1c34c7aa51a7293f0b3",
                "sha256:0b4c48648d7649c9335cf1927a8b87fa692de3dcb15faa676c6a6f1f1aabda43",
                "sha256:0d17522c37d03e85c8098ec8431636309b2682cf12e58f4dbc76121fb50e4962",
                "sha256:0e161ddf326db5577c3a4cc2d8648f81456e8a20d40415541587a71620d7a7d1",
                "sha256:0e697826df7eb63418ee190fd06ce9f1803593bb4b9517d08c60d9b9a7f69d8f",
                "sha256:10ae39c9cfe6adedcdb764f5e8411d4a92b055e35573a2eaa88d3323289ef93c",
                "sha256:121a34e5bfa410cdf2c8c49716de160de3b1dbcd86b49656f5681e4543bcd1a8",
                "sha256:128441d052254f42989ef98b7b6a6ecb1e6f708aa962c7984235316db59f50fa",
                "sha256:12fad252f8b267cc75b66e8fc51b3079604e8d43a75428ffe193cd9e2195dfd6",
                "sha256:14525a5f61d7d0c94b368a42cff4c9a4e7ba2d52e2672a7b23d84dc86fb02b0c",
                "sha256:17207077e29342fdc2c9a82e4b306f1127bf1ea91f8b71e02d4798a70bb99991",
                "sha256:17307b22c217b4cf05033dabefe68255a534d637c6c9b0cc8382718f87be4262",
                "sha256:1b99af4d9eec0b49927b4402bcbb58dea89d3e0db8806a4086117019939ad3dd",
                "sha256:1d540e51b7e8e170174555edecddbd5538105443754539193e3e1061864d444d",
                "sha256:1e3a8bb24342a8201d178c3b4984c26ba81a577c80d4d525727427460a50c22d",
                "sha256:1fa6609d0364f4f6f58351b4659a1f3e0e898ba2a8c5cac04cb2c7bc556b0bc5",
                "sha256:21f830fe223215dffd51f538e78c172ed7c7f60c9b96a2bf05c4848ad49921c3",
                "sha256:233b398c29d3f1b9676b4b6f75c518a06fcb2ea0b925119fb2c1bc35c05e1601",
                "sha256:24c0cf81544ca5e17cfcb6e482e7a82cd475925242b308b890c9452a074d4505",
                "sha256:25167cc263257660290fba06b9318d2026e3c910be240a146e1f66dd114af2b0",
                "sha256:253282d70d67885a15c8a7716f3a73edf2d635793ceda8173b9ecc21f2fb8292",
                "sha256:273d23f4b40f3dce4d6c8a821c741a86dec62cded82e1175ba3d99be128147ed",
                "sha256:283ddac99f7ac25a4acadbf004cb5ae34480bbeb063520f70ce397b281859362",
                "sha256:28ca5ce2fd9716631133d0e9a9b9a745ad7f60bac2bccafb56aa380fc0b6c511",
                "sha256:2b41f5fed0ed563624f1c17630cb9941cf2309d4df00e494b551b5f3e3d67a23",
                "sha256:2bbd113e0d4af5db41d5ebfe9ccaff89de2120578164f86a5d17d5a576d1e5b2",
                "sha256:2e1425e2f99ec5bd36c15a01b690a1a2456209c5deed58f95469ffb46039ccbb",
                "sha256:2e2d2ed645ea29f31c4c7ea1552fcfd7cb7ba656e1eafd4134a6620c9f5fdd9e",
                "sha256:3758692429e4e32f1ba0df23219cd0b4fc0a52f476726fff9337d1a57676a582",
                "sha256:38fb49540705369bab8484db0689d86c0a33a0a9f2c1b197f506b71b4b6c19b0",
                "sha256:3943debf0fbb57bdde5901695c11094a9a36723e5c03875f87718ee15ca2f4d2",
                "sha256:398c1478926eca669f2fd6a5856b6de9c0acf23a2cb59a14c0ba5844fa38077e",
                "sha256:3ab8b9d8b75aef9df299595d5388b14530839f6422333357af1339443cff777d",
                "sha256:3bd231490fa7217cc832528e1cd8752a96f0125ddd2b5749390f7c3ec8721b65",
                "sha256:3d51ff4785d58d3f6c91bdbffcb5e1f7ddfda557727043aa20d20ec4f65e324a",
                "sha256:3fccb473e87eaa1382689053e4a4618e7ba7b9b9b8d6adf2027ee474597128cd",
                "sha256:401c5a650f3add2472d1d288c26deebc540f99e2fb83e9525007a74cd2116f1d",
                "sha256:41f2952231456154ee479651491e94118229844dd7226541788be783be2b5108",
                "sha256:432feb25a1cb67fe82a9680b4d65fb542e4635cb3166cd9c01560651ad60f177",
                "sha256:439cbebd499f92e9aa6793016a8acaa161dfa749ae86d20960189f5398a19144",
                "sha256:4885cb0e817aef5d00a2e8451d4665c1808378dc27c2705f1bf4ef8505c0d2e5",
                "sha256:497394b3239fc6f0e13a78a3e1b61296e72bf1c5f94b4c4eb80b265c37a131cd",
                "sha256:497bde6223c212ba11d462853cfa4f0ae6ef97465033e7dc9940cdb3ab5b48e5",
                "sha256:4cfb48c6ea66c83bcaaf7e4dfa7ec1b6bbcf751b7db85a328902796dfde4c060",
                "sha256:538cec1e18c067d0e6103aa9a74f9e832904c957adc260e61cd9d8cf0c3b3d37",
                "sha256:55d97cc6dae627efa6a6e548885712d4864b81110ac76fa4e534c03819fa4a56",
                "sha256:563fe25c678aaba333d5399408f5ec3c383ca5b663e7f774dd179a520b8144df",
                "sha256:57b46b24b5d5ebcc978da4ec23a819a9402b4228b8a90d9c656422b4bdd8a963",
                "sha256:5884a04f4ff56c6120f6ccf703bdeb8b5079d808ba604d4d53aec0d55dc33568",
                "sha256:59bc83d3f66b41dac1e7460aac1d196edc70c9ba3094965c467715a70ecb46db",
                "sha256:5a37ca18e360377cfda1d62f5f382ff41f2b8c4ccb329ed974cc2e1643440118",
                "sha256:5c4b9bfc148f5a91be9244d6264c53035c8a0dcd2f51f1c3c6e30e30ebaa1c84",
                "sha256:5e01429a929600e7dab7b166062d9bb54a5eed752384c7384c968c2afab8f50f",
                "sha256:5fa6a95dfee63893d80a34758cd0e0c118a30b8dcb46372bf75106c591b77889",
                "sha256:619e5a1ac57986dbfec9f0b301d865dddf763696435e2962f6d9cf2fdff2bb71",
                "sha256:65573858d27cdeaca41893185677dc82395159aa28875a8867af66532d413a8f",
                "sha256:6704fa2b7453b2fb121740555fa1ee20cd98c4d011120caf4d2b8d4e7c76eec0",
                "sha256:6aac4f16b472d5b7dc6f66a0d49dd57b0e0902090be16594dc9ebfd3d17c47e7",
                "sha256:6b10359683bd8806a200fd2909e7c8ca3a7b24ec1d8132e483d58e791d881048",
                "sha256:6b83cabdc375ffaaa15edd97eb7c0c672ad788e2687004990074d7d6c9b140c8",
                "sha256:6d3bc717b6fe763b8be3f2bee2701d3c8eb1b2a8ae9f60910f1b2860c82b6c49",
                "sha256:6f77ce314a29263e67adadc7e7c1bc699fcb3a305059ab973d038f87caa42ed0",
                "sha256:749aa54f578f2e5f439538706a475aa844bfa8ef75854b1401e6e528e4937cf9",
                "sha256:7a7e590ff876a3eaf1c02a4dfe0724b6e69a9e9de6d8f556816f29c496046e59",
                "sha256:7dfb78d966b2c906ae1d28ccf6e6712a3cd04407ee5088cd276fe8cb42186190",
                "sha256:7eee46ccb30ff48a1e35bb818cc90846c6be2b68240e42a78599166722cea709",
                "sha256:7ff981b266af91d7b4b3793ca3382e53229088d193a85dfad6f5f4c27fc73e5d",
                "sha256:841189848ba629c3552035a6a7f5bf3b02eb304e9fea7492ca220a8eda6b0e5c",
                "sha256:844c5bca0b5444adb44a623fb0a1310c2f4cd41f402126bb269cd44c9b3f3e1e",
                "sha256:84e61e3af5463c19b67ced91f6c634effb89ef8bfc5ca0267f954451ed4bb6a2",
                "sha256:8affcf1c98b82bc901702eb73b6947a1bfa170823c153fe8a47b5f5f02e48e40",
                "sha256:8be1802715a8e892c784c0197c2ace276ea52702a0ede98b6310c8f255a5afb3",
                "sha256:8f333ec9c5eb1b7105e3b84b53141e66ca05a19a605368c55450b6ba208cb9ee",
                "sha256:9004d8386d133b7e6135679424c91b0b854d2d164af6ea3f289f8f2761064609",
                "sha256:90efbcf47dbe33dcf643a1e400d67d59abeac5db07dc3f27d6bdeae497a2198c",
                "sha256:935434b9853c7c112eee7ac891bc4cb86455aa631269ae35442cb316790c1445",
                "sha256:93b1818e4a6e0930454f0f2af7dfce69307ca03cdcfb3739bf4d91241967b6c1",
                "sha256:95922cee9a778659e91db6497596435777bd25ed116701a4c034f8e46544955a",
                "sha256:960c83bf01a95b12b08fd54324a4eb1d5b52c88932b5cba5d6e712bb3ed12eb5",
                "sha256:97231140a50f5d447d3164f994b86a0bed7cd016e2682f8650d6a9158e14fd31",
                "sha256:974e72a2474600827abaeda71af0c53d9ebbc3c2eb7da37b37d7829ae31232d8",
                "sha256:97891f3b1b3ffbded884e2916cacf3c6fc87b66bb0dde46f7357404750559f33",
                "sha256:98655c737850c064a65e006a3df7c997cd3b220be4ec8fe26215760b9697d4d7",
                "sha256:98bc624954ec4d2c7cb074b8eefc2b5d0ce7d482e410df446414355d158fe4ca",
                "sha256:98c5787b0a0d9a41d9311eae44c3b76e6753def8d8870ab501320efe75a6a5f8",
                "sha256:9b0d9b91d1aa44db9c1f1ecd0d9d2ae610b2f4f856448664e01a3b35899f3f92",
                "sha256:9c90fed18bffc0189ba814749fdcc102b536e83a9f738a9003e569acd540a733",
                "sha256:9d624335fd4fa1c08a53f8b4be7676ebde19cd092b3895c421045ca87895b429",
                "sha256:9f9af11306994335398293f9958071019e3ab95e9a707dc1383a35613f6abcb9",
                "sha256:a0543217a6a017692aa6ae5cc39adb75e587af0f3a82288b1492eb73dd6cc2a4",
                "sha256:a088b62bd733e2ad12c50dad01b7d0166c30287c166e137433d3b410add807a6",
                "sha256:a407f13c188f804c759fc6a9f88286a565c242a76b27626594c133b82883b5c2",
                "sha256:a90f75c956e32891a4eda3639ce6dd86e87105271f43d43442a3aedf3cddf172",
                "sha256:a9fc4caa29e2e6ae408d1c450ac8bf19892c5fca83ee634ecd88a53332c59981",
                "sha256:aa23b001d968faef416ff70dc0f1ab045517b9b42a90edd3e9bcdb06479e31d5",
                "sha256:ac1c665bad8b5d762f5f85ebe4d94130c26965f11de70c708c75671297c776de",
                "sha256:af959b9beeb66c822380f222f0e0a1889331597e81f1ded7f374f3ecb0fd6c52",
                "sha256:b0fa96985700739c4c7853a43c0b3e169360d6855780021bfc6d0f1ce7c123e7",
                "sha256:b26684587228afed0d50cf804cc71062cc9c1cdf55051c4c6345d372947b268c",
                "sha256:b4938326284c4f1224178a560987b6cf8b4d38458b113d9b8c1db1a836e640a2",
                "sha256:b8c990b037d2fff2f4e33d3f21b9b531c5745b33a49a7d6dbe7a177266af44f6",
                "sha256:ba0a9fb644d0c1a2194cf7ffb043bd852cea63a57f66fbd33959f7dae18517bf",
                "sha256:bb08271280173720e9fea9ede98e5231defcbad90f1624bea26f32ec8a956e2f",
                "sha256:bdbf9f3b332abd0cdb306e7c2113818ab1e922dc84b8f8fd06ec89ed2a19ab8b",
                "sha256:bfde23ef6ed9db7eaee6c37dcec08524cb43903c60b285b172b6c094711b3961",
                "sha256:c0abd12629b0af3cf590982c0b413b1e7395cd4ec026f30986818ab95bfaa94a",
                "sha256:c102791b1c4f3ab36ce4101154549105a53dc828f016356b3e3bcae2e3a039d3",
                "sha256:c3a32d23520ee37bf327d1e1a656fec76a2edd5c038bf43eddfa0572ec49c60b",
                "sha256:c524c6fb8fc342793708ab111c4dbc90ff9abd568de220432500e47e990c0358",
                "sha256:c5f0c21549ab432b57dcc82130f388d84ad8179824cc3f223d5e7cfbfd4143f6",
                "sha256:c6b3228e1d80af737b72925ce5fb4daf5a335e49cd7ab77ed7b9fdfbf58c526e",
                "sha256:c76c4bec1538375dad9d452d246ca5368ad6e1c9039dadcf007ae59c70619ea1",
                "sha256:c9035dde0f916702850ef66460bc4239d89d08df4d02023a5926e7446724212c",
                "sha256:c93c3db7ea657dd4637d57e74ab73de31bccefe144d3d4ce370052035bc85fb5",
                "sha256:cb2a55f408c3043e42b40cc8eecd575afa27b7e0b956dfb190de0f8499a57a53",
                "sha256:cdea2e7b2456cfb6694fb113066fd0ec7ea4d67e3a35e1f4cbeea0b448bf5872",
                "sha256:ce1bbd7d780bb5a0da032e095c951f7014d6b0a205f8318308140f1a6aba159e",
                "sha256:cf37cbe5ced48d417ba045aca1b21bafca67489452debcde94778a576666a1df",
                "sha256:d4f49cb5661344764e4c7c7973e92a47a59b8fc19b6523649ec9dc4960e58a03",
                "sha256:d54ecf9f301853f2c5e802da559604b3e95bb7a3b01a9c295c6ee591b9882de8",
                "sha256:d62b7f64ffde3b99d06b707a280db04fb3855b55f5a06df387236051d0668f4a",
                "sha256:d82dd730a95e6643802f4454b8fdecdf08667881a9c5670db85bc5a56693f122",
                "sha256:da62917e6076f512daccfbbde27f46fed1c98fee202f0559adec8ee0de67f71a",
                "sha256:dd96c01a9dcd4889dcfcf9eb5544ca0c77603f239e3ffab0524ec17aea9a93ee",
                "sha256:df9f19c28adcb40b6aae30bbaa1478c389efd50c28d541d76760199fc1037c32",
                "sha256:e1c5988359516095535c4301af38d8a8838534158f649c05dd1050222321bcb3",
                "sha256:e628ef0e6859ffd8273c69412a2465c4be4a9517d07261b33334b5ec6f3c7489",
                "sha256:e82d14e3c948952a1a85503817e038cba5905a3352de76b9a465075d072fba23",
                "sha256:e954b24433c768ce78ab7929e84ccf3422e46deb45a4dc9f93438f8217fa2d34",
                "sha256:eb0ce7b2a32d09892b3dd6cc44877a0d02a33241fafca5f25c8b6b62374f8b75",
                "sha256:eb304767bca2bb92fb9c5bd33cedc95baee5bb5f6c88e63706533a1c06ad08c8",
                "sha256:eb351f72c26dc9abe338ca7294661aa22969ad8ffe7ef7d5541d19f368dc854a",
                "sha256:ec6652a1bee61c53a3e5776b6049172c53b6aaba34f18c9ad04f82712bac623d",
                "sha256:f2a0a924d4c2e9afcd7ec64f9de35fcd96915149b2216e1cb2c10a56df483855",
                "sha256:f33dc2a3abe9249ea5d8360f969ec7f4142e7ac45ee7014d8f8d5acddf178b7b",
                "sha256:f537b55778cd3cbee430abe3131255d3a78202e0f9ea7ffc6ada893a4bcaeea4",
                "sha256:f5dd81c45b05518b9aa4da4aa74e1c93d715efa234fd3e8a179df611cc85e5f4",
                "sha256:f99fe611c312b3c1c0ace793f92464d8cd263cc3b26b5721950d977b006b6c4d",
                "sha256:fa263a02f4f2dd2d11a7b1bb4362aa7cb1049f84a9235d31adf63f30143469a0",
                "sha256:fc5907494fccf3e7d3f94f95c91d6336b092b5fc83811720fae5e2765890dfba",
                "sha256:fcee94dfbd638784645b066074b338bc9cc155d4b4bffa4adce1615c5a426c19"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==6.7.1"
        },
        "packaging": {
            "hashes": [
                "sha256:5fc45236b9446107ff2415ce77c807cee2862cb6fac22b8a73826d0693b0980e",
                "sha256:ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==26.2"
        },
        "pluggy": {
            "hashes": [
                "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3",
                "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.6.0"
        },
        "propcache": {
            "hashes": [
                "sha256:01c4fc7480cd0598bb4b57022df55b9ca296da7fc5a8760bd8451a7e63a7d427",
                "sha256:04dc2390d9edbbaef7461f33322555976ffddf0b650a038649d026358714e6c5",
                "sha256:06187263ddad280d05b4d8a8b3bb7d164cbebd469236544a42e6d9b28ac6a4fa",
                "sha256:0958834041a0166d343b8d2cedcd8bcbaeb4fdbe0cf08320c5379f143c3be6e7",
                "sha256:099aaf4b4d1a02265b92a977edf00b5c4f63b3b17ac6de39b0d637c9cac0188a",
                "sha256:0d2c9bf8528f135dbb805ce027567e09164f7efa51a2be07458a2c0420f292d0",
                "sha256:0fd59b5af35f74da48d905dcbad55449ba13be91823cb05a9bd590bbf5b61660",
                "sha256:10734b5484ea113152ee25a91dccedf81631791805d2c9ccb054958e51842c94",
                "sha256:13fef48778b5a2a756523fdb781326b028ca75e32858b04f2cdd19f394564917",
                "sha256:178b4a2cdaac1818e2bf1c5a99b94383fa73ea5382e032a48dec07dc5668dc42",
                "sha256:196913dea116aeb5a2ba95af4ddcb7ea85559ae07d8eee8751688310d09168c3",
                "sha256:1b31822f4474c4036bae62de9402710051d431a606d6a0f907fec79935a071aa",
                "sha256:1ca071adabaab6e9219924bbe00af821f1ee7de113a9eca1cdc292de3d120f4d",
                "sha256:1d1ad32d9d4355e2be65574fd0bfd3677e7066b009cd5b9b2dee8aa6a6393b33",
                "sha256:1dbcf7675229b35d31abb6547d8ebc8c27a830ac3f9a794edff6254873ec7c0a",
                "sha256:2293949b855ce597f2826452d17c2d545fb5622379c4ea6fdf525e9b8e8a2511",
                "sha256:26a4dca084132874e639895c3135dfad5eb20bae209f62d1aeb31b03e601c3c0",
                "sha256:2800a4a8ead6b28cccd1ec54b59346f0def7922ee1c7598e8499c733cfbb7c84",
                "sha256:29cbaac5ea0212663e6845e04b5e188d5a6ae6dd919810ac835bf1d3b42c3f4c",
                "sha256:29f9309a2e42b0d273be006fdb4be2d6c39a47f6f57d8fb1cf9f81481df81b66",
                "sha256:2d7aa89ebca5acc98cba9d1472d976e394782f587bad6661003602a619fd1821",
                "sha256:2f22cbbac9e26a8e864c0985ff1268d5d939d53d9d9411a9824279097e03a2cb",
                "sha256:2f8ea531c794b9d6274acd4e8d2c2ebcac590a4361d27482edd3010b79f1325e",
                "sha256:3115559b8effafd63b142ea5ed53d63a16ea6469cbc63dce4ee194b42db5d853",
                "sha256:32775082acd2d807ee3db715c7770d38767b817870acfa08c29e057f3c4d5b56",
                "sha256:3430bb2bfe1331885c427745a751e774ee679fd4344f80b97bf879815fe8fa55",
                "sha256:3b199b9b2b3d6a7edf3183ba8a9a137a22b97f7df525feb5ae1eccf026d2a9c6",
                "sha256:40314bca9ac559716fe374094fc81c11dcc34b64fd6c585360f5775690505704",
                "sha256:44e488ef40dbb452700b2b1f8188934121f6648f52c295055662d2191959ff82",
                "sha256:452b5065457eb9991ec5eb38ff41d6cd4c991c9ac7c531c4d5849ae473a9a13f",
                "sha256:45f11346f884bc47444f6e6647131055844134c3175b629f84952e2b5cd62b64",
                "sha256:46088abff4cba581dea21ae0467a480526cb25aa5f3c269e909f800328bc3999",
                "sha256:4621064bbf28fa77ff64dd5d94367c04684c67d3a5bf1dff25f0cd0d98a38f3b",
                "sha256:4bc8ff1feffc6a61c7002ffe84634c41b822e104990ae009f44a0834430070bb",
                "sha256:4db0ba63d693afd40d249bd93f842b5f144f8fcbb83de05660373bcf30517b1d",
                "sha256:51f96d685ab16e88cab128cd37a52c5da540809c8b879fa047731bfcb4ad35a4",
                "sha256:54adaa85a22078d1e306304a40984dc5be99d599bf3dc0a24dc98f7daeab89ab",
                "sha256:552ffadf6ad409844bc5919c42a0a83d88314cedddaea0e41e80a8b8fffe881f",
                "sha256:5538d2c13d93e4698af7e092b57bc7298fd35d1d58e656ae18f23ee0d0378e03",
                "sha256:5570dbcc97571c15f68068e529c92715a12f8d54030e272d264b377e22bd17a5",
                "sha256:5671d09a36b06d0fd4a3da0fccbcae360e9b1570924171a15e9e0997f0249fba",
                "sha256:583c19759d9eec1e5b69e2fbef36a7d9c326041be9746cb822d335c8cedc2979",
                "sha256:5aaa2b923c1944ac8febd6609cb373540a5563e7cbcb0fd770f75dace2eb817b",
                "sha256:5dbc581d2814337da56222fab8dc5f161cd798a434e49bac27930aaef798e144",
                "sha256:5fcb98e7598b1ee0addab320d90f65b530297a867dbfe9de52ea838077e16e3d",
                "sha256:6041d31504dc1779d700e1edcfb08eea334b357620b06681a4eabb57a74e574e",
                "sha256:66ea454f095ddf5b6b14f56c064c0941c4788be11e18d2464cf643bf7203ff67",
                "sha256:68ce1c44c7a813a7f71ea04315a8c7b330b63db99d059a797a4651bb6f69f117",
                "sha256:6a997d0489e9668a384fcfd5061b857aa5361de73191cac204d04b889cfbbafa",
                "sha256:6bf3be92233808fcd338eba0fb4d0b59ec5772af4f4ecfcec450d1bfc0f8b5eb",
                "sha256:6de8bd93ddde9b992cf2b2e0d796d501a19026b5b9fd87356d7d0779531a8d96",
                "sha256:6e7b8719005dd1175be4ab1cd25e9b98659a5e0347331506ec6760d2773a7fb5",
                "sha256:6f328175a2cde1f0ff2c4ed8ce968b9dcfb55f3a7153f39e2957ed994da13476",
                "sha256:72d61e16dd78228b58c5d47be830ff3da7e5f139abdf0aef9d86cde1c5cf2191",
                "sha256:74b70780220e2dd89175ca24b81b68b67c83db499ae611e7f2313cb329801c78",
                "sha256:79aa3ff0a9b566633b642fa9caf7e21ed1c13d6feca718187873f199e1514078",
                "sha256:7afa37062e6650640e932e4cc9297d81f9f42d9944029cc386b8247dea4da837",
                "sha256:80168e2ebe4d3ec6599d10ad8f520304ae1cad9b6c5a95372aef1b66b7bfb53a",
                "sha256:806719138ecd720339a12410fb9614ac9b2b2d3a5fdf8235d56981c36f4039ba",
                "sha256:8114f28879e0904748e831c3a7774261bd9e75f49be089f389a76f959dcd13fe",
                "sha256:81e3a30b0bb60caa22033dd0f8a3618d1d67356212514f62c57db75cb0ef410c",
                "sha256:823581fd5cb08b12a48bfa11fe962a7916766b6170c17b028fbdf762b85eb9bf",
                "sha256:85341b12b9d55bad0bded24cac341bb34289469e03a11f3f583ea1cc1db0326c",
                "sha256:857187f381f88c8e2fa2fe56ab94879d011b883d5a2ee5a1b60a8cd2a06846d9",
                "sha256:8a90efd5777e996e42d568db9ac740b944d691e565cbfd31b2f7832f9184b2b8",
                "sha256:8b73ab70f1a3351fbc71f663b3e645af6dd0329100c353081cf69c37433fc6fe",
                "sha256:8c7972d8f193740d9175f0998ab38717e6cd322d5935c5b0fef8c0d323fd9031",
                "sha256:8e778ebd44ef4f66ed60a0416b06b489687db264a9c0b3620362f26489492913",
                "sha256:9282fb1a3bccd038da9f768b927b24a0c753e466c086b7c4f3c6982851eefb2d",
                "sha256:949c91d1a990cf3b2e8188dfcfb25005e0b834a06c63fa4ef9f360878ce21ecf",
                "sha256:95f1e3f4760d404b13c9976c0229b2b49a3c8e2c62a9ce92efdd2b11ada75e3f",
                "sha256:97797ebb098e670a2f92dd66f32897e30d7615b14e7f59711de23e30a9072539",
                "sha256:a0e399a2eccb91ed18721f86aa85757727400b6865c89e88934781deb9c8498b",
                "sha256:a473b3440261e0c60706e732b2ed2f517857344fc21bf48fdfe211e2d98eb285",
                "sha256:a4840ab0ae0216d952f4b53dc6d0b992bfc2bedbfe360bdd9b548bc184c08959",
                "sha256:a592f5f3da71c8691c788c13cb6734b6d17663d2e1cb8caddf0673d01ef8847d",
                "sha256:a6ae2198be502c10f09b2516e7b5d019816924bc3183a43ce792a7bd6625e6f4",
                "sha256:a6ddc6ac9e25de626c1f129c1b467d7ecd33ce2237d3fd0c4e429feef0a7ee1f",
                "sha256:acd2c8edba48e31e58a363b8cf4e5c7db3b04b3f9e371f601df30d9b0d244836",
                "sha256:b05d643f944a8c3c4bd86d65ffd87bf3264b617f87791940302bc474d2ff5274",
                "sha256:b96db7141a592cbc968daf1feea83a118e6ab378af4abbc72b248c895414c22d",
                "sha256:ba338430e87ceb9c8f0cf754de38a9860560261e56c00376debd628698a7364f",
                "sha256:ba57fffe4ac99c5d30076161b5866336d97600769bad35cc68f7774b15298a4e",
                "sha256:be1ddfcbb376e3de5d2e2db1d58d6d67463e6b4f9f040c000de8e300295465fe",
                "sha256:c0cb9ed24c8964e172768d455a38254c2dd8a552905729ce006cad3d3dda59b1",
                "sha256:c60462af8e6dc30c35407c7237ea908d777b22862bbee27bc4699c0d8bcdc45a",
                "sha256:c66afea89b1e43725731d2004732a046fe6fe955d51f952c3e95a7314a284a39",
                "sha256:c6844ba6364fb12f403928a82cfd295ab103a2b315c77c747b2dbe4a41894ea7",
                "sha256:c80f4ba3e8f00189165999a742ee526ebeccedf6c3f7beb0c7df821e9772435a",
                "sha256:cafca7e56c12bb02ae16d283742bef25a61122e9dab2b5b3f2ccbe589ce32164",
                "sha256:cc1177027eda740fdb152706bd215a3f124e3eea15afc39f2cb9fe351b50619e",
                "sha256:cc49723e2f60d6b32a0f0b08a3fd6d13203c07f1cd9566cfce0f12a917c967a2",
                "sha256:cc6fc3cc62e8501d3ed62894425040d2728ecddb1ed072737a5c70bd537aa9f0",
                "sha256:cd416c1de191973c52ff1a12a57446bfc7642797b282d7caf2162d7d1b8aa9a0",
                "sha256:cd645f03898405cabe694fb8bc35241e3a9c332ec85627584fe3de201452b335",
                "sha256:cef6cea3922890dd6c9654971001fa797b526c16ab5e1e46c05fd6f877be7568",
                "sha256:cfa21e036ce1e1db2be04ba3b85d2df1bb1702fa01932d984c5464c665228ff4",
                "sha256:d0326e2e5e1f3163fa306c834e48e8d490e5fae607a097a40c0648109b47ba80",
                "sha256:d310c013aad2c72f1c3f2f8dd3279d460a858c551f97aeb8c63e4693cca7b4d2",
                "sha256:d447bb0b3054be5818458fbb171208b1d9ff11eba14e18ca18b90cbb45767370",
                "sha256:d4dc37dec6c6cdad0b57881a5658fd14fbf53e333b1a86cf86559f190e1d9ec4",
                "sha256:d5a81be28596d6559f6131ef33e10200de6e17643b3c74ce03f9eb103be6ae8b",
                "sha256:d9ee8826a7d47863a08ac44e1a5f611a462eefc3a194b492da242128bec75b42",
                "sha256:db2b80ea58eab4f86b2beec3cc8b39e8ff9276ac20e96b7cce43c8ae84cd6b5a",
                "sha256:decfca4c79dd53ebab484b00cc4b6717d8c369f86e74aa4ca395a64ac651495e",
                "sha256:dfed59d0a5aeb01e242e66ff0300bc4a265a7c05f612d30016f0b60b1017d757",
                "sha256:e00820e192c8dbebcafb383ebbf99030895f09905e7a0eb2e0340a0bcc2bc825",
                "sha256:e4294d04a94dcab1b3bccd8b66d962dcad411a1d19414b2a41d1445f1de32ad0",
                "sha256:e59bc9e66329185b93dab73f210f1a37f81cb40f321501db8017c9aea15dba27",
                "sha256:e5cbfac9f61484f7e9f3597775500cd3ebe8274e9b050c38f9525c77c97520bf",
                "sha256:f064f8d2b59177878b7615df1735cd8fe3462ed6be8c7b217d17a276489c2b7f",
                "sha256:f156a3529f38063b6dbaf356e15602a7f95f8055b1295a438433a6386f10463d",
                "sha256:f19bb891234d72535764d703bfed1153cc34f4214d5bd7150aee1eec9e8f4366",
                "sha256:f7467da8a9822bf1a55336f877340c5bcbd3c482afc43a99771169f74a26dedc",
                "sha256:f78abfa8dfc32376fd1aacf597b2f2fbbe0ea751419aee718af5d4f82537ef8c",
                "sha256:f7eabc04151c78a9f4d5bbb5f1faf571e4defeb4b585e0fe95b60ff2dbe4d3d7",
                "sha256:f814362777a9f841adddb200ecdf8f5cb1e5a3c4b7a86378edbd6ccb26edd702",
                "sha256:fc299c129490f55f254cd90be0deca4764e36e9a7c08b4aa588479a3bbed3098",
                "sha256:fc76378c62a0f04d0cd82fbb1a2cd2d7e28fcb40d5873f28a6c44e388aaa2751",
                "sha256:fc88b26f08d634f7bc819a7852e5214f5802641ab8d9fd5326892292eee1993e",
                "sha256:fe67a3d11cd9b4efabfa45c3d00ffba2b26811442a73a581a94b67c2b5faccf6"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==0.5.2"
        },
        "psutil": {
            "hashes": [
                "sha256:0746f5f8d406af344fd547f1c8daa5f5c33dbc293bb8d6a16d80b4bb88f59372",
                "sha256:076a2d2f923fd4821644f5ba89f059523da90dc9014e85f8e45a5774ca5bc6f9",
                "sha256:11fe5a4f613759764e79c65cf11ebdf26e33d6dd34336f8a337aa2996d71c841",
                "sha256:1a571f2330c966c62aeda00dd24620425d4b0cc86881c89861fbc04549e5dc63",
                "sha256:1a7b04c10f32cc88ab39cbf606e117fd74721c831c98a27dc04578deb0c16979",
                "sha256:1fa4ecf83bcdf6e6c8f4449aff98eefb5d0604bf88cb883d7da3d8d2d909546a",
                "sha256:2edccc433cbfa046b980b0df0171cd25bcaeb3a68fe9022db0979e7aa74a826b",
                "sha256:7b6d09433a10592ce39b13d7be5a54fbac1d1228ed29abc880fb23df7cb694c9",
                "sha256:8c233660f575a5a89e6d4cb65d9f938126312bca76d8fe087b947b3a1aaac9ee",
                "sha256:917e891983ca3c1887b4ef36447b1e0873e70c933afc831c6b6da078ba474312",
                "sha256:ab486563df44c17f5173621c7b198955bd6b613fb87c71c161f827d3fb149a9b",
                "sha256:ae0aefdd8796a7737eccea863f80f81e468a1e4cf14d926bd9b6f5f2d5f90ca9",
                "sha256:b0726cecd84f9474419d67252add4ac0cd9811b04d61123054b9fb6f57df6e9e",
                "sha256:b58fabe35e80b264a4e3bb23e6b96f9e45a3df7fb7eed419ac0e5947c61e47cc",
                "sha256:c7663d4e37f13e884d13994247449e9f8f574bc4655d509c3b95e9ec9e2b9dc1",
                "sha256:e452c464a02e7dc7822a05d25db4cde564444a67e58539a00f929c51eddda0cf",
                "sha256:e78c8603dcd9a04c7364f1a3e670cea95d51ee865e4efb3556a3a63adef958ea",
                "sha256:eb7e81434c8d223ec4a219b5fc1c47d0417b12be7ea866e24fb5ad6e84b3d988",
                "sha256:ed0cace939114f62738d808fdcecd4c869222507e266e574799e9c0faa17d486",
                "sha256:eed63d3b4d62449571547b60578c5b2c4bcccc5387148db46e0c2313dad0ee00",
                "sha256:fd04ef36b4a6d599bbdb225dd1d3f51e00105f6d48a28f006da7f9822f2606d8"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==7.2.2"
        },
        "pycparser": {
            "hashes": [
                "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29",
                "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==3.0"
        },
        "pygments": {
            "hashes": [
                "sha256:6757cd03768053ff99f3039c1a36d6c0aa0b263438fcab17520b30a303a82b5f",
                "sha256:81a9e26dd42fd28a23a2d169d86d7ac03b46e2f8b59ed4698fb4785f946d0176"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==2.20.0"
        },
        "pyjwt": {
            "hashes": [
                "sha256:28ca37c070cad8ba8cd9790cd940535d40274d22f80ab87f3ac6a713e6e8454c",
                "sha256:c74a7a2adf861c04d002db713dd85f84beb242228e671280bf709d765b03672b"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==2.12.1"
        },
        "pytest": {
            "hashes": [
                "sha256:2c5efc453d45394fdd706ade797c0a81091eccd1d6e4bccfcd476e2b8e0ab5d9",
                "sha256:b86ada508af81d19edeb213c681b1d48246c1a91d304c6c81a427674c17eb91c"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==9.0.3"
        },
        "python-engineio": {
            "hashes": [
                "sha256:0a853fcef52f5b345425d8c2b921ac85023a04dfcf75d7b74696c61e940fd066",
                "sha256:f32ad10589859c11053ad7d9bb3c9695cdf862113bfb0d20bc4d890198287399"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==4.13.1"
        },
        "python-socketio": {
            "extras": [
                "client"
            ],
            "hashes": [
                "sha256:a3eb1702e92aa2f2b5d3ba00261b61f062cce51f1cfb6900bf3ab4d1934d2d35",
                "sha256:f863f98eacce81ceea2e742f6388e10ca3cdd0764be21d30d5196470edf5ea89"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==5.16.1"
        },
        "pywin32": {
            "hashes": [
                "sha256:0502d1facf1fed4839a9a51ccbcc63d952cf318f78ffc00a7e78528ac27d7a2b",
                "sha256:184eb5e436dea364dcd3d2316d577d625c0351bf237c4e9a5fabbcfa5a58b151",
                "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87",
                "sha256:3ce80b34b22b17ccbd937a6e78e7225d80c52f5ab9940fe0506a1a16f3dab503",
                "sha256:62ea666235135fee79bb154e695f3ff67370afefd71bd7fea7512fc70ef31e3d",
                "sha256:6c6f2969607b5023b0d9ce2541f8d2cbb01c4f46bc87456017cf63b73f1e2d8c",
                "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d",
                "sha256:750ec6e621af2b948540032557b10a2d43b0cee2ae9758c54154d711cc852d31",
                "sha256:797c2772017851984b97180b0bebe4b620bb86328e8a884bb626156295a63b3b",
                "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a",
                "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42",
                "sha256:a733f1388e1a842abb67ffa8e7aad0e70ac519e09b0f6a784e65a136ec7cefd2",
                "sha256:aba8f82d551a942cb20d4a83413ccbac30790b50efb89a75e4f586ac0bb8056b",
                "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee",
                "sha256:b8c095edad5c211ff31c05223658e71bf7116daa0ecf3ad85f3201ea3190d067",
                "sha256:c8015b09fb9a5e188f83b7b04de91ddca4658cee2ae6f3bc483f0b21a77ef6cd",
                "sha256:d03ff496d2a0cd4a5893504789d4a15399133fe82517455e78bad62efbb7f0a3",
                "sha256:e0c4cfb0621281fe40387df582097fd796e80430597cb9944f0ae70447bacd91",
                "sha256:e286f46a9a39c4a18b319c28f59b61de793654af2f395c102b4f819e584b5852",
                "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d"
            ],
            "markers": "sys_platform == 'win32'",
            "version": "==311"
        },
        "pyzmq": {
            "hashes": [
                "sha256:01c0e07d558b06a60773744ea6251f769cd79a41a97d11b8bf4ab8f034b0424d",
                "sha256:01f9437501886d3a1dd4b02ef59fb8cc384fa718ce066d52f175ee49dd5b7ed8",
                "sha256:03ff0b279b40d687691a6217c12242ee71f0fba28bf8626ff50e3ef0f4410e1e",
                "sha256:05b12f2d32112bf8c95ef2e74ec4f1d4beb01f8b5e703b38537f8849f92cb9ba",
                "sha256:0790a0161c281ca9723f804871b4027f2e8b5a528d357c8952d08cd1a9c15581",
                "sha256:08363b2011dec81c354d694bdecaef4770e0ae96b9afea70b3f47b973655cc05",
                "sha256:08e90bb4b57603b84eab1d0ca05b3bbb10f60c1839dc471fc1c9e1507bef3386",
                "sha256:0c996ded912812a2fcd7ab6574f4ad3edc27cb6510349431e4930d4196ade7db",
                "sha256:0de3028d69d4cdc475bfe47a6128eb38d8bc0e8f4d69646adfbcd840facbac28",
                "sha256:15c8bd0fe0dabf808e2d7a681398c4e5ded70a551ab47482067a572c054c8e2e",
                "sha256:1779be8c549e54a1c38f805e56d2a2e5c009d26de10921d7d51cfd1c8d4632ea",
                "sha256:18339186c0ed0ce5835f2656cdfb32203125917711af64da64dbaa3d949e5a1b",
                "sha256:18770c8d3563715387139060d37859c02ce40718d1faf299abddcdcc6a649066",
                "sha256:190cbf120fbc0fc4957b56866830def56628934a9d112aec0e2507aa6a032b97",
                "sha256:19c9468ae0437f8074af379e986c5d3d7d7bfe033506af442e8c879732bedbe0",
                "sha256:1c179799b118e554b66da67d88ed66cd37a169f1f23b5d9f0a231b4e8d44a113",
                "sha256:1f0b2a577fd770aa6f053211a55d1c47901f4d537389a034c690291485e5fe92",
                "sha256:1f8426a01b1c4098a750973c37131cf585f61c7911d735f729935a0c701b68d3",
                "sha256:226b091818d461a3bef763805e75685e478ac17e9008f49fce2d3e52b3d58b86",
                "sha256:250e5436a4ba13885494412b3da5d518cd0d3a278a1ae640e113c073a5f88edd",
                "sha256:346e9ba4198177a07e7706050f35d733e08c1c1f8ceacd5eb6389d653579ffbc",
                "sha256:3837439b7f99e60312f0c926a6ad437b067356dc2bc2ec96eb395fd0fe804233",
                "sha256:3970778e74cb7f85934d2b926b9900e92bfe597e62267d7499acc39c9c28e345",
                "sha256:43ad9a73e3da1fab5b0e7e13402f0b2fb934ae1c876c51d0afff0e7c052eca31",
                "sha256:448f9cb54eb0cee4732b46584f2710c8bc178b0e5371d9e4fc8125201e413a74",
                "sha256:452631b640340c928fa343801b0d07eb0c3789a5ffa843f6e1a9cee0ba4eb4fc",
                "sha256:49d3980544447f6bd2968b6ac913ab963a49dcaa2d4a2990041f16057b04c429",
                "sha256:4a19387a3dddcc762bfd2f570d14e2395b2c9701329b266f83dd87a2b3cbd381",
                "sha256:4c618fbcd069e3a29dcd221739cacde52edcc681f041907867e0f5cc7e85f172",
                "sha256:50081a4e98472ba9f5a02850014b4c9b629da6710f8f14f3b15897c666a28f1b",
                "sha256:507b6f430bdcf0ee48c0d30e734ea89ce5567fd7b8a0f0044a369c176aa44556",
                "sha256:508e23ec9bc44c0005c4946ea013d9317ae00ac67778bd47519fdf5a0e930ff4",
                "sha256:510869f9df36ab97f89f4cff9d002a89ac554c7ac9cadd87d444aa4cf66abd27",
                "sha256:53b40f8ae006f2734ee7608d59ed661419f087521edbfc2149c3932e9c14808c",
                "sha256:544b4e3b7198dde4a62b8ff6685e9802a9a1ebf47e77478a5eb88eca2a82f2fd",
                "sha256:5bbf8d3630bf96550b3be8e1fc0fea5cbdc8d5466c1192887bd94869da17a63e",
                "sha256:677e744fee605753eac48198b15a2124016c009a11056f93807000ab11ce6526",
                "sha256:6bb54ca21bcfe361e445256c15eedf083f153811c37be87e0514934d6913061e",
                "sha256:6df079c47d5902af6db298ec92151db82ecb557af663098b92f2508c398bb54f",
                "sha256:6f3afa12c392f0a44a2414056d730eebc33ec0926aae92b5ad5cf26ebb6cc128",
                "sha256:7200bb0f03345515df50d99d3db206a0a6bee1955fbb8c453c76f5bf0e08fb96",
                "sha256:722ea791aa233ac0a819fc2c475e1292c76930b31f1d828cb61073e2fe5e208f",
                "sha256:726b6a502f2e34c6d2ada5e702929586d3ac948a4dbbb7fed9854ec8c0466027",
                "sha256:753d56fba8f70962cd8295fb3edb40b9b16deaa882dd2b5a3a2039f9ff7625aa",
                "sha256:75a2f36223f0d535a0c919e23615fc85a1e23b71f40c7eb43d7b1dedb4d8f15f",
                "sha256:7be883ff3d722e6085ee3f4afc057a50f7f2e0c72d289fd54df5706b4e3d3a50",
                "sha256:7ccc0700cfdf7bd487bea8d850ec38f204478681ea02a582a8da8171b7f90a1c",
                "sha256:8085a9fba668216b9b4323be338ee5437a235fe275b9d1610e422ccc279733e2",
                "sha256:80d834abee71f65253c91540445d37c4c561e293ba6e741b992f20a105d69146",
                "sha256:849ca054d81aa1c175c49484afaaa5db0622092b5eccb2055f9f3bb8f703782d",
                "sha256:90e6e9441c946a8b0a667356f7078d96411391a3b8f80980315455574177ec97",
                "sha256:93ad4b0855a664229559e45c8d23797ceac03183c7b6f5b4428152a6b06684a5",
                "sha256:9541c444cfe1b1c0156c5c86ece2bb926c7079a18e7b47b0b1b3b1b875e5d098",
                "sha256:96c71c32fff75957db6ae33cd961439f386505c6e6b377370af9b24a1ef9eafb",
                "sha256:9a916f76c2ab8d045b19f2286851a38e9ac94ea91faf65bd64735924522a8b32",
                "sha256:9c1790386614232e1b3a40a958454bdd42c6d1811837b15ddbb052a032a43f62",
                "sha256:9ce490cf1d2ca2ad84733aa1d69ce6855372cb5ce9223802450c9b2a7cba0ccf",
                "sha256:a1aa0ee920fb3825d6c825ae3f6c508403b905b698b6460408ebd5bb04bbb312",
                "sha256:a5b42d7a0658b515319148875fcb782bbf118dd41c671b62dae33666c2213bda",
                "sha256:ac0765e3d44455adb6ddbf4417dcce460fc40a05978c08efdf2948072f6db540",
                "sha256:ac25465d42f92e990f8d8b0546b01c391ad431c3bf447683fdc40565941d0604",
                "sha256:ad68808a61cbfbbae7ba26d6233f2a4aa3b221de379ce9ee468aa7a83b9c36b0",
                "sha256:add071b2d25f84e8189aaf0882d39a285b42fa3853016ebab234a5e78c7a43db",
                "sha256:b1267823d72d1e40701dcba7edc45fd17f71be1285557b7fe668887150a14b78",
                "sha256:b2e592db3a93128daf567de9650a2f3859017b3f7a66bc4ed6e4779d6034976f",
                "sha256:b721c05d932e5ad9ff9344f708c96b9e1a485418c6618d765fca95d4daacfbef",
                "sha256:bafcb3dd171b4ae9f19ee6380dfc71ce0390fefaf26b504c0e5f628d7c8c54f2",
                "sha256:bd67e7c8f4654bef471c0b1ca6614af0b5202a790723a58b79d9584dc8022a78",
                "sha256:bf7b38f9fd7b81cb6d9391b2946382c8237fd814075c6aa9c3b746d53076023b",
                "sha256:c0bb87227430ee3aefcc0ade2088100e528d5d3298a0a715a64f3d04c60ba02f",
                "sha256:c17e03cbc9312bee223864f1a2b13a99522e0dc9f7c5df0177cd45210ac286e6",
                "sha256:c65047adafe573ff023b3187bb93faa583151627bc9c51fc4fb2c561ed689d39",
                "sha256:c895a6f35476b0c3a54e3eb6ccf41bf3018de937016e6e18748317f25d4e925f",
                "sha256:c9f7f6e13dff2e44a6afeaf2cf54cee5929ad64afaf4d40b50f93c58fc687355",
                "sha256:ce980af330231615756acd5154f29813d553ea555485ae712c491cd483df6b7a",
                "sha256:cedc4c68178e59a4046f97eca31b148ddcf51e88677de1ef4e78cf06c5376c9a",
                "sha256:cf44a7763aea9298c0aa7dbf859f87ed7012de8bda0f3977b6fb1d96745df856",
                "sha256:d54530c8c8b5b8ddb3318f481297441af102517602b569146185fa10b63f4fa9",
                "sha256:da96ecdcf7d3919c3be2de91a8c513c186f6762aa6cf7c01087ed74fad7f0968",
                "sha256:dc5dbf68a7857b59473f7df42650c621d7e8923fb03fa74a526890f4d33cc4d7",
                "sha256:dd2fec2b13137416a1c5648b7009499bcc8fea78154cd888855fa32514f3dad1",
                "sha256:df7cd397ece96cf20a76fae705d40efbab217d217897a5053267cd88a700c266",
                "sha256:e2687c2d230e8d8584fbea433c24382edfeda0c60627aca3446aa5e58d5d1831",
                "sha256:e30a74a39b93e2e1591b58eb1acef4902be27c957a8720b0e368f579b82dc22f",
                "sha256:e343d067f7b151cfe4eb3bb796a7752c9d369eed007b91231e817071d2c2fec7",
                "sha256:e829529fcaa09937189178115c49c504e69289abd39967cd8a4c215761373394",
                "sha256:eca6b47df11a132d1745eb3b5b5e557a7dae2c303277aa0e69c6ba91b8736e07",
                "sha256:f30f395a9e6fbca195400ce833c731e7b64c3919aa481af4d88c3759e0cb7496",
                "sha256:f328d01128373cb6763823b2b4e7f73bdf767834268c565151eacb3b7a392f90",
                "sha256:f605d884e7c8be8fe1aa94e0a783bf3f591b84c24e4bc4f3e7564c82ac25e271",
                "sha256:fbb4f2400bfda24f12f009cba62ad5734148569ff4949b1b6ec3b519444342e6",
                "sha256:ff8d114d14ac671d88c89b9224c63d6c4e5a613fe8acd5594ce53d752a3aafe9"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==27.1.0"
        },
        "requests": {
            "hashes": [
                "sha256:2a0d60c172f83ac6ab31e4554906c0f3b3588d37b5cb939b1c061f4907e278e0",
                "sha256:f288924cae4e29463698d6d60bc6a4da69c89185ad1e0bcc4104f584e960b9ed"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==2.34.2"
        },
        "simple-websocket": {
            "hashes": [
                "sha256:4af6069630a38ed6c561010f0e11a5bc0d4ca569b36306eb257cd9a192497c8c",
                "sha256:7939234e7aa067c534abdab3a9ed933ec9ce4691b0713c78acb195560aa52ae4"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==1.1.0"
        },
        "sqlparse": {
            "hashes": [
                "sha256:12a08b3bf3eec877c519589833aed092e2444e68240a3577e8e26148acc7b1ba",
                "sha256:e20d4a9b0b8585fdf63b10d30066c7c94c5d7a7ec47c889a2d83a3caa93ff28e"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.5.5"
        },
        "tzdata": {
            "hashes": [
                "sha256:9173fde7d80d9018e02a662e168e5a2d04f87c41ea174b139fbef642eda62d10",
                "sha256:bbe9af844f658da81a5f95019480da3a89415801f6cc966806612cc7169bffe7"
            ],
            "markers": "python_version >= '2'",
            "version": "==2026.2"
        },
        "urllib3": {
            "hashes": [
                "sha256:231e0ec3b63ceb14667c67be60f2f2c40a518cb38b03af60abc813da26505f4c",
                "sha256:9fb4c81ebbb1ce9531cce37674bbc6f1360472bc18ca9a553ede278ef7276897"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==2.7.0"
        },
        "websocket-client": {
            "hashes": [
                "sha256:9e813624b6eb619999a97dc7958469217c3176312b3a16a4bd1bc7e08a46ec98",
                "sha256:af248a825037ef591efbf6ed20cc5faa03d3b47b9e5a2230a529eeee1c1fc3ef"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.9.0"
        },
        "werkzeug": {
            "hashes": [
                "sha256:63a77fb8892bf28ebc3178683445222aa500e48ebad5ec77b0ad80f8726b1f50",
                "sha256:9bad61a4268dac112f1c5cd4630a56ede601b6ed420300677a869083d70a4c44"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==3.1.8"
        },
        "wsproto": {
            "hashes": [
                "sha256:61eea322cdf56e8cc904bd3ad7573359a242ba65688716b0710a5eb12beab584",
                "sha256:b86885dcf294e15204919950f666e06ffc6c7c114ca900b060d6e16293528294"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==1.3.2"
        },
        "yarl": {
            "hashes": [
                "sha256:03214408cfa590df47728b84c679ae4ef00be2428e11630277be0727eba2d7cc",
                "sha256:041b1a4cefacf65840b4e295c6985f334ba83c30607441ae3cf206a0eed1a2e4",
                "sha256:0793e2bd0cf14234983bbb371591e6bea9e876ddf6896cdcc93450996b0b5c85",
                "sha256:0e1fdaa14ef51366d7757b45bde294e95f6c8c049194e793eedb8387c86d5993",
                "sha256:0e40111274f340d32ebcc0a5668d54d2b552a6cca84c9475859d364b380e3222",
                "sha256:115136c4a426f9da976187d238e84139ff6b51a20839aa6e3720cd1026d768de",
                "sha256:13a563739ae600a631c36ce096615fe307f131344588b0bc0daec108cdb47b25",
                "sha256:16c6994ac35c3e74fb0ae93323bf8b9c2a9088d55946109489667c510a7d010e",
                "sha256:170e26584b060879e29fac213e4228ef063f39128723807a312e5c7fec28eff2",
                "sha256:17235362f580149742739cc3828b80e24029d08cbb9c4bda0242c7b5bc610a8e",
                "sha256:1932b6b8bba8d0160a9d1078aae5838a66039e8832d41d2992daa9a3a08f7860",
                "sha256:1b6b572edd95b4fa8df75de10b04bc81acc87c1c7d16bcdd2035b09d30acc957",
                "sha256:1c3a3598a832590c5a3ce56ab5576361b5688c12cb1d39429cf5dba30b510760",
                "sha256:1c57676bdedc94cd3bc37724cf6f8cd2779f02f6aba48de45feca073e714fe52",
                "sha256:1dc702e42d0684f42d6519c8d581e49c96cefaaab16691f03566d30658ee8788",
                "sha256:21d1b7305a71a15b4794b5ff22e8eef96ff4a6d7f9657155e5aa419444b28912",
                "sha256:23f371bd662cf44a7630d4d113101eafc0cfa7518a2760d20760b26021454719",
                "sha256:2569b67d616eab450d262ca7cb9f9e19d2f718c70a8b88712859359d0ab17035",
                "sha256:263cd4f47159c09b8b685890af949195b51d1aa82ba451c5847ca9bc6413c220",
                "sha256:2803ed8b21ca47a43da80a6fd1ed3019d30061f7061daa35ac54f63933409412",
                "sha256:2a6940a074fb3c48356ed0158a3ca5699c955ee4185b4d7d619be3c327143e05",
                "sha256:2e27c8841126e017dd2a054a95771569e6070b9ee1b133366d8b31beb5018a41",
                "sha256:31c9921eb8bd12633b41ad27686bbb0b1a2a9b8452bfdf221e34f311e9942ed4",
                "sha256:34b6cf500e61c90f305094911f9acc9c86da1a05a7a3f5be9f68817043f486e4",
                "sha256:3650dc2480f94f7116c364096bc84b1d602f44224ef7d5c7208425915c0475dd",
                "sha256:389871e65468400d6283c0308e791a640b5ab5c83bcee02a2f51295f95e09748",
                "sha256:39004f0ad156da43e86aa71f44e033de68a44e5a31fc53507b36dd253970054a",
                "sha256:394906945aa8b19fc14a61cf69743a868bb8c465efe85eee687109cc540b98f4",
                "sha256:3ceb13c5c858d01321b5d9bb65e4cf37a92169ea470b70fec6f236b2c9dd7e34",
                "sha256:411225bae281f114067578891bc75534cfb3d92a3b4dfef7a6ca78ba354e6069",
                "sha256:44bb7bef4ea409384e3f8bc36c063d77ea1b8d4a5b2706956c0d6695f07dcc25",
                "sha256:4503053d296bc6e4cbd1fad61cf3b6e33b939886c4f249ba7c78b602214fabe2",
                "sha256:4764a6a7588561a9aef92f65bda2c4fb58fe7c675c0883862e6df97559de0bfb",
                "sha256:4966242ec68afc74c122f8459abd597afd7d8a60dc93d695c1334c5fd25f762f",
                "sha256:4a42e651629dafb64fd5b0286a3580613702b5809ad3f24934ea87595804f2c5",
                "sha256:4a59ba56f340334766f3a4442e0efd0af895fae9e2b204741ef885c446b3a1a8",
                "sha256:4c41e021bc6d7affb3364dc1e1e5fa9582b470f283748784bd6ea0558f87f42c",
                "sha256:5023346c4ee7992febc0068e7593de5fa2bf611848c08404b35ebbb76b1b0512",
                "sha256:50f9d8d531dfb767c565f348f33dd5139a6c43f5cbdf3f67da40d54241df93f6",
                "sha256:51430653db848d258336cfa0244427b17d12db63d42603a55f0d4546f50f25b5",
                "sha256:531ef597132086b6cf96faa7c6c1dcd0361dd5f1694e5cc30375907b9b7d3ea9",
                "sha256:53ad387048f6f09a8969631e4de3f1bf70c50e93545d64af4f751b2498755072",
                "sha256:53b1ea6ca88ebd4420379c330aea57e258408dd0df9af0992e5de2078dc9f5d5",
                "sha256:575aa4405a656e61a540f4a80eaa5260f2a38fff7bfdc4b5f611840d76e9e277",
                "sha256:578110dd426f0d209d1509244e6d4a3f1a3e9077655d98c5f22583d63252a08a",
                "sha256:5ec2f42d41ccbd5df0270d7df31618a8ee267bfa50997f5d720ddba86c4a83a6",
                "sha256:5ee586fb17ff8f90c91cf73c6108a434b02d69925f44f5f8e0d7f2f260607eae",
                "sha256:5f10fd85e4b75967468af655228fbfd212bdf66db1c0d135065ce288982eda26",
                "sha256:609d3614d78d74ebe35f54953c5bbd2ac647a7ddb9c30a5d877580f5e86b22f2",
                "sha256:62694e275c93d54f7ccedcfef57d42761b2aad5234b6be1f3e3026cae4001cd4",
                "sha256:63e92247f383c85ab00dd0091e8c3fa331a96e865459f5ee80353c70a4a42d70",
                "sha256:682bae25f0a0dd23a056739f23a134db9f52a63e2afd6bfb37ddc76292bbd723",
                "sha256:6b41389c19b07c760c7e427a3462e8ab83c4bb087d127f0e854c706ce1b9215c",
                "sha256:6e87a6e8735b44816e7db0b2fbc9686932df473c826b0d9743148432e10bb9b9",
                "sha256:6f0fd84de0c957b2d280143522c4f91a73aada1923caee763e24a2b3fda9f8a5",
                "sha256:70efd20be968c76ece7baa8dafe04c5be06abc57f754d6f36f3741f7aa7a208e",
                "sha256:71d006bee8397a4a89f469b8deb22469fe7508132d3c17fa6ed871e79832691c",
                "sha256:73309162a6a571d4cbd3b6a1dcc703c7311843ae0d1578df6f09be4e98df38d4",
                "sha256:75e3026ab649bf48f9a10c0134512638725b521340293f202a69b567518d94e0",
                "sha256:76855800ac56f878847a09ce6dba727c93ca2d89c9e9d63002d26b916810b0a2",
                "sha256:7c6b9461a2a8b47c65eef63bb1c76a4f1c119618ffa99ea79bc5bb1e46c5821b",
                "sha256:803a3c3ce4acc62eaf01eaca1208dcf0783025ef27572c3336502b9c232005e7",
                "sha256:80e6d33a3d42a7549b409f199857b4fb54e2103fc44fb87605b6663b7a7ff750",
                "sha256:8419ebd326430d1cbb7efb5292330a2cf39114e82df5cc3d83c9a0d5ebeaf2f2",
                "sha256:85610b4f27f69984932a7abbe52703688de3724d9f72bceb1cca667deff27474",
                "sha256:85e9beda1f591bc73e77ea1c51965c68e98dafd0fec72cdd745f77d727466716",
                "sha256:877b0738624280e34c55680d6054a307aa94f7d52fa0e3034a9cc6e790871da7",
                "sha256:88f9fb0116fbfcefcab70f85cf4b74a2b6ce5d199c41345296f49d974ddb4123",
                "sha256:8c4fe09e0780c6c3bf2b7d4af02ee2394439d11a523bbcf095cf4747c2932007",
                "sha256:93a784271881035ab4406a172edb0faecb6e7d00f4b53dc2f55919d6c9688595",
                "sha256:94f8575fbdf81749008d980c17796097e645574a3b8c28ee313931068dad14fe",
                "sha256:95451e6ce06c3e104556d73b559f5da6c34a069b6b62946d3ad66afcd51642ea",
                "sha256:99c8a9ed30f4164bc4c14b37a90208836cbf50d4ce2a57c71d0f52c7fb4f7598",
                "sha256:9a18d6f9359e45722c064c97464ec883eb0e0366d33eda61cb19a244bf222679",
                "sha256:9cbf44c5cb4a7633d078788e1b56387e3d3cf2b8139a3be38040b22d6c3221c8",
                "sha256:9ee33b875f0b390564c1fb7bc528abf18c8ee6073b201c6ae8524aca778e2d83",
                "sha256:a0e317df055958a0c1e79e5d2aa5a5eaa4a6d05a20d4b0c9c3f48918139c9fc6",
                "sha256:a2df6afe50dea8ae15fa34c9f824a3ee958d785fd5d089063d960bae1daa0a3f",
                "sha256:a31de1613658308efdb21ada98cbc86a97c181aa050ba22a808120bb5be3ab94",
                "sha256:a3d2bff8f37f8d0f96c7ec554d16945050d54462d6e95414babaa18bfafc7f51",
                "sha256:a41bcf68efd19073376eb8cf948b8d9be0af26256403e512bb18f3966f1f9120",
                "sha256:a82836cab5f197a0514235aaf7ffccdc886ccdaa2324bc0aafdd4ae898103039",
                "sha256:a8d00f29b42f534cc8aa3931cfe773b13b23e561e10d2b26f27a8d309b0e82a1",
                "sha256:aafe5dcfda86c8af00386d7781d4c2181b5011b7be3f2add5e99899ea925df05",
                "sha256:ab5f043cb8a2d71c981c09c510da013bc79fd661f5c60139f00dd3c3cc4f2ffb",
                "sha256:ac09d42f48f80c9ee1635b2fcaa819496a44502737660d3c0f2ade7526d29144",
                "sha256:aecfed0b41aa72b7881712c65cf764e39ce2ec352324f5e0837c7048d9e6daaa",
                "sha256:b2c6b50c7b0464165472b56b42d4c76a7b864597007d9c085e8b63e185cf4a7a",
                "sha256:b35d13d549077713e4414f927cdc388d62e543987c572baee613bf82f11a4b99",
                "sha256:b39cb32a6582750b6cc77bfb3c49c0f8760dc18dc96ec9fb55fbb0f04e08b928",
                "sha256:b5405bb8f0e783a988172993cfc627e4d9d00432d6bbac65a923041edacf997d",
                "sha256:baaf55442359053c7d62f6f8413a62adba3205119bcb6f49594894d8be47e5e3",
                "sha256:bd654fad46d8d9e823afbb4f87c79160b5a374ed1ff5bde24e542e6ba8f41434",
                "sha256:be61f6fff406ca40e3b1d84716fde398fc08bc63dd96d15f3a14230a0973ed86",
                "sha256:bf49a3ae946a87083ef3a34c8f677ae4243f5b824bfc4c69672e72b3d6719d46",
                "sha256:c4a80f77dc1acaaa61f0934176fccca7096d9b1ff08c8ba9cddf5ae034a24319",
                "sha256:c75eb09e8d55bceb4367e83496ff8ef2bc7ea6960efb38e978e8073ea59ecb67",
                "sha256:c7f8dc16c498ff06497c015642333219871effba93e4a2e8604a06264aca5c5c",
                "sha256:c8aa34a5c864db1087d911a0b902d60d203ea3607d91f615acd3f3108ac32169",
                "sha256:cbb0fef01f0c6b38cb0f39b1f78fc90b807e0e3c86a7ff3ce74ad77ce5c7880c",
                "sha256:cde9a2ecd91668bcb7f077c4966d8ceddb60af01b52e6e3e2680e4cf00ad1a59",
                "sha256:cff6d44cb13d39db2663a22b22305d10855efa0fa8015ddeacc40bc59b9d8107",
                "sha256:d1009abedb49ae95b136a8904a3f71b342f849ffeced2d3747bf29caeda218c4",
                "sha256:d38c1e8231722c4ce40d7593f28d92b5fc72f3e9774fe73d7e800ec32299f63a",
                "sha256:d53834e23c015ee83a99377db6e5e37d8484f333edb03bd15b4bc312cc7254fb",
                "sha256:d7504f2b476d21653e4d143f44a175f7f751cd41233525312696c76aa3dbb23f",
                "sha256:dbf507e9ef5688bada447a24d68b4b58dd389ba93b7afc065a2ba892bea54769",
                "sha256:dc52310451fc7c629e13c4e061cbe2dd01684d91f2f8ee2821b083c58bd72432",
                "sha256:dd00607bffbf30250fe108065f07453ec124dbf223420f57f5e749b04295e090",
                "sha256:dda608c88cf709b1d406bdfcd84d8d63cff7c9e577a403c6108ce8ce9dcc8764",
                "sha256:debe9c4f41c32990771be5c22b56f810659f9ddf3d63f67abfdcaa2c6c9c5c1d",
                "sha256:e09fd068c2e169a7070d83d3bde728a4d48de0549f975290be3c108c02e499b4",
                "sha256:e0fd068364a6759bc794459f0a735ab151d11304346332489c7972bacbe9e72b",
                "sha256:e4c53f8347cd4200f0d70a48ad059cabaf24f5adc6ba08622a23423bc7efa10d",
                "sha256:e5723c01a56c5028c807c701aa66722916d2747ad737a046853f6c46f4875543",
                "sha256:e7b0460976dc75cb87ad9cc1f9899a4b97751e7d4e77ab840fc9b6d377b8fd24",
                "sha256:e9d9a4d06d3481eab79803beb4d9bd6f6a8e781ec078ac70d7ef2dcc29d1bea5",
                "sha256:ead11956716a940c1abc816b7df3fa2b84d06eaed8832ca32f5c5e058c65506b",
                "sha256:ed5f69ce7be7902e5c70ea19eb72d20abf7d725ab5d49777d696e32d4fc1811d",
                "sha256:f2af5c81a1f124609d5f33507082fc3f739959d4719b56877ab1ee7e7b3d602b",
                "sha256:f40e782d49630ad384db66d4d8b73ff4f1b8955dc12e26b09a3e3af064b3b9d6",
                "sha256:f514f6474e04179d3d33175ed3f3e31434d3130d42ec153540d5b157deefd735",
                "sha256:f69f57305656a4852f2a7203efc661d8c042e6cc67f7acd97d8667fb448a426e",
                "sha256:fb1e8b8d66c278b21d13b0a7ca22c41dd757a7c209c6b12c313e445c31dd3b28",
                "sha256:fb4948814a2a98e3912505f09c9e7493b1506226afb1f881825368d6fb776ee3",
                "sha256:fda207c815b253e34f7e1909840fd14299567b1c0eb4908f8c2ce01a41265401",
                "sha256:fe8f8f5e70e6dbdfca9882cd9deaac058729bcf323cf7a58660901e55c9c94f6",
                "sha256:fffc45637bcd6538de8b85f51e3df3223e4ad89bccbfca0481c08c7fc8b7ed7d"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==1.23.0"
        },
        "zope.event": {
            "hashes": [
                "sha256:5e755153ac4faf64c10a4b6dd3307680166a3edf65b38df22df592610f8fa874",
                "sha256:b97d5d6327067ee6b9dfcbdf606ade9ade70991e19c162e808ea39e5fcf0f8d3"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==6.2"
        },
        "zope.interface": {
            "hashes": [
                "sha256:049ba3c7b38cc400ae08e011617635706e0f442e1d075db1b015246fcbf6091e",
                "sha256:04c2c9b58e9c177628715d85e94834efa807c1f9f0a2f57ae0f7b553e8266ac4",
                "sha256:0d88c1f106a4f06e074a3ada2d20f4a602e3f2871c4f55726ed5d91e94ec19b1",
                "sha256:265bad2df2ec070f23ff863249a89b408b11908fd4207662781fd18e3c6fc912",
                "sha256:29f09ec8bda65f7b30294328070070a2590b90f252f834ee0817cdb0e2c35f6a",
                "sha256:2bc388cebcb753d21eaf2a0481fd6f0ce6840a47300a40dcec0b56bac27d0f97",
                "sha256:2e9e4aa33b76877af903d5532545e64d24ade0f6f80d9d1a31e6efcea76a60bc",
                "sha256:36c575356732d59ffd3279ad67e302a6fe517e67db5b061b36b377ee0fa016c4",
                "sha256:376d0ef005a131b349e2088e302aa094fa23c826d2ec8a7db4b00fb33c71e0d9",
                "sha256:3e5866917ccb57d929e515a1136d729bd3fa4f367965fb16e38a4bc72cb05521",
                "sha256:415de524326ddd61a78f0816f65942fa1aa35dced19e72579ad30dd106ce523e",
                "sha256:4713bf651ec36e7eea49d2ace4f0e89bec2b33a339674874b1121f2537edc62a",
                "sha256:4ae6a1e111642dbf724f635424dcaf5a5c8abbde49eac3f452f5323ffaa10232",
                "sha256:5ec1a56b6cf9a757cbbce9da38284a01473b92b96c1517eabd99150f51f1bb69",
                "sha256:7cbb887fdbfaacb4c362dbb487033551646e28013ad5ffe72e96eb260003a1a1",
                "sha256:81ed23698bfb588c48b1756129814b890febac971ff6c8a414f82601773145bb",
                "sha256:84064876ed96ddd0744e3ad5d37134c758d77885e54113567792671405a02bac",
                "sha256:8544081e32b515bbaf1c6339eef06b23ed470cf4876ff2f575803f82a744cc43",
                "sha256:892b4b5350e58d6914858f58eb85d39fe9b992640ac6ece695f46c978046554d",
                "sha256:8b302f955c36e924e1f4fe70dd9105ff06235857861c6ae72c3b10b016aeee99",
                "sha256:8b733af6e89a2b0b8edf5ff7a37988fe4e1788806e84e72127b88c47858f0da6",
                "sha256:8d683267a6243526869cb69677dcfc663416d5f87904c1576ddec6e420687d51",
                "sha256:9c4ac009c2c8e43283842f80387c4d4b41bcbc293391c3b9ab71532ae1ccc301",
                "sha256:9dbee7925a23aa6349738892c911019d4095a96cff487b743482073ecbc174a8",
                "sha256:a5638c6be715116d3453e6d099c299c6844d54810de7445ce116424e905ede06",
                "sha256:b8147b40bfcd53803870a9519e0879ff066aeecc2fcff8295663c1b17fc38dc2",
                "sha256:caffd033b27e311b45e15f01923cc9e73c6bfd8e843b4532e29b59ee432bf893",
                "sha256:cd55965d715413038774aead54851bc3dbdd74a69f3ce30252182a94407b9905",
                "sha256:d934497c4b72d5f528d2b5ebe9b8b5a7004b5877948ebd4ea00c2432fb27178f",
                "sha256:e0b9d7e958657fad414f8272afcdf0b8a873fbbb2bb6a6287232d2f11a232bf8",
                "sha256:e195e76767847afb5379ffd67690c17d3c6efdab58dc0e477cf81ac94d5a5a15",
                "sha256:eef0a49e041f4dc4d2a6ab894b4fd0c5354e0e8037e731fb953531e59b0d3d33",
                "sha256:f00fd65343d2a241a2b17688a12f5e815aa704ed64f9ca375de5f9e0ae9c9bda",
                "sha256:f1f854bef8bc137519e4413bcc1322d55faad28b20b3ca39f7bec49d2f1b26df",
                "sha256:fa0a26d5767087170b3da9ff503221d535ea266bf61b522d0afa2590fd05db0a"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==8.4"
        }
    },
    "develop": {}
}

```

---

### <a id="📄-readme-md"></a>📄 `README.md`

**File Info:**
- **Size**: 2.61 KB
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `README.md`
- **Relative Path**: `root`
- **Created**: 2026-05-16 15:04:41 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:02:50 (Asia/Damascus / GMT+03:00)
- **MD5**: `efae6949d3d16e2dd28a784ca8f67d4d`
- **SHA256**: `b52977cc80ecbc0a32d9dc8e13d47a171ebf1d78cb2b3e49fb6e4831a4b87cf7`
- **Encoding**: ASCII

**File code content:**

````markdown
# ParallelProgramming

## E-commerce Load Balancing Lab

This project is a Django REST e-commerce API for a college report on non-functional requirements. The core workflow is database-backed through Django ORM models:

- users register and automatically receive a cart
- cart items are stored in the database
- orders are created from the cart and reduce stock inside a transaction
- payments are stored in the database and mark the order as paid
- JWT logout blacklisting also uses the database-backed Simple JWT blacklist app

There is no Redis backend in the current codebase.

## Docker Stack

- `docker-compose.yml` runs the API directly against PostgreSQL for the no-load-balancer baseline
- `docker-compose.lb.yml` runs three Django app containers behind Nginx with round-robin upstreams
- `docker-compose.least.yml` runs the same stack with Nginx `least_conn` upstreams

Typical local commands:

~~~~bash
docker compose up --build
docker compose -f docker-compose.lb.yml up --build
docker compose -f docker-compose.least.yml up --build
~~~~

## Benchmark Workflow

Use the benchmark seed command first:

~~~~bash
python manage.py migrate
python manage.py seed_benchmark_data
~~~~

That command creates a deterministic benchmark store and product and writes `benchmark_context.json` with the IDs used by the load test.

Run Locust from `benchmark/locustfile.py` with 100 users. The scenario creates a unique customer, registers it, logs in, adds the seeded product to cart, creates an order, and completes payment.

To capture the summary in the plain-text comparison file, use `benchmark/run_benchmark.ps1` and point it at either `http://localhost:8000` for the direct baseline or `http://localhost:8080` for the Nginx stack.

Example:

~~~~powershell
.enchmark
un_benchmark.ps1 -HostUrl http://localhost:8000 -Label "Baseline without load balancer"
.enchmark
un_benchmark.ps1 -HostUrl http://localhost:8080 -Label "Nginx round robin"
~~~~

## Algorithm Choice

Round robin is the baseline Nginx algorithm because the API is stateless at the HTTP layer and the workload is mostly short write requests. Least connections is also included because checkout bursts can create uneven response times when the database is under contention. The benchmark compares both to see which one gives better throughput and tail latency for this specific project.

## Results File

Record the output of the three runs in `benchmark/benchmark_results.txt`:

1. direct app access with PostgreSQL only
2. Nginx round robin
3. Nginx least connections

The file is plain text so it can be pasted directly into the report.

````

---

### <a id="📄-requirements-txt"></a>📄 `requirements.txt`

**File Info:**
- **Size**: 188 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `requirements.txt`
- **Relative Path**: `root`
- **Created**: 2026-05-17 18:58:57 (Asia/Damascus / GMT+03:00)
- **Modified**: 2026-05-17 19:00:32 (Asia/Damascus / GMT+03:00)
- **MD5**: `5396e1f956b64515663dc3bcd53293a3`
- **SHA256**: `3a30057be6e00448970727145c082e9e85c162d22cceeda09e4a5cb215f463ca`
- **Encoding**: ASCII

**File code content:**

```text
Django>=6.0,<7.0
djangorestframework>=3.16,<4.0
djangorestframework-simplejwt>=5.5,<6.0
drf-nested-routers>=0.95,<1.0
gunicorn>=23.0,<24.0
psycopg2-binary>=2.9,<3.0
locust>=2.40,<3.0
```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `db.sqlite3`
- `Dockerfile`
- `Pipfile`

