# Generated by Django 2.2.3 on 2020-08-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200803_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
