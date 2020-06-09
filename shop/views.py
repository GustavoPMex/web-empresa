from django.shortcuts import render
from .models import itemShop


# Create your views here.

def shop_view(request):
    items = itemShop.objects.all()
    return render(request, 'shop/shop.html', {'items':items})
