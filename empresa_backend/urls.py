"""empresa_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.urls import home_patterns
from contact.urls import contact_patterns
from clients.urls import clients_patterns
from shop.urls import shop_urls
from carts.urls import cart_patterns
from django.conf import settings


urlpatterns = [
    path('', include(home_patterns)), 
    path('contact/', include(contact_patterns)),
    path('clients/', include(clients_patterns)),
    path('carrito/', include(cart_patterns)),
    path('shop/', include(shop_urls)),
    path('admin/', admin.site.urls),
    #PATHS TO USER
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)