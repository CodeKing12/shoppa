from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('search-results', views.search_products, name='search_results'),
    path('games/franchises/<franchise_name>', views.game_franchises, name='game-franchise'),
    path('<category_url>/', views.products_category, name='category'),
    path('<category_url>/<field>/<field_value>/', views.product_group, name='field_products'),
    path('<category_url>/<slug>/', views.product_details, name='product-details'),
]

# urlpatterns = [
#     path("products/", views.get_products),
#     path("products/<id>", views.this_product),
# ]