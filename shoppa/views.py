from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .forms import LoginForm
from django.contrib import messages

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
    login = LoginForm()
    # messages.success(request, f"Form submitted successfully. Your email is {data}")
    return render(request, 'index.html', {'login_form': login})

def login(request):
    if is_ajax(request) and request.method == 'POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            saved_form = login.save()
            ser_login = serializers.serialize('json', [saved_form])
            return JsonResponse({'Saved Form': ser_login}, status=200)
        else:
            return JsonResponse({'errors': login.errors}, status=400)
    return JsonResponse({"error": "Unknown Error Occured"}, status=400)

# When the user is authenticated, the authenticated info will be sent the page in json and the success function will add them to their respective divs e.g. cart items will be sent and the JS will add them to the cart
