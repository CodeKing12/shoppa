from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from products.models import Product
from .forms import LoginForm, CreateAccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login as django_login, logout
from .models import Cart, CartDetails, Wishlist, CustomAccount
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from accounts.decorators import insert_cart
from rest_framework.decorators import api_view
import json
from shoppa.views import get_cart

from django.http import JsonResponse
from .serializers import RegistrationSerializer
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from accounts import serializers

@csrf_exempt
@api_view(("GET", "POST"))
def create_account(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(("GET", "POST"))
def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        # return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)