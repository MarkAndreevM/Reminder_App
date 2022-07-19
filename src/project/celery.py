import os
from celery import Celery
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY') # namespace - переменные, которые начинаются с CELERY читаюстся и подцепляются celery
app.autodiscover_tasks()  # celery ищет задачки эти и автоматически подцепляет 





