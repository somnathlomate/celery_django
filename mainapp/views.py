from celery.schedules import crontab
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    #print(request.data)
    return HttpResponse("sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=18, minute=30)
    task = PeriodicTask.objects.create(crontab=schedule, name="scheduled_mail_task_" + "126",
                                       task='send_mail_app.tasks.send_mail_func')  # , args=json.dumps(([[2, 3]])))
    return HttpResponse("Done")
