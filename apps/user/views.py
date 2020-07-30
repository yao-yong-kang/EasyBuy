from django.shortcuts import render
from django.db.models import Q
from user.models import UserProfile,EmailVerify
from django.views.generic.base import View
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from utils.send_email import send_register_email

#注册
class RegisterView(View):
    def get(self,request):
        if request.method == 'GET':
            register_form = RegisterForm()
            return render(request,'users/Regist.html',{'register_form':register_form})


    def post(self,request):
        register_form = RegisterForm(request.POST)
        print(register_form.data)
        if register_form.is_valid():
            user_name = request.POST.get('username', None)
            if UserProfile.objects.filter(username=user_name):
                return render(request,'users/Regist.html',{'register_form':register_form,'msg': '用户已存在'})

            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)
            email = request.POST.get('email', None)
            tel = request.POST.get('tel', None)
            if password1 == password2:
                user_profile = UserProfile()
                # 实例化UserProfile对象
                user_profile.username = user_name
                user_profile.email = email
                user_profile.mobile = int(tel)

                user_profile.is_active=False

                user_profile.password = make_password(password1)
                user_profile.save()
                send_register_email(email)
                return render(request,'users/Login.html')
            else:
                return render(request, 'users/Regist.html', {'register_form': register_form})
        else:
            return render(request, 'users/Regist.html', {'register_form': register_form})

#激活邮箱验证码
class ActiveUserView(View):
    def get(self,request,active_code):
        all = EmailVerify.objects.filter(code = active_code)
        if all:
            for i in all:
                email = i.email
                user = UserProfile.objects.get(email = email)

                user.is_active = True
                user.save()

        else:
            return render(request,'users/active_fail.html')


        return render(request,'users/Login.html')

class LoginView(View):
    def get(self,request):

        return render(request,'users/Login.html')