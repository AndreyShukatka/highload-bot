# Generated by Django 3.1.2 on 2020-11-21 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0027_auto_20201121_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='success_attempts_current_session',
        ),
    ]