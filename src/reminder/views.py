from django.shortcuts import render

from .models import * # Импортируем модели 

from .forms import NotificationForm  #импортируем формочку

# Create your views here.


def home_page(request):
    notifications = Notification.objects.all()
    return render(request, 'reminder/main.html', {'notifications': notifications})
