
from django import forms
from .models import Notification
import datetime


class NotificationForm(forms.Form):


    text_reminder = forms.CharField(max_length=255, label='Напоминание')
    user_mail  = forms.EmailField(max_length=60)
    date_notification = forms.DateField(label='')
    time_notification  = forms.TimeField(label='')


    text_reminder.widget.attrs.update({'class': 'search-form__field', 'type': 'text', 'name': 'Reminder_text', 'placeholder': 'Введите текст уведомления'})
    user_mail.widget.attrs.update({'class': 'search-form__field', 'type': 'text', 'name': 'User_mail', 'placeholder': 'Введите вашу почту'})
    date_notification.widget.attrs.update({'class': 'redminer_add_date', 'name': 'data', 'type': 'text', 'id': 'datepicker', 'placeholder': 'Set Date   |'})
    time_notification.widget.attrs.update({'class': 'redminer_add_date', 'name': 'time', 'type': 'text', 'id': 'clockpicker', 'placeholder': 'Set Time'})






