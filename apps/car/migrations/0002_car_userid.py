# Generated by Django 2.2.5 on 2020-08-03 17:36
# Generated by Django 2.2.3 on 2020-08-03 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id'),
        ),
    ]
