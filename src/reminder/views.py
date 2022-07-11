
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import * # Импортируем модели 
from . forms import NotificationForm


def home_page(request):

    # Добавление нового уведомления 

    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Notification.objects.create(**form.cleaned_data)
                return HttpResponseRedirect('http://127.0.0.1:8000/')
            except:
                form.add_error(None, 'Ошибка добавления записи')            
    else:
        form = NotificationForm()


    # Удаление записи

    if request.method == 'POST':
        print('kek')
        if 'Remove' in request.POST:
            id=request.POST.get('Remove')
            if id:
                remove_add = Notification.objects.get(id=id)
                remove_add.delete()
                return HttpResponseRedirect('http://127.0.0.1:8000/')

                    



    notifications = Notification.objects.all()
    return render(request, 'reminder/main.html', {'form': form, 'notifications': notifications})




