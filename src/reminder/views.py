import logging

from datetime import datetime, timedelta

from distutils.log import info
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, resolve_url

from .models import Notification # Импортируем модели 
from . forms import NotificationForm # Импортируем форму

# from .service import send
from .tasks import example_task, send_reminder_on_email


logger = logging.getLogger(__name__)






def home_page(request):
    form = NotificationForm()
    notifications = Notification.objects.all().order_by("-id")
    

    return render(request, 'reminder/main.html', {'form': form, 'notifications': notifications})



# def home_page(request):
#     form = NotificationForm()
#     notifications = Notification.objects.all().order_by("-id")

#     import random
#     reminder_id = random.randint(0, 100)
#     logger.info("set task for %d", reminder_id)
#     logger.error("ALARM: set task for %d", reminder_id)

#     next_time = datetime.utcnow() + timedelta(seconds=10)
#     task_id = example_task.apply_async((reminder_id, ), eta=next_time)

#     logger.info("New task id %s", task_id)


#     return render(request, 'reminder/main.html', {'form': form, 'notifications': notifications})



# Добавление уведомления
def create_reminder(request):

    # tzname = request.session.get('django_timezone')

    form = NotificationForm(request.POST)
    if form.is_valid():
        
        print(form.cleaned_data)
        # try:
        notification = Notification.objects.create(**form.cleaned_data)
        datatime_notification = datetime.combine(notification.date_notification, notification.time_notification)

        task_id = send_reminder_on_email.apply_async((notification.id,), eta=datatime_notification)
        logger.error("New task id %s", task_id)

        return redirect(resolve_url('index'))
        # except:
            # form.add_error(None, 'Ошибка добавления записи')
            # return redirect(resolve_url('index'))
    else:
        form.add_error(None, 'Ошибка добавления записи')
        return redirect(resolve_url('index'))
    



# Изменение уведомления
def update_reminder(request, id):
    get_article = Notification.objects.get(pk=id)
    print('EDIT')

    form = NotificationForm(request.POST, instance=get_article)
    if form.is_valid():
        form.save()
    return redirect(resolve_url('index'))



# Удаление записи

def delete_reminder(request, id):
    reminder = Notification.objects.get(pk=id)
    reminder.delete()
    return redirect(resolve_url('index'))






# Отправка уведомления пользовтелю на почту 

# def send_reminder_on(form):
#     # form.save()
#     # send_reminder_user_on_email.delay(form.instance.email)
#     # return super().form_valid(form)
#     pass



# ЗАПУС 3 терминала 
# 1. Django - python manage.py runserver
# 2. Celery - celery -A project worker -l info     (project - имя проекта основного)
# 3. Celery - celery -A project beat -l info
















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


