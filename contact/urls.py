from django.urls import path
from .views import contact_view

contact_patterns = ([
    path('', contact_view, name='index'),
], 'contact')