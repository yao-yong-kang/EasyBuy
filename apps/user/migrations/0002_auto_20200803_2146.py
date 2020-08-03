# Generated by Django 2.2.3 on 2020-08-03 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='money',
            field=models.FloatField(default=0, verbose_name='余额'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(verbose_name='余额')),
                ('note', models.CharField(max_length=255, verbose_name='备注')),
                ('pay', models.CharField(max_length=255, verbose_name='支付方式')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='创建时间')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
            ],
            options={
                'verbose_name': '充值记录',
                'verbose_name_plural': '充值记录',
            },
        ),
    ]