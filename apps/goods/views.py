from django.shortcuts import render, HttpResponse, redirect, reverse

from django.views.generic import View
from .models import Category, Product
from car.models import Car
from usercenter.models import UserFav
from user.models import UserProfile
from django.db.models import Q

from datetime import datetime

# Create your views here.

class IndexView(View):
    def get(self, request):
        # 获取cookies
        username = request.COOKIES.get('username')
        if username:
            # 获取用户信息
            user_info = UserProfile.objects.get(username=username)
            # 三级目录
            type1 = Category.objects.filter(category_type=1)
            type2 = Category.objects.filter(category_type=2)
            type3 = Category.objects.filter(category_type=3)
            # 分类商品信息

            # 热门商品
            hosts = Product.objects.values().order_by('-sold')
            host = [i for i in hosts]
            # 进口食品,生鲜
            goods1 = Product.objects.filter(categoryL1Id=660)
            # 保健食品
            goods2 = Product.objects.filter(categoryL1Id=676)
            # 化妆品
            goods3 = Product.objects.filter(categoryL1Id=548)
            # 箱包
            goods4 = Product.objects.filter(categoryL1Id=681)
            # 家用商品
            goods5 = Product.objects.filter(categoryL1Id=628)
            # 电子商品
            goods6 = Product.objects.filter(categoryL1Id=670)
            # 购物车
            carts = Car.objects.filter(userId=user_info.id)
            num = len(carts)
            total = 0
            for i in carts:
                total += i.productId.price * i.number
            return render(request, 'goods/Index.html', {
                'type1': type1,
                'type2': type2,
                'type3': type3,
                'host': host,
                'goods1': goods1,
                'goods2': goods2,
                'goods3': goods3,
                'goods4': goods4,
                'goods5': goods5,
                'goods6': goods6,
                'carts': carts,
                'num': num,
                'total': total,
                'username': username,
            })
        else:
            return redirect(reverse('user:login'))

class logout(View):
    def get(self,request):
        a = redirect(reverse('user:login'))
        a.delete_cookie('username')
        return a


class SearchView(View):
    def get(self,request):
        info = request.GET.get('info')
        # 三级目录
        type1 = Category.objects.filter(category_type=1)
        type2 = Category.objects.filter(category_type=2)
        type3 = Category.objects.filter(category_type=3)
        # 购物车
        carts = Car.objects.all()
        num = len(carts)
        total = 0
        for i in carts:
            total += i.productId.price * i.number
        if info:
            type = request.GET.get('type')
            fil1 = Product.objects.filter(name__contains=info)
            fil2 = Product.objects.filter(name__contains=info).order_by('-sold')
            fil3 = Product.objects.filter(name__contains=info).order_by('-price')
            if fil1 or fil2 or fil3:
                if type == '默认':
                    return render(request, 'goods/Search.html', {'info': info, 'fil1': fil1, 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2, 'type3': type3})
                if type == '销量':
                    return render(request, 'goods/Search.html', {'info': info, 'fil2': fil2, 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2, 'type3': type3})
                if type == '价格':
                    return render(request, 'goods/Search.html', {'info': info, 'fil3': fil3, 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2, 'type3': type3})
            return render(request, 'goods/Search.html', {'info': info, 'fil1': fil1, 'alter': '没有找到相关的商品信息', 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2, 'type3': type3})
        return render(request, 'goods/Search.html', {'alter': '请输入要搜索的内容', 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2, 'type3': type3})
    def post(self,request):
        info = request.POST.get('info')
        # 三级目录
        type1 = Category.objects.filter(category_type=1)
        type2 = Category.objects.filter(category_type=2)
        type3 = Category.objects.filter(category_type=3)
        fil1 = Product.objects.filter(name__contains=info)
        if fil1:
            return render(request, 'goods/Search.html', {'info': info, 'fil1': fil1, 'type1': type1, 'type2': type2, 'type3': type3})
        return render(request, 'goods/Search.html', {'alter': '没有找到相关的商品信息', 'type1': type1, 'type2': type2, 'type3': type3})

class KindView(View):
    def get(self,request):
        kind = request.GET.get('kind')
        # 三级目录
        type1 = Category.objects.filter(category_type=1)
        type2 = Category.objects.filter(category_type=2)
        type3 = Category.objects.filter(category_type=3)
        # 购物车
        carts = Car.objects.all()
        num = len(carts)
        total = 0
        for i in carts:
            total += i.productId.price * i.number
        if kind:
            cate = Category.objects.get(name=kind)
            kind_goods = Product.objects.filter(categoryL3Id=cate.id)
            return render(request, 'goods/kind.html', {'kind': kind, 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2,'type3': type3, 'kind_goods': kind_goods})
        return render(request, 'goods/kind.html', {'kind': kind, 'carts': carts, 'num': num, 'total': total, 'type1': type1, 'type2': type2, 'type3': type3})

class AddsView(View):

    def get(self,request):
        username = request.COOKIES.get('username')
        if username:
            user_info = UserProfile.objects.get(username=username)
            id = request.GET.get('id')
            product = Product.objects.get(id=id)
            if user_info.is_active == 1:
                userfav = UserFav()
                userfav.addTime = datetime.now()
                userfav.productId = id
                userfav.userId = 1
                return render(request, 'goods/Search.html')
            else:
                return render(request, 'goods/Search.html', {'alter': '当前用户未激活'})
        return redirect(reverse('user:login'))

def product_detail(request):
    id = request.GET.get('id')
    if id:
        product = Product.objects.get(id=id)
        if request.method== "POST":
            if request.user.is_active:
                num = request.POST.get('num', 1)
                Car.objects.create(number= num,productId_id= id,userId_id=request.user.id)
                return render(request, "goods/ProductDetail.html", {'product': product,'msg':'加入购物车完成'})
            else:
                return redirect("/")
        return render(request,"goods/ProductDetail.html",{'product' : product})

    return redirect("/")