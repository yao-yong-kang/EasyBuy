# Generated by Django 2.2.5 on 2020-08-04 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='收货人姓名')),
                ('address', models.CharField(max_length=255, verbose_name='地址')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
                ('sign', models.CharField(max_length=50, null=True, verbose_name='标志建筑')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='邮箱')),
                ('code', models.IntegerField(verbose_name='邮政编码')),
                ('isDefault', models.BooleanField(default=False, verbose_name='默认地址')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户外键')),
            ],
            options={
                'verbose_name': '地址',
                'verbose_name_plural': '地址',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('cost', models.FloatField(default='', verbose_name='总消费')),
                ('number', models.CharField(default='', max_length=255, verbose_name='订单号')),
                ('addressId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.Address', verbose_name='用户地址')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Product', verbose_name='商品id')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='购买数量')),
                ('cost', models.FloatField(default='', verbose_name='每类商品的总价格')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.Order', verbose_name='订单id')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Product', verbose_name='商品id')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
    ]
