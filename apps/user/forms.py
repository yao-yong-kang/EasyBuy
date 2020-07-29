from django import forms
from user.models import User
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10,label='用户名',error_messages={"required":"该字段不能为空"})
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)
    tel = forms.CharField(required=True)
    email = forms.EmailField(required=True,label='电话号码',error_messages={"required":"该字段不能为空",'invalid':"格式错误"})
    #验证码
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
