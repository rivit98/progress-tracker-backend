FROM python:3.10

WORKDIR /app

COPY . ./

RUN pip install pipenv
RUN PIPENV_DONT_LOAD_ENV=1 pipenv install --deploy --ignore-pipfile

CMD pipenv run python manage.py collectstatic --noinput && pipenv run gunicorn progress_tracker.wsgi --bind 0.0.0.0:5001 --workers 3 --preload


