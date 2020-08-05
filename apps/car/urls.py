
from django.contrib import admin
from django.urls import path
from apps.car import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('car1/',views.car1,name='goodcar1'), #查看购物车
    path('car2/',views.car2,name='goodcar2'), #确认订单
    path('car3/',views.car3,name='goodcar3'), #使用积分
    path('car4/',views.car4,name='goodcar4'), #不使用积分
    path('car5/',views.car5,name='goodcar5'), #余额不足
    path('dele/<id>/',views.dele,name='dele'),
    path('success/',views.success,name='success'),
]
