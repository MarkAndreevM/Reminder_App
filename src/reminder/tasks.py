from time import sleep
from django.core.mail import send_mail
from project.celery import app

from .service import send
from .models import Notification

from datetime import datetime

import time



# Таска на отправку уведомления пользователю

@app.task(bind=True)
def send_reminder_on_email(self, notifications):

    while True:
        for i in notifications:
            if i.date_notification.strftime("%Y-%m-%d") + " " + i.time_notification == datetime.now().strftime("%Y-%m-%d %H:%M"):  # Костыль (нужен) todo: исправить на нормальный вариант
                send_mail(
                    'Уведомление от Reminders',
                    i.text_reminder,
                    'django_app@mail.ru',
                    [i.user_mail],
                    fail_silently=False,
                 )
                
        



@app.task(bind=True)
def example_task(self, reminder_id):
    print(f"I had a work for {reminder_id}")





