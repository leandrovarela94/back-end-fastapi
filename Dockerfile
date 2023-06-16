FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./Pipfile.lock .
COPY ./Pipfile .

RUN apt-get update && apt-get install -y --no-install-recommends && apt-get install -y python3-pip && pip install --upgrade pip && pip install pipenv && pipenv install --dev

COPY . .
