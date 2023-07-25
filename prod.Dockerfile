FROM python:3.11

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

RUN chmod +x ./run.sh
CMD ./run.sh


