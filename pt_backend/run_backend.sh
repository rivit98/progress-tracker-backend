#!/bin/bash

source venv/bin/activate
rm -rf ./gunicorn
mkdir -p ./gunicorn
touch ./gunicorn/pid
gunicorn -c gunicorn.config.py --pid ./gunicorn/pid progress_tracker.wsgi
python3.9 manage.py runscheduler &

