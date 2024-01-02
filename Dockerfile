FROM python:3.9-alpine3.16

ENV DOCKER_DNS 8.8.8.8

COPY requirements.txt /temp/requirements.txt
COPY service /service

WORKDIR /service

EXPOSE 8000

#RUN apk add postgresql-client build-base postgresql-dev
RUN apk add build-base postgresql-client postgresql-dev


RUN pip install -r /temp/requirements.txt
#RUN django-admin startproject core

RUN adduser --disabled-password service-user

USER service-user