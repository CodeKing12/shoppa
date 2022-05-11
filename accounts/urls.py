from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.create_account, name='register_user'),
    path('login/', views.login_view, name='login_page'),
    path('my-dashboard/', views.user_dashboard, name="dashboard"),
    path("activate/<uidb64>/<token>", views.activate_account, name="activate_account"),
    path('resend/', views.resend_token, name='resend_token'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('change_password/<uidb64>/<token>', views.change_password, name='change_password'),
    path('my-wishlist/', views.wishlistview, name='wishlist'),
    path('my-cart/', views.cartview, name='cart'),
    path('logout/', views.logout_user, name='logout'),
    # path('create_vendor', views.create_vendor, name='create_vendor')
]