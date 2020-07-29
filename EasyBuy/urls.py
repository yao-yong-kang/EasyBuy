from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usercenter/', include('usercenter.urls', namespace='member')),
    #图片路径
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
]
