from django.shortcuts import render
from django.db.models import Q
from user.models import UserProfile
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password


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

            password1 = request.POST.get('password', None)
            password2 = request.POST.get('password', None)
            email = request.POST.get('email', None)
            tel = request.POST.get('tel', None)
            if password1 == password2:
                user_profile = UserProfile()
                # 实例化UserProfile对象
                user_profile.username = user_name
                user_profile.email = email
                user_profile.mobile = tel
                user_profile.is_active = False
                user_profile.password = make_password(password1)
                user_profile.save()



            # user_name = request.POST.get('username', None)




            # username = register_form.cleaned_data['username']
            # password1 = register_form.cleaned_data['password1']
            # password2 = register_form.cleaned_data['password2']
            # email = register_form.cleaned_data['email']
            # tel = register_form.cleaned_data['tel']
            # user = authenticate



            # else:
            #     if password1 == password2:
            #         pwd = make_password(password1)
            #         UserProfile.objects.create(username=username, password=pwd, email=email, mobile=tel)
            #         return render(request, 'users/Login.html')
            #
            #     return render(request, 'users/Regist.html', {'register_form': register_form})

        return render(request,'users/Regist.html')


class LoginView(View):
    def get(self,request):

        return render(request,'users/Login.html')