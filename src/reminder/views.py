from django.shortcuts import render

from django.views.generic import TemplateView  # класс для отображения странички по шаблону

from .models import *
# Create your views here.


def home_page(request):
    notifications = Notification.objects.all()
    return render(request, 'reminder/main.html', {'notifications': notifications})
