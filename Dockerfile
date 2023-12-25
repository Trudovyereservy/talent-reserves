FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./talent_reserves .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0:8000"]