from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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


class producto_individual(DetailView):
    model = itemShop
    template_name = 'shop/shop_individual.html'
    context_object_name = 'product'



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

class SearchView(ListView):
    model = itemShop
    template_name = 'shop/shop_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        
        query = query.title()

        if query:
            postresult = itemShop.objects.filter(name__contains=query)
            
            if postresult:
                result = postresult
            else:
                result = 'no results'
                
        else:
            result = 'no results'
        
        return result
    
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['items'] = itemShop.objects.all()
        context['categories'] = categoryModel.objects.all()

        return context