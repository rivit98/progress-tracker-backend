FROM python:3.10

WORKDIR /app

COPY . ./

RUN pip install pipenv
RUN PIPENV_DONT_LOAD_ENV=1 pipenv install --deploy --ignore-pipfile

RUN chmod +x ./run.sh
CMD ./run.sh


