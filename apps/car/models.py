from django.db import models
from user.models import User
from goods.models import Product


# Create your models here.
class Car(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    number = models.IntegerField(max_length=20, verbose_name='商品数量')
