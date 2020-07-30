from django.db import models
from user.models import UserProfile
from goods.models import Product
import datetime


# Create your models here.
class Address(models.Model):
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户外键')
    name = models.CharField(max_length=20, null=False, verbose_name='收货人姓名')
    address = models.CharField(max_length=255, null=False, verbose_name='地址')
    phone = models.CharField(max_length=11, null=False, verbose_name='手机')
    sign = models.CharField(max_length=50, null=True, verbose_name='标志建筑')
    email = models.CharField(max_length=50, null=True, verbose_name='邮箱')
    code = models.IntegerField(verbose_name='邮政编码')
    isDefault = models.BooleanField(default=False, verbose_name='默认地址')

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = verbose_name


class Order(models.Model):
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户id')
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='用户地址')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    cost = models.FloatField(default='', verbose_name='总消费')
    number = models.CharField(max_length=255, default='', verbose_name='订单号')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class Order_detail(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    quantity = models.IntegerField(null=False, verbose_name='购买数量')
    cost = models.FloatField(default='', verbose_name='每类商品的总价格')
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单id')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name


class UserFav(models.Model):
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户id')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    addTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name
