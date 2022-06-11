FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# COPY ./run.py /app/run.py
COPY ./app /app/app

EXPOSE 80

ENTRYPOINT [ "gunicorn" ]
CMD [ "-w", "4", "-b", ":80", "app:app" ]