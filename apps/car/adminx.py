import xadmin

from .models import *


class CarAdmin(object):
    # 显示的列
    list_display = ['userId', 'productId', 'number']
    # 搜索的字段
    search_fields = ['userId']
    # 过滤
    list_filter = ['product']


# 注册
xadmin.site.register(Car, CarAdmin)
