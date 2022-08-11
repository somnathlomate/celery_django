from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import Celery
import os
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "django_celery_project.settings")
# argument to Celery is name of the current module
app = Celery('django_celery_project')
app.conf.enable_utc = False
# Loads configuration from a configuration object
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.TASK_APPS)
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# Celery Beat setting
app.conf.beat_schedule = {
    'send_mail_every_day_at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=19, minute=59, day_of_week=1),
        # 'args': (2,)

    }

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
