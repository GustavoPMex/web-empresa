from django.urls import path
from .views import shop_view

shop_urls = ([
    path('', shop_view, name='index'),
],'shop')