# Generated by Django 2.2.3 on 2020-07-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='img/%Y/%m', verbose_name='头像'),
        ),
    ]
