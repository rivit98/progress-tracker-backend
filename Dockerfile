FROM python:3.10

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:5001"]


