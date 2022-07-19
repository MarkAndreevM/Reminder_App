from django.core.mail import send_mail



def send(user_email):
    send_mail(
        'Вам пришло уведомление с Reminder',
        'django_app@mail.ru',
        [user_email],
        fail_silently=False, 
    )



