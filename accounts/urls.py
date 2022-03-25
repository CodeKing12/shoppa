from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    # path('', views.create_account, name='create-account'),
    path('login/', views.login_view, name='login_page'),
    path('profile/', views.user_profile, name="profile")
    # path("activate/<uidb64>/<token>", views.activate_account, name="activate_account"),
    # path('resend/', views.resend_token, name='resend_token'),
    # path('reset_password/', views.reset_password, name='reset_password'),
    # path('change_password/<uidb64>/<token>', views.change_password, name='change_password'),
    # path('cartwish/', views.cartwish, name='test_cartwish'),
    # path('logout/', views.logout_user, name='logout'),
    # path('logout_user/', views.logout_success, name='logout_success'),
    # path('create_vendor', views.create_vendor, name='create_vendor')
]