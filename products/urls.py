from django.urls import path
from . import views

urlpatterns = [
    path('our-products/', views.all_products, name='all_products'),
    # path('create_vendor', views.create_vendor, name='create_vendor')
]