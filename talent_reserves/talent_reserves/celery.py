import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talent_reserves.settings")

app = Celery("talent_reserves")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
