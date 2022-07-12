from django.db import models
import datetime


class Notification(models.Model):

    def default_start_time():
        now = datetime.time(hour=8, minute=0)
        return now  

    text_reminder = models.CharField(max_length=255)
    user_mail = models.EmailField(max_length=60, default='SOME STRING')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_notification = models.DateField(auto_now=False)
    time_notification = models.TimeField(default=default_start_time)

    def __str__(self):
        return f"Notification: {self.text_reminder}"






