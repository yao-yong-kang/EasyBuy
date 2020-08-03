from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class UserProfile(AbstractUser):
    nickName = models.CharField(max_length=25, null=True, default='易买网用户', verbose_name='昵称')
    sex = models.IntegerField(default=0, verbose_name='性别1为男0为女')
    idcard = models.CharField(max_length=20, default='未设置', verbose_name='身份证')
    email = models.CharField(max_length=30, unique=True, verbose_name='邮箱')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    time = models.DateTimeField(auto_now_add=True, verbose_name='登录时间')
    score = models.IntegerField(default=0, verbose_name='积分')  # 100scroe=1￥
    money = models.IntegerField(default=0, verbose_name='余额')
    cost = models.IntegerField(default=0, verbose_name='总消费')
    photo = models.ImageField(upload_to='img/%Y/%m', default='default.jpg', verbose_name='头像')


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerify(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(default='注册', max_length=30)
    send_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name




