# Generated by Django 4.0.1 on 2022-08-21 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_mypractice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='is_completed',
        ),
    ]
