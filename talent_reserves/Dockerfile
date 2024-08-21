FROM python:3.11.4-slim-buster
WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install --upgrade pip

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "talent_reserves.wsgi"]
