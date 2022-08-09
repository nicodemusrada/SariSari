FROM python:3.9-alpine
MAINTAINER Nicodemus Rada

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd

COPY ./load_db.sh /load_db.sh
RUN chmod u+x /load_db.sh

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user