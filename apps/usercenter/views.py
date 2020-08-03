from django.shortcuts import render, redirect, reverse
from user.models import UserProfile
from usercenter.models import Address, Order, Order_detail, UserFav
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def memberIndex(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        user = UserProfile.objects.get(id=user.id)
        return render(request, 'usercenter/Member.html', {'user': user})
    else:
        return redirect(reverse('user:login'))


def myOrder(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        orders = Order.objects.filter(userId=user.id)
        del_id = request.GET.get('id')
        if del_id:
            Order.objects.filter(id=del_id).delete()
        return render(request, 'usercenter/Member_Order.html', {'orders': orders})
    else:
        return redirect(reverse('user:login'))


def orderDetail(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        id = request.GET.get('id')
        goods = Order_detail.objects.filter(orderId=id)
        return render(request, 'usercenter/Member_OrderDetail.html', {'goods': goods})
    else:
        return redirect(reverse('user:login'))


def address(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        addr = Address.objects.filter(userId=user.id)
        default = request.GET.get('default')
        del_id = request.GET.get('del')
        if default:
            Address.objects.filter(isDefault=True).update(isDefault=False)
            Address.objects.filter(id=default).update(isDefault=True)
        if del_id:
            Address.objects.filter(id=del_id).delete()
        return render(request, 'usercenter/Member_Address.html', {'addr': addr})
    else:
        return redirect(reverse('user:login'))


def addOrUpdate(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        id = request.GET.get('update')
        if request.method == 'POST' and request.POST.get('ok'):
            name = request.POST.get('name', None)
            email = request.POST.get('email', None)
            addr = request.POST.get('addr', None)
            code = request.POST.get('code', None)
            phone = request.POST.get('phone', None)
            sign = request.POST.get('sign', None)
            if name and email and addr and phone and code:
                if id:
                    if sign:
                        Address.objects.filter(id=id).update(name=name, email=email, address=addr, phone=phone,
                                                             code=code, sign=sign)
                    else:
                        Address.objects.filter(id=id).update(name=name, email=email, address=addr, phone=phone,
                                                             code=code)
                    return redirect(reverse('usercenter:address'))
                else:
                    if sign:
                        Address.objects.create(name=name, email=email, address=addr, phone=phone, code=code,
                                               userId=user, sign=sign)
                    else:
                        Address.objects.create(name=name, email=email, address=addr, phone=phone, userId=user,
                                               code=code)
                    return redirect(reverse('usercenter:address'))
            else:
                return render(request, 'usercenter/Member_AddOrUpdate.html', {'id': id, 'err': '请填写完整'})
        return render(request, 'usercenter/Member_AddOrUpdate.html', {'id': id})
    else:
        return redirect(reverse('user:login'))


def fav(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        fav = UserFav.objects.filter(userId=user.id)
        del_id = request.GET.get('del')
        if del_id:
            UserFav.objects.filter(id=del_id).delete()
        return render(request, 'usercenter/Member_Collect.html', {'fav': fav})
    else:
        return redirect(reverse('user:login'))


def editUser(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        if request.method == 'POST' and request.POST.get('ok'):
            nickname = request.POST.get('nickname', None)
            sex = request.POST.get('sex', None)
            mobile = request.POST.get('mobile', None)
            idcard = request.POST.get('idcard', None)
            photo = request.FILES.get('photo')
            if nickname and sex and mobile and idcard and photo:
                if sex == '男':
                    user.nickName = nickname
                    user.sex = 1
                    user.mobile = mobile
                    user.idcard = idcard
                    user.photo = photo
                    user.save()
                    return redirect(reverse('usercenter:index'))
                elif sex == '女':
                    user.nickName = nickname
                    user.sex = 1
                    user.mobile = mobile
                    user.idcard = idcard
                    user.photo = photo
                    user.save()
                    return redirect(reverse('usercenter:index'))
                else:
                    return render(request, 'usercenter/Member_Edit.html', {'user': user, 'err': '请填写正确的性别'})
            else:
                return render(request, 'usercenter/Member_Edit.html', {'user': user, 'err': '请填写完整'})
        return render(request, 'usercenter/Member_Edit.html', {'user': user})
    else:
        return redirect(reverse('user:login'))


def safe(request):
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    if user:
        if request.method == 'POST' and request.POST.get('ok'):
            old_email = request.POST.get('old_email')
            new_email = request.POST.get('new_email')
            if old_email and new_email:
                if user.email == old_email:
                    if old_email != new_email:
                        user.email = new_email
                        user.save()
                        return redirect(reverse('usercenter:index'))
                    else:
                        return render(request, 'usercenter/Member_Safe.html', {'err': '新邮箱不能与旧邮箱相同'})
                else:
                    return render(request, 'usercenter/Member_Safe.html', {'err': '原邮箱输入错误'})
            else:
                return render(request, 'usercenter/Member_Safe.html', {'err': '请输入完整'})
        elif request.method == 'POST' and request.POST.get('ok1'):
            old_psd = request.POST.get('old_psd')
            psd = request.POST.get('new_psd')
            psd1 = request.POST.get('new_psd1')
            if old_psd and psd and psd1:
                if check_password(old_psd, user.password):
                    if old_psd != psd:
                        if psd == psd1:
                            user.password = make_password(psd)
                            user.save()
                            return redirect(reverse('user:login'))
                        else:
                            return render(request, 'usercenter/Member_Safe.html', {'err': '新密码输入不一致'})
                    else:
                        return render(request, 'usercenter/Member_Safe.html', {'err': '新密码不能与旧密码相同'})
                else:
                    return render(request, 'usercenter/Member_Safe.html', {'err': '旧密码输入错误'})
            else:
                return render(request, 'usercenter/Member_Safe.html', {'err': '请输入完整'})
        return render(request, 'usercenter/Member_Safe.html')
    else:
        return redirect(reverse('user:login'))


def money(request):
    return render(request, 'usercenter/Member_Money.html')
