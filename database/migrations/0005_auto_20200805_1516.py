# Generated by Django 3.0.8 on 2020-08-05 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_remove_ask_ask_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='files',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ques',
        ),
    ]
