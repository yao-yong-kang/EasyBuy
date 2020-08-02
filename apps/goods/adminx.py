import xadmin

from .models import *


class CategoryAdmin(object):
    # 显示的列
    list_display = ['name', 'parent_category', 'category_type']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['name', 'parent_category']


class ProductAdmin(object):
    list_display = ['name', 'description', 'price', 'stock', 'categoryL1Id', 'categoryL2Id', 'categoryL3Id', 'img',
                    'isDelete']
    search_fields = ['name']
    list_filter = ['name']


# 注册
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Product, ProductAdmin)
