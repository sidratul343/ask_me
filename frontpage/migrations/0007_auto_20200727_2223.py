# Generated by Django 3.0.8 on 2020-07-27 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0006_auto_20200727_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='background',
            new_name='department',
        ),
    ]
