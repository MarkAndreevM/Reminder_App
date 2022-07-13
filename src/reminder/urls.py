from django.contrib import admin
from django.urls import path
from .views import home_page, update_reminder

urlpatterns = [
    path("", home_page),
    path("update-reminder/<int:pk>", update_reminder, name="update_reminder"),
]