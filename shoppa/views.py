from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
from accounts.forms import LoginForm, CreateAccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login as django_login, logout

def home(request):
    login = LoginForm()
    register = CreateAccountForm()
    if 'logout_message' in request.session:
        message = request.session['logout_message'][0]
        level = request.session["logout_message"][1]
        del request.session['logout_message']
        if level == "success":
            messages.success(request, message)
        elif level == "warning":
            messages.warning(request, message)
        elif level == "error":
            messages.error(request, message)
        elif level == "info":
            messages.info(request, message)

    open_login = False

    if 'open_login' in request.session:
        open_login = True
        del request.session['open_login']
    # messages.success(request, f"Form submitted successfully. Your email is {data}")
    return render(request, 'index.html', {'login_form': login, "register_form": register, "open_login": open_login})

# When the user is authenticated, the authenticated info will be sent the page in json and the success function will add them to their respective divs e.g. cart items will be sent and the JS will add them to the cart
