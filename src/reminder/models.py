from django.db import models
import datetime


class Notification(models.Model):

    def default_start_time():
        now = datetime.time(hour=8, minute=0)
        return now  

    text_reminder = models.CharField(max_length=255)
    user_mail = models.EmailField(max_length=60)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_notification = models.DateField(auto_now=False)
    time_notification = models.CharField(max_length=16, default=default_start_time)

    def __str__(self):
        return f"{self.text_reminder, self.user_mail, self.date_notification, self.time_notification,}"






