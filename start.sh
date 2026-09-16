#!/usr/bin/env bash
# Start the Celery worker in the background
celery -A config worker -l info &

# Start the Django API via Gunicorn in the foreground
gunicorn config.wsgi:application
