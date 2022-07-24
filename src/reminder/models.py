from operator import mod
from django.db import models
import datetime
from django import forms
from pytz import timezone, utc


class Notification(models.Model):

    def default_start_time():
        now = datetime.time(hour=8, minute=0)
        return now  

    text_reminder = models.CharField(max_length=255)
    user_mail = models.EmailField(max_length=60)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_notification = models.DateField(auto_now=False)
    time_notification = models.TimeField(max_length=16, default=default_start_time)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text_reminder, self.user_mail, self.date_notification, self.time_notification,}"






