# Generated by Django 2.2.13 on 2020-07-29 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('description', models.CharField(default='', max_length=1024, verbose_name='描述')),
                ('price', models.FloatField(verbose_name='价格')),
                ('stock', models.IntegerField(verbose_name='库存')),
                ('categoryL1Id', models.IntegerField(default='', verbose_name='分类一')),
                ('categoryL2Id', models.IntegerField(default='', verbose_name='分类二')),
                ('categoryL3Id', models.IntegerField(default='', verbose_name='分类三')),
                ('img', models.ImageField(upload_to='product/img/', verbose_name='商品图片')),
                ('isDelete', models.IntegerField(default=0, verbose_name='是否删除1删除0不删除')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类别名')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')])),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Category', verbose_name='自关联')),
            ],
        ),
    ]
