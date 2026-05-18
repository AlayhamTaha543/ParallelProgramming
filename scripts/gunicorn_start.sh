#!/usr/bin/env bash
set -e

# Default env vars
: ${GUNICORN_WORKERS:=3}
: ${GUNICORN_THREADS:=2}
: ${GUNICORN_TIMEOUT:=30}

echo "Running migrations (if any)"
python manage.py migrate --noinput || true

echo "Collecting static files"
python manage.py collectstatic --noinput || true

echo "Starting Gunicorn: workers=${GUNICORN_WORKERS}, threads=${GUNICORN_THREADS}"
exec gunicorn ecommerce.wsgi:application \
  --bind 0.0.0.0:${PORT} \
  --workers ${GUNICORN_WORKERS} \
  --threads ${GUNICORN_THREADS} \
  --timeout ${GUNICORN_TIMEOUT} \
  --log-level info \
  --access-logfile '-' \
  --error-logfile '-'
