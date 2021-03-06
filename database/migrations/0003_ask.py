# Generated by Django 3.0.8 on 2020-08-04 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20200804_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField(max_length=500)),
                ('image', models.ImageField(max_length=50, upload_to='ques/')),
                ('files', models.FileField(max_length=50, upload_to='files/')),
                ('ask_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.profile')),
            ],
        ),
    ]
