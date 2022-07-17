from django.contrib import admin
from django.urls import path
from .views import home_page, delete_reminder, update_reminder

# Обновление уведомления (плохой способ через новую страницу) 
# update_reminder

urlpatterns = [
    path("", home_page, name='index'),
    path("api/reminder/<int:id>", update_reminder, name='update_reminder'),


    path('reminder/delete/<int:id>', delete_reminder, name="delete_reminder"),
    # Обновление уведомления (плохой способ через новую страницу)
    # path("update-reminder/<int:pk>", update_reminder, name="update_reminder"),
]