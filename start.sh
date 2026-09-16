#!/usr/bin/env bash
# Start the Celery worker in the background
celery -A config worker -l info &

# Start the Django API via Gunicorn in the foreground
# Render assigns a PORT env var (default 10000) — must bind to 0.0.0.0
gunicorn config.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
