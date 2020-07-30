import xadmin

from .models import *


class EmailVerifyAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['email']
    list_filter = ['email']


# 注册
xadmin.site.register(EmailVerify, EmailVerifyAdmin)
