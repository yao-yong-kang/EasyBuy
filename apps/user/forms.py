from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    ''' 注册验证表单 '''
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True,min_length=5,error_messages={'invalid':"密码不能少于5位数"})
    password2 = forms.CharField(required=True,min_length=5,error_messages={'invalid':"两次密码不一样"})
    email = forms.EmailField(required=True,error_messages={'invalid':"邮箱格式错误"})
    tel = forms.CharField(required=True,max_length=11,error_messages={'invalid':"手机号码格式错误"})
    #验证码
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})



