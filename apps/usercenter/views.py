from django.db.models import Count
from django.shortcuts import render, redirect
from user.models import UserProfile
from usercenter.models import Address, Order, UserFav


# Create your views here.
def memberIndex(request):
    user = UserProfile.objects.get(id=1)
    return render(request, 'usercenter/Member.html', {'user': user})


def myOrder(request):
    orders = Order.objects.all()
    print(orders)
    if request.method == 'POST' and request.POST.get('del'):
        print(1)
    return render(request, 'usercenter/Member_Order.html', {'orders':orders})
