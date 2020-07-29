from django import forms
from user.models import UserProfile
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    ''' 注册验证表单 '''

    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)
    email = forms.EmailField(required=True,label='电话号码',error_messages={"required":"该字段不能为空",'invalid':"格式错误"})
    tel = forms.CharField(required=True)
    #验证码
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})



