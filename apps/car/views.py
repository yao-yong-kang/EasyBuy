from django.shortcuts import render, redirect, HttpResponse
import datetime, random
from car.models import *
from user.models import *
from usercenter.models import *
from goods.models import *


# Create your views here.

def index(request):
    return render(request, 'goods/Index.html')


def car1(request):
    username = request.COOKIES.get('username')
    print(username)
    if username:
        product_list = Car.objects.all()  # 购物车的所有信息
        count = Car.objects.all().count()  # 购物车的所有信息
        return render(request, 'goods_car/BuyCar.html',
                      {'product_list': product_list, "count": count, 'username': username})
    else:
        return redirect('user:login')


def dele(request, id):
    product = Car.objects.get(id=id).delete()  # 删除购物车信息
    return redirect('goodcar1')


list = []  # 总消费


def car2(request):
    product_list = Car.objects.all()  # 购物车所有商品
    count = Car.objects.all().count()  # 购物车所有商品
    user = UserProfile.objects.get(id=1)  # 获取当前用户
    add = Address.objects.filter(isDefault='1', id=user.id)  # 获取当前用户的默认地址
    total = 0  # 消费
    try:
        add = Address.objects.get(isDefault=1)  # 默认地址
    except:
        add = ""
    if add:
        for i in product_list:
            total = total + i.productId.price * i.number  # 累加消费
        print(total)
        list.append(total)
        if request.method == 'POST':
            if request.POST.get('city'):  # 使用积分
                city=request.POST.get('city')
                print('city是',city)
                if user.money-list[-1]<0:  # 余额不知时
                    return redirect('goodcar5')
                else:
                    return redirect('goodcar3')  # 使用积分
            else:
                if user.money-list[-1]<0:  # 余额不知时
                    return redirect('goodcar5')
                else:  # 不使用积分
                    return redirect('goodcar4')
        return render(request, 'goods_car/BuyCar_Two.html',
                      {'product_list': product_list, 'total': total, "user": user, 'add': add,"count":count})
    else:
        return render(request, 'goods_car/BuyCar_Two.html',
                      {'total': list[-1], "msg": "您还没有收货地址",'product_list': product_list, "user": user, 'add': add,"count":count})

def car3(request):
    username=request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    # user.id#当前用户id
    if user.money-list[-1]<0:  # 余额不知时
        return redirect('goodcar5')
    else:
        money = list[-1] - user.score / 100  # 使用积分后的总价格
        list.append(money)
        money1 = user.money - money
        print('我适应积分用户的积分是',)
        UserProfile.objects.filter(id=1).update(cost=user.cost + money, money=money1, score=0)
        # print(list)  # 总消费
        b = str(datetime.datetime.now())[-6:-1]
        a = random.randint(1000, 50000)
        number = (str(a) + (b))  # 订单号
        try:
            add = Address.objects.get(isDefault=1)  # 默认地址
        except:
            add = ""
        product_list = Car.objects.all()  # 购物车商品
        count = Car.objects.all().count()  # 购物车商品总数量
        order = Order()
        order.userId = user
        if add:
            order.addressId = add
            order.cost = list[-1]
            order.number = number
            order.quantity = count
            order.save()  # 添加订单
        else:
            return render(request, 'goods_car/BuyCar_Two.html',
                          {'total': list[-1], "msg": "您还没有收货地址",'product_list': product_list, "user": user, 'add': add})
        for i in product_list:
            quantity = i.number * i.productId.price
            o = Order_detail()
            o.quantity = i.number
            o.cost = quantity
            o.productId = i.productId
            o.orderId = order
            o.save()
        Car.objects.all().delete()  # 清空购物车
        order1 = Order.objects.filter(userId_id=1).last()  # 当前用户的所有订单
        order_detail1 = Order_detail.objects.filter(orderId=order1)  # 当前用户的所以订单
        return render(request, 'goods_car/BuyCar_Three.html',
                      {'order': order1, 'order_detail': order_detail1, 'list': list[-1],'money':money1})


def car4(request):  # 不使用积分
    username = request.COOKIES.get('username')
    user = UserProfile.objects.get(username=username)
    money1 = user.money - list[-1]  # 用户所剩金额
    print('不适应积分用户的积分是',user.score+list[-1])
    UserProfile.objects.filter(username=user).update(cost=user.cost + list[-1], money=money1,
                                                     score=user.score + list[-1])
    # print(list)  # 总消费
    b = str(datetime.datetime.now())[-6:-1]
    a = random.randint(1000, 50000)
    number = (str(a) + (b))  # 订单号
    try:
        add = Address.objects.get(isDefault=1)  # 默认地址
        print(add.email)
    except:
        add = ""

    product_list = Car.objects.all()  # 购物车商品
    count = Car.objects.all().count()  # 购物车商品总数量
    order = Order()
    order.userId = user
    if add:
        order.addressId = add
        order.cost = list[-1]
        order.number = number
        order.quantity = count
        print('订单添加完成')
        order.save()  # 添加订单
    else:
        return render(request, 'goods_car/BuyCar_Two.html',
                      {'total': list[-1], "msg": "您还没有收货地址",
                       'product_list': product_list, "user": user, 'add': add})
    for i in product_list:
        quantity = i.number * i.productId.price
        o = Order_detail()
        o.quantity = i.number
        o.cost = quantity
        o.productId = i.productId
        o.orderId = order
        o.save()
    Car.objects.all().delete()  # 清空购物车
    order1 = Order.objects.filter(userId_id=1).last()  # 当前用户的所有订单
    order_detail1 = Order_detail.objects.filter(orderId=order1)  # 当前用户的所以订单
    return render(request, 'goods_car/BuyCar_Three.html',
                  {'order': order1, 'order_detail': order_detail1, 'list': list[-1],'money':money1})


def car5(request):
    username=request.COOKIES.get('username')
    user=UserProfile.objects.get(username=username)
    product_list = Car.objects.all()  # 购物车商品
    count = Car.objects.all().count()  # 购物车商品总数量
    money=user.money
    return render(request, 'goods_car/BuyCar_Four.html',{"money":money,"product_list":product_list,"count":count,"total":list[-1]})
