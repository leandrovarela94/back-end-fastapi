FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update -y && apt-get install curl -y \
    && export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags` \
    && export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs` \
    && pip install mysqlclient -y \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry install \
    && apt-get remove curl -y 

COPY . .
WORKDIR /app
