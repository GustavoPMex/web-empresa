from django.urls import path
from .views import clientes_view

clients_patterns = ([
    path('', clientes_view, name='index')
], 'clientes')