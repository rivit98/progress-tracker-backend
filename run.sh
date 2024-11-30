#!/bin/bash

set -e

python manage.py collectstatic --noinput
python manage.py runscheduler &
gunicorn progress_tracker.wsgi --bind 0.0.0.0:5001 --workers 1 --preload
