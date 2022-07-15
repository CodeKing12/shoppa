from django.urls import path
from . import viewsets

urlpatterns = [
    path("products/", viewsets.get_products),
    path("products/<id>", viewsets.get_product),
]