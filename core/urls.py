from django.urls import path
from .views import home

home_patterns = ([
    path('', home, name='index')
], 'home')