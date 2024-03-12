FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=backend.settings

RUN mkdir /backend
WORKDIR /backend

COPY requirements.txt /backend/
RUN pip install -r requirements.txt

COPY . /backend/