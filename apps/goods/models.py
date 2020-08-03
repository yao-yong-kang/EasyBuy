from django.db import models


# Create your models here.
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

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='名称')
    description = models.CharField(max_length=1024, default='', verbose_name='描述')
    price = models.FloatField(null=False, verbose_name='价格')
    sold = models.IntegerField(null=False, verbose_name='销量')
    categoryL1Id = models.IntegerField(default='', verbose_name='分类一')
    categoryL2Id = models.IntegerField(default='', verbose_name='分类二')
    categoryL3Id = models.IntegerField(default='', verbose_name='分类三')
    img = models.ImageField(upload_to='product/img/', verbose_name='商品图片')
    isDelete = models.IntegerField(default=0, verbose_name='是否删除1删除0不删除')

    # categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='商品分类')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
