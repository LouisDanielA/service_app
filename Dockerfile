FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service

WORKDIR /service

EXPOSE 8000

RUN pip install -r /temp/requirements.txt
#RUN django-admin startproject core

RUN adduser --disabled-password service-user

USER service-user