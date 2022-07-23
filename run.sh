#!/bin/bash

pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py runscheduler &
pipenv run gunicorn progress_tracker.wsgi --bind 0.0.0.0:5001 --workers 3 --preload
