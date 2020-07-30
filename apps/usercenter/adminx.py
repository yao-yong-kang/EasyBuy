import xadmin

from xadmin import views
from .models import *


class BaseSetting(object):
    '''
        xadmin基础配置
    '''
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSetting(object):
    '''
        全局配置，固定写法
    '''
    # 修改title
    site_title = '易买网后台管理页面'
    # 修改footer
    site_footer = 'Group six'
    # 收起菜单
    menu_style = 'accordion'


class AddressAdmin(object):
    # 显示的列
    list_display = ['name', 'address', 'phone', 'sign', 'email', 'code', 'isDefault', 'userId']
    # 搜索的字段
    search_fields = ['name', 'address', 'phone', 'email', 'isDefault']
    # 过滤
    list_filter = ['name', 'address', 'phone', 'email', 'isDefault']


class OrderAdmin(object):
    list_display = ['userId', 'addressId', 'productId', 'createTime', 'cost', 'number', 'quantity']
    search_fields = ['number']
    list_filter = ['number', 'createTime']


class UserFavAdmin(object):
    list_display = ['userId', 'productId', 'addTime']
    search_fields = ['addTime']
    list_filter = ['addTime']


# 注册
xadmin.site.register(Address, AddressAdmin)
xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(UserFav, UserFavAdmin)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSetting)
