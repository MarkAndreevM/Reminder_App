from ast import Mod
from .models import Notification
from django.forms import ModelForm, TextInput


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['text_reminder', 'user_mail', 'date_notification', 'time_notification']
            




