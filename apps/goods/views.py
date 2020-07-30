from django.shortcuts import render,redirect

# Create your views here.
from.models import Product
from car.models import Car


def product_detail(request):
    id = request.GET.get('id')
    if id:
        product = Product.objects.get(id=id)
        if request.method== "POST":
            num = request.POST.get('num', 1)
            Car.objects.create(number= num,productId_id= id,userId_id=request.user.id)
            return render(request, "goods/ProductDetail.html", {'product': product,'msg':'加入购物车完成'})
        return render(request,"goods/ProductDetail.html",{'product' : product})

    return redirect("index")
