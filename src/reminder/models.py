from django.db import models
import datetime

# Create your models here.


# class User(models.Model):
#     name = models.CharField("Contact name", max_length=50)
#     user_mail = models.EmailField("Contact mail", max_length=254)

#     def __str__(self):
#         return f"User: {self.name}\n{self.user_mail}"




class Notification(models.Model):

    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    def default_start_time():
        now = datetime.time(hour=8, minute=0)
        return now  

    text_reminder = models.TextField()
    user_mail = models.EmailField(max_length=60, default='SOME STRING')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_notification = models.DateField(auto_now=False)
    time_notification = models.TimeField(default=default_start_time)

    def __str__(self):
        return f"Notification: {self.text_reminder}"






