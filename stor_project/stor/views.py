from django.shortcuts import render
from .models import *

def build_template(lst, cols):
    return [lst[i:i+cols] for i in range(0, len(lst), cols)] 

def product_list(request):
    search_querry = request.GET.get("search",None)
    if search_querry:
        products = Product.objects.filter(title__icontains = search_querry)
    else:
        products = Product.objects.all()
    return render(
        request,
        "stor/product_list.html",
        context={"product_list": build_template(products, 3)}
    )

def category_list(request):
    categories = Category.objects.all()
    return render (request, "stor/categories.html", context={"categories": categories,})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render (request, "stor/product_detail.html", context={"product": product})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = category.products.all()
    return render (request, "stor/category_detail.html", context={"product_list": build_template(products, 3), "category": category})

def save_order(request):
    order = Order()
    order.name = request.POST["user_name"]
    order.email = request.POST["user_email"]
    order.product = Product.objects.get(pk=request.POST["product_id"])
    order.save()
    return render(request, "stor/product_list.html")
    
"Привет, artem! Ваш заказ находиться в оброботке"

    
