from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField("Contact name", max_length=50)
    user_mail = models.EmailField("Contact mail", max_length=254)

    def __str__(self):
        return f"User: {self.name}\n{self.user_mail}"


class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    text_reminder = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_notification = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"Notification: {self.text_reminder}"






