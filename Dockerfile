FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN python3 -m venv /opt/venv

# This is wrong!
RUN . /opt/venv/bin/activate

# Install dependencies:
COPY /app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt





