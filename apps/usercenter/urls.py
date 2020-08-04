from django.urls import path
from . import views

app_name = 'usercenter'

urlpatterns = [
    path('index/', views.memberIndex, name='index'),
    path('order/', views.myOrder, name='order'),
    path('orderDetail/', views.orderDetail, name='detail'),
    path('address/', views.address, name='address'),
    path('edit/', views.addOrUpdate, name='edit'),
    path('fav/', views.fav, name='fav'),
    path('editUser/', views.editUser, name='editUser'),
    path('safe/', views.safe, name='safe'),
    path('money/', views.money, name='money'),
    path('recharge/', views.recharge, name='recharge'),
    path('search/', views.search, name='search'),
]
