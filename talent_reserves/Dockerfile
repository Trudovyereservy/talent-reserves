FROM python:3.11.4-slim-buster
WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install --upgrade pip

ADD . /app
