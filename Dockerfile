FROM python:alpine

COPY requirements.txt /app/requirements.txt
COPY project /project

WORKDIR /project

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /app/requirements.txt