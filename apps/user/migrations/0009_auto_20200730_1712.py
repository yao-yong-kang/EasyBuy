# Generated by Django 2.2.3 on 2020-07-30 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200730_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverify',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 17, 12, 24, 81278)),
        ),
    ]
