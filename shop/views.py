from django.shortcuts import render, redirect
from .models import itemShop, categoryModel


# Create your views here.

def shop_view(request):
    items = itemShop.objects.all()
    categories = categoryModel.objects.all()

    modelos = {
        'items':items,
        'categories':categories
    }

    return render(request, 'shop/shop.html', modelos)

def shop_price_view(request):
    items = itemShop.objects.all()
    categories = categoryModel.objects.all()

    modelos = {
        'items':items,
        'categories':categories
    }

    if request.method == 'POST':

        option_value = request.POST.get('filter_price', )
        
        if option_value == 'all':
            return redirect('shop:index')
        
        elif option_value == '1':
            products_price = itemShop.objects.filter(price__range=(0,500))
        
        elif option_value == '2':
            products_price = itemShop.objects.filter(price__range=(0,1000))
        
        else:
            products_price = itemShop.objects.filter(price__range=(1000,9999))
        
        modelos['products_price'] = products_price
    
    elif request.method == 'GET':
        return redirect('shop:index')


    return render(request, 'shop/shop_price.html', modelos)


def shop_cat_view(request):
    items = itemShop.objects.all()
    categories = categoryModel.objects.all()

    modelos = {
        'items':items,
        'categories':categories
    }

    if request.method == 'POST':
        option_value = request.POST.get('filter_cat', )

        if option_value == 'all':
            return redirect('shop:index')
        
        products_cat = itemShop.objects.filter(category__name = option_value)
        modelos['products_cat'] = products_cat
    
    elif request.method == 'GET':
        return redirect('shop:index')

    return render(request, 'shop/shop_category.html', modelos)