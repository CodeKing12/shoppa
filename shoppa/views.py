from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
from accounts.forms import LoginForm, CreateAccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login as django_login, logout
from django.views.decorators.csrf import csrf_protect
from accounts.models import ApiUser, Cart, CartDetails, CustomAccount
from products.models import Product
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
import json

import environ
env = environ.Env()

project_email = env("PROJECT_EMAIL")
project_phone = env("PROJECT_PHONE")
project_first = env("PROJECT_FIRST")
project_last = env("PROJECT_LAST")

try:
    admin_user = CustomAccount.objects.get(email=project_email, first_name=project_first, last_name=project_last)
except ObjectDoesNotExist:
    project_password = env("PROJECT_PASSWORD")
    admin_user = CustomAccount.objects.create_superuser(email=project_email, phone_number=project_phone, first_name=project_first, last_name=project_last, password=project_password)

try:
    api_admin = ApiUser.objects.get(user=admin_user)
except ObjectDoesNotExist:
    api_admin = ApiUser.objects.create(user=admin_user, product_groups={
        "featured": [50, 242, 262, 48, 239, 258, 46, 235, 257, 45, 233, 255, 41, 230, 253, 40, 223, 251], 
        "discounted": [48, 240, 260, 47, 238, 259, 40, 225, 258, 42, 218, 257, 29, 208, 255, 24, 204, 250]
    })
product_groups = api_admin.product_groups

def convert_to_list(list):
    object_list = []
    for id in list:
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            print(f"There is no product with an id of {id}")
            continue


def get_cart(request):
    sub_total = 0
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart_details = CartDetails.objects.filter(cart=cart)
        for item in cart_details:
            sub_total += item.product.price
    else:
        cart_details = []
        session_cart = request.session.get("user-cart", json.dumps({}))
        print(session_cart)
        anon_cart = json.loads(session_cart)
        for product_id, details in anon_cart.items():
            cart_product = Product.objects.get(id=product_id)
            cart_details.append([cart_product, details[0], details[1]])
    return cart_details, sub_total

@csrf_protect
def home(request):
    login = LoginForm()
    register = CreateAccountForm()
    if 'action_message' in request.session:
        message = request.session['action_message'][0]
        level = request.session["action_message"][1]
        del request.session['action_message']
        if level == "success":
            messages.success(request, message)
        elif level == "warning":
            messages.warning(request, message)
        elif level == "error":
            messages.error(request, message)
        elif level == "info":
            messages.info(request, message)

    if 'open_login' in request.session:
        open_login = request.session["open_login"]
        del request.session['open_login']
    else:
        open_login = ["", "", False]
    # messages.success(request, f"Form submitted successfully. Your email is {data}")
    featured_products = []
    discounted_products = []
    featured_products = Product.objects.filter(pk__in=product_groups["featured"]).order_by("?")
    discounted_products = Product.objects.filter(pk__in=product_groups["discounted"]).order_by("?")
    affordable_laptops = Product.objects.filter(category="PC").order_by("percent_off")[:24]
    popular_phones = Product.objects.filter(category="PHONE").order_by("?")[:24]
    popular_games = Product.objects.filter(category="GAME").order_by("?")[:24]
    current_site = request.build_absolute_uri()
    current_site = str(current_site.strip("/"))
    sub_total = 0
    # if request.user.is_authenticated:
    #     cart = Cart.objects.get(user=request.user)
    #     cart_details = CartDetails.objects.filter(cart=cart)
    #     for item in cart_details:
    #         sub_total += item.product.price
    # else:
    #     cart_details = []
    #     session_cart = request.session.get("user-cart", json.dumps({}))
    #     print(session_cart)
    #     anon_cart = json.loads(session_cart)
    #     for product_id, details in anon_cart.items():
    #         cart_product = Product.objects.get(id=product_id)
    #         cart_details.append([cart_product, details[0], details[1]])

    return render(request, 'home.html', {'login_form': login, "register_form": register, "open_login": open_login, "discounted_products": discounted_products, "featured_products": featured_products, "popular_phones": popular_phones, "affordable_laptops": affordable_laptops, "popular_games": popular_games, "domain": current_site, "cart_details": "cart_details", "cart_total": sub_total})

# When the user is authenticated, the authenticated info will be sent the page in json and the success function will add them to their respective divs e.g. cart items will be sent and the JS will add them to the cart

def help_page(request):
    return HttpResponse("Help Who?")

def privacy_policy(request):
    return render(request, "privacy-policy.html")

def privacy_policy(request):
    return render(request, "privacy-policy.html")

def return_policy(request):
    return render(request, "returns-policy.html")

def shipping_policy(request):
    return render(request, "shipping-policy.html")

def payment_policy(request):
    return render(request, "payment-policy.html")

def terms_and_conditions(request):
    return render(request, "terms-and-conditions.html")
