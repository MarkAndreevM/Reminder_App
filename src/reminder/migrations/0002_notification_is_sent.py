# Generated by Django 3.1.14 on 2022-07-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]