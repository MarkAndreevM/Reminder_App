from django.core.mail import send_mail
from project.celery import app

from .service import send
from .models import Notification

@app.task
def send_reminder_user_on_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for i in Notification.objects.all():
        send_mail(
            'Уведомление от Reminders',
            'django_app@mail.ru',
            [i.user_mail],
            fail_silently=False,

        )


