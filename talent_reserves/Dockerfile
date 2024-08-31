FROM python:3.11.4-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /app
#ADD entrypoint.sh /app

#RUN chmod +x entrypoint.sh
#ENTRYPOINT ["sh", "entrypoint.sh"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app
