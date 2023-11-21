FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./talent_reserves .

CMD ["python", "manage.py", "runserver", "0:8000"]