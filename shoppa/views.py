from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
from accounts.forms import LoginForm, CreateAccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login as django_login, logout
from django.views.decorators.csrf import csrf_protect
from accounts.models import Cart, CartDetails
from products.models import Product
import json

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

    discounted_list = Product.objects.all()
    current_site = request.build_absolute_uri()
    current_site = str(current_site.strip("/"))
    sub_total = 0
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart_details = CartDetails.objects.filter(cart=cart)
        for item in cart_details:
            sub_total += item.product.price
    else:
        cart_details = []
        session_cart = request.session.get("user-cart", json.dumps({}))
        anon_cart = json.loads(session_cart)
        for product_id, details in anon_cart.items():
            cart_product = Product.objects.get(id=product_id)
            cart_details.append([cart_product, details[0], details[1]])
            
    return render(request, 'index.html', {'login_form': login, "register_form": register, "open_login": open_login, "discounted": discounted_list, "domain": current_site, "cart_details": cart_details, "cart_total": sub_total})

# When the user is authenticated, the authenticated info will be sent the page in json and the success function will add them to their respective divs e.g. cart items will be sent and the JS will add them to the cart
