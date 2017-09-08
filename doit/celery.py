# Future
from __future__ import absolute_import

# Standart Library
import os

# Celery
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doit.settings')

app = Celery('doit')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
