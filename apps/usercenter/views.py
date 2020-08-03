from django.shortcuts import render, redirect, reverse
from user.models import UserProfile
from usercenter.models import Address, Order, Order_detail, UserFav


# Create your views here.
def memberIndex(request):
    user = UserProfile.objects.get(id=1)
    return render(request, 'usercenter/Member.html', {'user': user})


def myOrder(request):
    orders = Order.objects.all()
    del_id = request.GET.get('id')
    if del_id:
        Order.objects.filter(id=del_id).delete()
    return render(request, 'usercenter/Member_Order.html', {'orders': orders})


def orderDetail(request):
    id = request.GET.get('id')
    goods = Order_detail.objects.filter(orderId=id)
    return render(request, 'usercenter/Member_OrderDetail.html', {'goods': goods})


def address(request):
    addr = Address.objects.all()
    default = request.GET.get('default')
    del_id = request.GET.get('del')
    if default:
        Address.objects.filter(isDefault=True).update(isDefault=False)
        Address.objects.filter(id=default).update(isDefault=True)
    if del_id:
        Address.objects.filter(id=del_id).delete()
    return render(request, 'usercenter/Member_Address.html', {'addr': addr})


def addOrUpdate(request):
    id = request.GET.get('update')
    if request.method == 'POST' and request.POST.get('ok'):
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        addr = request.POST.get('addr', None)
        code = request.POST.get('code', None)
        phone = request.POST.get('phone', None)
        sign = request.POST.get('sign', None)
        if name and email and addr and phone:
            if id:
                Address.objects.filter(id=id).update(name=name, email=email, address=addr, phone=phone, code=code,
                                                     sign=sign)
                return redirect(reverse('usercenter:address'))
            # else:
            #     Address.objects.create(name=name, email=email, address=addr, phone=phone, code=code,
            #                                          sign=sign)
            #     return redirect(reverse('usercenter:address'))
        else:
            return render(request, 'usercenter/Member_AddOrUpdate.html', {'id':id, 'err': '请填写完整'})
    return render(request, 'usercenter/Member_AddOrUpdate.html', {'id':id})


def fav(request):
    fav = UserFav.objects.all()
    del_id = request.GET.get('del')
    if del_id:
        UserFav.objects.filter(id=del_id).delete()
    return render(request, 'usercenter/Member_Collect.html', {'fav':fav})


def editUser(request):
    user = UserProfile.objects.get(id=1)
    if request.method == 'POST' and request.POST.get('ok'):
        nickname = request.POST.get('nickname', None)
        sex = request.POST.get('sex', None)
        mobile = request.POST.get('mobile', None)
        idcard = request.POST.get('idcard', None)
        photo = request.FILES.get('photo')
        print(type(photo))
        if nickname and sex and mobile and idcard and photo:
            if sex == '男':
                user.nickName = nickname
                user.sex = 1
                user.mobile = mobile
                user.idcard = idcard
                user.photo = photo
                user.save()
                return redirect('usercenter:index')
            elif sex == '女':
                user.nickName = nickname
                user.sex = 1
                user.mobile = mobile
                user.idcard = idcard
                user.photo = photo
                user.save()
                return redirect('usercenter:index')
            else:
                return render(request, 'usercenter/Member_Edit.html', {'user': user, 'err': '请填写正确的性别'})
        else:
            return render(request, 'usercenter/Member_Edit.html', {'user': user, 'err':'请填写完整'})
    return render(request, 'usercenter/Member_Edit.html', {'user':user})


def safe(request):
    if request.method == 'POST' and request.POST.get('ok'):
        old_email = request.POST.get('old_email')
        new_email = request.POST.get('new_email')
        if old_email and new_email:
            if UserProfile.objects.filter(email=old_email):
                old = UserProfile.objects.filter(email=old_email)
                if old_email != new_email:
                    old.update(email=new_email)
                    return redirect('usercenter:index')
                else:
                    return render(request, 'usercenter/Member_Safe.html', {'err':'请输入新的邮箱'})
            else:
                return render(request, 'usercenter/Member_Safe.html', {'err':'原邮箱输入错误'})
        else:
            return render(request, 'usercenter/Member_Safe.html', {'err':'请输入完整'})
    elif request.method == 'POST' and request.POST.get('ok1'):
        old_psd = request.POST.get('old_psd')
        psd = request.POST.get('new_psd')
        psd1 = request.POST.get('new_psd1')
        if old_psd and psd and psd1:
            pass
    return render(request, 'usercenter/Member_Safe.html')


def money(request):
    return render(request, 'usercenter/Member_Money.html')
