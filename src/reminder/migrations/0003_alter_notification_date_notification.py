# Generated by Django 4.0.5 on 2022-07-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date_notification',
            field=models.DateTimeField(),
        ),
    ]
