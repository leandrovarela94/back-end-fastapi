FROM python:3.10-slim

WORKDIR /app

RUN python3 -m venv /opt/venv

# This is wrong!
RUN . /opt/venv/bin/activate

# Install dependencies:
COPY /app/requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y default-mysql-client
RUN pip install -r requirements.txt

COPY . .

CMD ["python","app.py"]


