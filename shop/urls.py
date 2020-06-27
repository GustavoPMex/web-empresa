from django.urls import path
from .views import shop_view, shop_cat_view , shop_price_view, SearchView

shop_urls = ([
    path('', shop_view, name='index'),
    path('category/', shop_cat_view, name='category'),
    path('price/', shop_price_view, name='price'),
    path('search/', SearchView.as_view(), name='search_p')
],'shop')