from django.shortcuts import render, redirect
from user.models import UserProfile


# Create your views here.
def memberIndex(request):
    user = UserProfile.objects.get(id=1)
    print(user.photo)
    return render(request, 'usercenter/Member.html', {'user': user})


def myOrder(request):
    return render(request, 'usercenter/Member_Order.html')
