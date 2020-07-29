from django.db import models
import datetime


# Create your models here.
class User(models.Model):
    loginName = models.CharField(max_length=25, null=False, verbose_name='登录名')
    nickName = models.CharField(max_length=25, null=True, verbose_name='昵称')
    password = models.CharField(max_length=256, null=False, verbose_name='密码')
    sex = models.IntegerField(max_length=1, default=1, verbose_name='性别1为男0为女')
    idcard = models.CharField(max_length=20, null=True,default='请填写身份证号', verbose_name='身份证')
    email = models.CharField(max_length=80, default='', verbose_name='邮箱')
    mobile = models.BigIntegerField(max_length=11, default=0, verbose_name='手机号')
    time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='登录时间')
    score = models.IntegerField(max_length=11, default=0, verbose_name='积分')  # 100scroe=1￥
