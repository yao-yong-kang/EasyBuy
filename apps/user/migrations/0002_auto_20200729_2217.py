# Generated by Django 2.2.13 on 2020-07-29 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverify',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 22, 17, 45, 539295)),
        ),
    ]