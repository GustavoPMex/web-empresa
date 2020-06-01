from django.urls import path
from .views import home, about

home_patterns = ([
    path('', home, name='index'),
    path('about/', about, name='about'),
], 'home')