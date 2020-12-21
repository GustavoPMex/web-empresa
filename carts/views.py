from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Cart
from .models import CartProducts
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

    quantity = int(request.POST.get('quantity', 1))

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart,
                                                                    product=item,
                                                                    quantity=quantity)

    return render(request, 'carts/add.html',{
        'quantity':quantity,
        'cart_product':cart_product,
        'item':item
    })

def remove(request):
    cart = get_or_create_cart(request)
    item = get_object_or_404(itemShop, pk=request.POST.get('product_id'))

    cart.products.remove(item)

    return redirect('carts:cart')

