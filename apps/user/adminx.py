import xadmin

from .models import *


class EmailVerifyAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['email']
    list_filter = ['email']


class RecordAdmin(object):
    list_display = ['userId', 'money', 'note', 'pay', 'time']
    search_fields = ['pay']
    list_filter = ['pay']


# 注册
xadmin.site.register(EmailVerify, EmailVerifyAdmin)
xadmin.site.register(Record, RecordAdmin)
