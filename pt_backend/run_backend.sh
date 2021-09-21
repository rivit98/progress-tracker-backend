source pt-venv/bin/activate
rm -rf ./gunicorn
mkdir -p ./gunicorn
touch ./gunicorn/pid
gunicorn -c gunicorn.config.py --pid ./gunicorn/pid progress_tracker.wsgi
python manage.py runscheduler &

