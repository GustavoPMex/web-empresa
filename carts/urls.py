from django.urls import path
from .views import cart, add, remove

cart_patterns = ([
    path('', cart, name='cart'),
    path('agregar/', add, name='add'),
    path('eliminar/', remove, name='remove'),
], 'carts')