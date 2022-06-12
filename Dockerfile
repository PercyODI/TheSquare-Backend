FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./config.py /app/config.py
COPY ./app /app/app

CMD gunicorn -w 4 -b :$PORT "app:create_app()"