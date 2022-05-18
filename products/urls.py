from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<category>/<product_slug>', views.this_product, name='this_product')
    # path('create_vendor', views.create_vendor, name='create_vendor')
]