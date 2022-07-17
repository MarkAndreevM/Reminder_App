
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, resolve_url

from .models import * # Импортируем модели 
from . forms import NotificationForm


def home_page(request):

    # Добавление нового уведомления 

    if request.method == 'POST':
        # print('add')
        form = NotificationForm(request.POST)
        # print(request.POST.get('text_reminder'))
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Notification.objects.create(**form.cleaned_data)
                # return HttpResponseRedirect('http://127.0.0.1:8000/')
                return redirect(resolve_url('index'))
            except:
                form.add_error(None, 'Ошибка добавления записи')
                return redirect(resolve_url('index'))     
        else:
            form.add_error(None, 'Ошибка добавления записи')
            return redirect(resolve_url('index'))          
    else:
        form = NotificationForm()

    
        

    notifications = Notification.objects.all()
    return render(request, 'reminder/main.html', {'form': form, 'notifications': notifications})





# Изменение уведомления
def update_reminder(request, id):

    if request.method == 'POST':
        print('kek')
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('index'))





# Удаление записи

def delete_reminder(request, id):
    reminder = Notification.objects.get(pk=id)
    reminder.delete()
    return redirect(resolve_url('index'))








# ============== Обновление уведомления (плохой способ через новую страницу) ========================= #

# def update_reminder(request, pk):


#     get_article = Notification.objects.get(pk=pk)

#     if request.method == 'POST':
#         form = NotificationForm(request.POST, instance = get_article)
#         if form.is_valid():
#             form.save()
#             return redirect(resolve_url('index'))

   
#     context = { 
#         'get_article': get_article,
#         # 'notifications': Notification.objects.all(),
#         'form': NotificationForm( instance = get_article),
        
#     }
#     return render(request, 'reminder/edit.html', context)


