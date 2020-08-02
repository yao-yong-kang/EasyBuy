from django.db import models
from user.models import UserProfile
from goods.models import Product


# Create your models here.
class Car(models.Model):
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户id')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    number = models.IntegerField(verbose_name='商品数量')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
