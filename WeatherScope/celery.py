# WeatherScope/celery.py
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherScope.settings')
app = Celery('WeatherScope')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Автоматически подхватывает расписание из settings.py
app.conf.beat_schedule = settings.CELERY_BEAT_SCHEDULE