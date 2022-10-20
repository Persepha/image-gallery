#!/bin/bash
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm image_gallery.wsgi:application --bind "0.0.0.0:8000"