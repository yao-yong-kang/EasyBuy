# Generated by Django 2.2.3 on 2020-07-30 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200730_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverify',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 10, 41, 20, 91732)),
        ),
    ]
