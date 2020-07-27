from django.db import models
from user.models import User
from goods.models import Product
import datetime


# Create your models here.
class Address(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户外键')
    address = models.CharField(max_length=255, default=None, verbose_name='地址')
    createTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    isDefault = models.IntegerField(max_length=2, default=None, verbose_name='默认地址')


class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='用户地址')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    createTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    cost = models.FloatField(default=None, verbose_name='总消费')
    number = models.CharField(max_length=255, default=None, verbose_name='订单号')
    quantity = models.IntegerField(max_length=10, null=False, verbose_name='购买数量')


class UserFav(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    addTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')
