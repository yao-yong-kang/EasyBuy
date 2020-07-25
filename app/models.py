from django.db import models
import datetime


# Create your models here.
class User(models.Model):
    loginName = models.CharField(max_length=25, null=False, verbose_name='登录名')
    nickName = models.CharField(max_length=25, null=False, verbose_name='昵称')
    password = models.CharField(max_length=25, null=False, verbose_name='密码')
    sex = models.IntegerField(max_length=1, default=1, verbose_name='性别1为男0为女')
    idcard = models.CharField(max_length=20, default=None, verbose_name='身份证')
    email = models.CharField(max_length=80, default=None, verbose_name='邮箱')
    mobile = models.IntegerField(max_length=11, default=None, verbose_name='手机号')
    time = models.DateTimeField(default=None, verbose_name='登录时间')
    score = models.IntegerField(max_length=11, default=0, verbose_name='积分')  # 100scroe=1￥


class Address(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户外键')
    address = models.CharField(max_length=255, default=None, verbose_name='地址')
    createTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    isDefault = models.IntegerField(max_length=2, default=None, verbose_name='默认地址')


class Category(models.Model):
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(max_length=20, null=False, verbose_name='类别名')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name='自关联')
    # 目录树
    category_type = models.IntegerField(choices=CATEGORY_TYPE)
    iconClass=models.CharField(default=None,verbose_name='图标')


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='名称')
    description = models.CharField(max_length=1024, default=None, verbose_name='描述')
    price = models.FloatField(null=False, verbose_name='价格')
    stock = models.IntegerField(max_length=10, null=False, verbose_name='库存')
    categoryL1Id=models.IntegerField(default=None,verbose_name='分类一')
    categoryL2Id=models.IntegerField(default=None,verbose_name='分类二')
    categoryL3Id=models.IntegerField(default=None,verbose_name='分类三')
    img = models.ImageField(upload_to='product/img/', verbose_name='商品图片')
    isDelete=models.IntegerField(default=0,verbose_name='是否删除1删除0不删除')
    # categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='商品分类')


class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='用户地址')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    createTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    cost = models.FloatField(default=None, verbose_name='总消费')
    number = models.CharField(max_length=255, default=None, verbose_name='订单号')
    quantity = models.IntegerField(max_length=10, null=False, verbose_name='购买数量')


class Car(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    number = models.IntegerField(max_length=20, verbose_name='商品数量')


class UserFav(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品id')
    addTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')
