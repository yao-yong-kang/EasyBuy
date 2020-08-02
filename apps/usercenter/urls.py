from django.urls import path
from . import views

app_name = 'usercenter'


urlpatterns = [
    path('index/', views.memberIndex, name='index'),
    path('order/', views.myOrder, name='order'),
]
