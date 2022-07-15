from django.contrib import admin
from django.urls import path
from .views import home_page, delete_reminder, update_reminder

urlpatterns = [
    path("", home_page, name='index'),
    path('reminder/delete/<int:id>', delete_reminder, name="delete_reminder"),
    path("update-reminder/<int:pk>", update_reminder, name="update_reminder"),
]