from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views, api_views
from django.conf import settings

urlpatterns = [
    path('create/', views.create_account, name='register_user'),
    path('login/', views.login_view, name='login_page'),
    path('my-dashboard/', views.user_dashboard, name="dashboard"),
    path('my-address/', views.user_address, name="address"),
    path('my-order-history/', views.order_history, name="order_history"),
    path('my-support-tickets/', views.support_tickets, name="support_tickets"),
    path("activation-link/", views.activate_button, name="activation_page"),
    path("confirm-password-email/", views.confirm_pass_email, name="password_page"),
    path("activate/<uidb64>/<token>/", views.activate_account, name="activate_account"),
    path('resend/', views.resend_token, name='resend_token'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('update-password/', views.update_password, name='update_password'),
    path('change-password/<uidb64>/<token>/', views.change_password, name='change_password'),
    path('my-wishlist/', views.wishlist, name='wishlist'),
    path('my-cart/', views.cartview, name='cart'),
    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
    # path('remove-from-cart/', views.remove_from_cart, name="remove_from_cart"),
    path('add-to-wishlist/', views.add_to_wishlist, name="add_to_wishlist"),
    path('remove-from-wishlist/', views.remove_from_wishlist, name="remove_from_wishlist"),
    path('checkout/', views.checkout, name="checkout"),
    path('logout/', views.logout_user, name='logout'),
    # path('create_vendor', views.create_vendor, name='create_vendor')
]

# I added a slash to both url mappings that end with <token>. Putting this here incase the code breaks