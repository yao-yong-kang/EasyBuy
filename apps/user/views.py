from django.shortcuts import render
from user.models import User
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password


def register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request,'users/Regist.html',{'register_form':register_form})


    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        print(register_form.data)
        if register_form.is_valid():

            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            tel = register_form.cleaned_data['tel']

            if User.objects.filter(loginName=username,email=email):
                return render(request,'users/Regist.html',{'register_form':register_form,'msg': '用户已存在'})

            else:
                if password1 == password2:
                    pwd = make_password(password1)
                    User.objects.create(loginName=username, password=pwd, email=email, mobile=tel)
                    return render(request, 'users/Login.html')

                return render(request, 'users/Regist.html', {'register_form': register_form})

    return render(request,'users/Regist.html')


def login(request):

    return render(request,'users/Login.html')