from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Create your models here.
class UserProfile(AbstractUser):
    nickName = models.CharField(max_length=25, null=True, verbose_name='昵称')
    sex = models.IntegerField(default='未设置', verbose_name='性别1为男0为女')
    idcard = models.CharField(max_length=20, default='未设置', verbose_name='身份证')
    email = models.CharField(max_length=30, unique=True, verbose_name='邮箱')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    time = models.DateTimeField(default='', verbose_name='登录时间')
    score = models.IntegerField(default=0, verbose_name='积分')  # 100scroe=1￥
    money = models.IntegerField(default=0, verbose_name='余额')
    cost = models.IntegerField(default=0, verbose_name='总消费')
    code = models.CharField(max_length=10, verbose_name='邮箱激活码')
    photo = models.ImageField(upload_to='img/%Y/%m', default='default.jpg', verbose_name='头像')
