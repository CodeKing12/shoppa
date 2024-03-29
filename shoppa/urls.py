"""shoppa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
import accounts.views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('help/', views.help_page, name='help'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('return-policy/', views.return_policy, name='return_policy'),
    path('shipping-policy/', views.shipping_policy, name='shipping_policy'),
    path('payment-policy/', views.payment_policy, name='payment_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('contact/', views.help_page, name='contact'),
    path('shop/', include('products.urls')),
    path('blog/', include('blog.urls')),
    # path('api/v1/', include('products.api.api_urls')),
    path('account/', include('accounts.urls')),
    path('login/', accounts_views.login_view, name="login_account"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)