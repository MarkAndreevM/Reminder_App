from time import sleep
from django.core.mail import send_mail
from project.celery import app

from .models import Notification

from datetime import datetime
import logging

import time


logger = logging.getLogger(__name__)



@app.task(bind=True)
def send_reminder_on_email(self, notifications_id):

    notification = Notification.objects.get(pk=notifications_id)
    print(notification)
    logger.info("New supertask id %s", notifications_id)


    send_mail(
        'Уведомление от Reminders',
        notification.text_reminder,
        'django_app1@mail.ru',
        [notification.user_mail],
        fail_silently=False,
        )

    notification.is_sent = True
    notification.save()
    

        






