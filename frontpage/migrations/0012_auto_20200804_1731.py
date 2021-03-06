# Generated by Django 3.0.8 on 2020-08-04 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0011_ask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='ask',
            name='username',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='frontpage.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
