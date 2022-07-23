FROM python:3.10

WORKDIR /app

COPY . ./

RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 PIPENV_DONT_LOAD_ENV=1 pipenv install

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:5001"]


