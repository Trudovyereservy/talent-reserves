#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py data_init

export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
python manage.py createsuperuser --no-input

exec "$@"