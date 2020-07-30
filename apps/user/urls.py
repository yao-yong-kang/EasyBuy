from django.urls import path
from user.views import RegisterView,LoginView

app_name = 'user'

urlpatterns = [
    #注册
    path('register/',RegisterView.as_view(),name='register'),
    #登录
    path('login/',LoginView.as_view(),name='login')



]