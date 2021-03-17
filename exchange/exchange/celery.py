from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

import datetime
import pytz


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exchange.settings")

app = Celery("exchange")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'read_bdm': {
        'task': 'api.tasks.read_bdm',
        'schedule': crontab(hour=12,minute=0),
    },
    'read_dof': {
        'task': 'api.tasks.read_dof',
        'schedule': crontab(hour=0,minute=0),
    },
    'read_fixer': {
        'task': 'api.tasks.read_fixer',
        'schedule': crontab(hour=0,minute=0),
    },

}
