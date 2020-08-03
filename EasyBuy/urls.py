
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from django.views.static import serve
from .settings import MEDIA_ROOT
from user.views import ActiveUserView

import xadmin


urlpatterns = [

    path('xadmin/', xadmin.site.urls),
    path('captcha/', include('captcha.urls')),  # 生成验证码图片功能
    path('user/',include('user.urls', namespace='user')),  # 用户
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='active'),  # 邮箱激活的路由
    path('usercenter/', include('usercenter.urls', namespace='member')),
    path('', include('goods.urls')),

    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),  # 图片路径


]
