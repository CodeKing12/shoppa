from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login as django_login, logout

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def login_view(request):
    if is_ajax(request) and request.method == 'POST':
        login_details = LoginForm(request.POST)
        if login_details.is_valid():
            email = login_details.cleaned_data['email']
            password = login_details.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is None:
                return JsonResponse({'message': 'Your email or password is incorrect', 'type': 'error'}, status=200)
            elif request.user.is_authenticated:
                return JsonResponse({'message': 'You are already logged in', 'type': 'warning'}, status=200)
            else:
                django_login(request, user)
            # saved_form = login.save()
            # ser_login = serializers.serialize('json', [saved_form])
                # messages = ["Login Successful", user.first_name]
                return JsonResponse({'message': 'Login Successful', 'type': 'success'}, status=200)
        else:
            return JsonResponse({'errors': django_login.errors}, status=400)
    return JsonResponse({"error": "Unknown Error Occured"}, status=400)

def user_profile(request):
    return HttpResponse("Hi")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        request.session['logout_message'] = ["Log Out Successful", "success"]
        return redirect('home')
    else:
        request.session['logout_message'] = ["You are not logged in", "warning"]
        return redirect('home')