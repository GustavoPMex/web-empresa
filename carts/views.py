from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Cart
from shop.models import itemShop
from .utils import get_or_create_cart
# Create your views here.

def cart(request):

    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html',{
        'cart':cart
    })

def add(request):

    cart = get_or_create_cart(request)

    item = get_object_or_404(itemShop, pk=request.POST.get('product_id'))

    cart.products.add(item)

    return render(request, 'carts/add.html',{
        'item':item
    })

def remove(request):
    cart = get_or_create_cart(request)
    item = get_object_or_404(itemShop, pk=request.POST.get('product_id'))

    cart.products.remove(item)

    return redirect('carts:cart')

