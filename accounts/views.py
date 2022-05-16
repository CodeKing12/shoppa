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
import json
from shoppa.views import get_cart

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@csrf_protect
def create_account(request):
    if is_ajax(request) and request.method == 'POST':
        registration_form = CreateAccountForm(request.POST)
        if registration_form.is_valid():
            if request.user.is_authenticated:
                return JsonResponse({'message': 'You are already logged in to an account', 'type': 'warning'}, status=400)
            elif not request.user.is_authenticated:
                # Retrieve info from form and create user
                first_name = registration_form.cleaned_data['first_name']
                last_name = registration_form.cleaned_data['last_name']
                email = registration_form.cleaned_data['email']
                phone_number = registration_form.cleaned_data['phone_number']
                password = registration_form.cleaned_data['password']
                user = CustomAccount.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password)
                user.save()

                # Send Confirmation Email
                
                current_site = get_current_site(request)
                mail_subject = 'Activate your account'
                message = render_to_string('accounts/confirm_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                to_email = user.email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()

                # Tell user to check email

                return JsonResponse({'message': 'An Activation Link Has Been Sent to Your E-mail', 'type': 'success'}, status=200)
                # info = "An activation link has been sent to your email address. Click on it to fully activate your account and login."
                # return render(request, "accounts/message_template.html", {"message": info})
                #return HttpResponse(user.first_name)
            
        else:
            return JsonResponse({'message': registration_form.errors, 'type': 'error'}, status=400)
    elif is_ajax(request) and request.method == 'GET':
        return JsonResponse({'message': 'Cart Created Successfully', 'type': 'success'}, status=200)
    return JsonResponse({'message': 'An Unknown Error Occurred', 'type': 'error'}, status=400)
    # return render(request, 'accounts/create-account.html', {'form': the_form})

def activate_account(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        # uid = 0
        user = CustomAccount.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomAccount.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.user.is_authenticated:
            request.session["open_login"] = ["You cannot authenticate an account while logged in", "warning", True]
        elif user.is_active == True:
            request.session["open_login"] = ["This account has been activated already", "warning", True]
        else:
            user.is_active = True
            user.save()
            cart = Cart.objects.create(user=user)
            wishlist = Wishlist.objects.create(user=user)
            cart.save()
            wishlist.save()
            request.session["open_login"] = ["Your account has been successfully activated", "success", True]
            return redirect('home')
    else:
        request.session['action_message'] = ["Activation Link is Invalid", "error"]
        return redirect('home')

def resend_token(request):
    if is_ajax(request) and request.method == 'POST':
        email = request.POST['user_email']
        try:
            user = CustomAccount.objects.get(email=email)
        except CustomAccount.DoesNotExist:
            return JsonResponse({'message': 'This user does not exist', 'type': 'error'}, status=200)
        else:
            if user.is_active == True:
                return JsonResponse({'message': 'This user has already been activated', 'type': 'warning'}, status=200)
            else:
                current_site = get_current_site(request)
                mail_subject = 'Activate your account'
                message = render_to_string('accounts/confirm_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                to_email = user.email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()

                return JsonResponse({'message': 'An Activation Link Has Been Sent to Your E-mail', 'type': 'success'}, status=200)
    else:
        request.session['action_message'] = ["Invalid Request", "error"]
        return redirect('home')

def reset_password(request):
    if is_ajax(request) and request.method == 'POST':
        email = request.POST['email_identity']
        try:
            user = CustomAccount.objects.get(email=email)
        except CustomAccount.DoesNotExist:
            return JsonResponse({'message': 'That user does not exist', 'type': 'error'}, status=200)
        else:
            if user.is_active == False:
                return JsonResponse({'message': 'This user has not been confirmed. Please request an activation token on the login page', 'type': 'warning'}, status=200)
            else:
                current_site = get_current_site(request)
                mail_subject = 'Activate your account'
                message = render_to_string('accounts/reset_password_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                to_email = user.email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return JsonResponse({'message': 'Your confirmation link has been sent', 'type': 'success'}, status=200)
    else:
        request.session['action_message'] = ["Invalid Request", "error"]
        return redirect('home')

def change_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        # uid = 0
        user = CustomAccount.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomAccount.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        request.session["confirmed"] = True
        request.session["uid"] = uid
        return redirect('update_password')
    else:
        request.session['action_message'] = ["Confirmation Link is Invalid", "error"]
        return redirect('home')

@insert_cart
def wishlist(request):
    if request.user.is_superuser:
        user_wishlist = 'Nothing'
        all_products = []
    elif not request.user.is_authenticated:
        request.session['open_login'] = ["You have to log in to view your wishlist", "warning", True]
        return redirect('home')
    else:
        cart_details, sub_total = get_cart(request)
        user_wishlist = Wishlist.objects.get(user=request.user)
        all_products = user_wishlist.wish_products.all()
    return render(request, 'products/wishlist.html', context={'cart_details': cart_details, 'wishlist': user_wishlist, 'cart_total': sub_total})

@csrf_protect
def login_view(request):
    if is_ajax(request) and request.method == 'POST':
        login_details = LoginForm(request.POST)
        if login_details.is_valid():
            email = login_details.cleaned_data['email']
            password = login_details.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is None:
                return JsonResponse({'message': 'Your email or password is incorrect', 'type': 'error'}, status=400)
            elif request.user.is_authenticated:
                return JsonResponse({'message': 'You are already logged in to an account', 'type': 'warning'}, status=400)
            else:
                if user.is_active == True:
                    django_login(request, user)
                    return JsonResponse({'message': 'Login Successful', 'type': 'success'}, status=200)
                elif user.is_active == False:
                    return JsonResponse({'message': 'Login Failed! Your account has not been activated', 'type': 'info'}, status=400)
            # saved_form = login.save()
            # ser_login = serializers.serialize('json', [saved_form])
                # messages = ["Login Successful", user.first_name]
        else:
            return JsonResponse({'message': login_details.errors, 'type': 'error'}, status=400)
    return JsonResponse({"error": "Unknown Error Occured"}, status=400)
    # Learn how to Intercept csrf errors and reload the page

def user_dashboard(request):
    if request.user.is_authenticated:
        user_details = CustomAccount.objects.get(email=request.user.email)
        return render(request, "accounts/dashboard.html", context={"user": user_details})
    elif not request.user.is_authenticated:
        request.session['open_login'] = ["You have to log in to view your dashboard", "warning", True]
        return redirect('home')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        request.session['action_message'] = ["Log Out Successful", "success"]
        return redirect('home')
    else:
        request.session['action_message'] = ["You are not logged in", "warning"]
        return redirect('home')

def cartview(request):
    if request.user.is_superuser:
        user_cart = 'Nothing'
        user_wishlist = 'Nothing'
    else:
        user_cart = Cart.objects.get(user=request.user)
        user_wishlist = Wishlist.objects.get(user=request.user)
    return render(request, 'products/cart.html', context={'cart': user_cart, 'wishlist': user_wishlist})

def add_to_cart(request):
    if is_ajax(request) and request.method == "POST":
        product_id = request.POST["product_id"]
        product = Product.objects.get(id=product_id)
        if "quantity" in request.POST:
            quantity = int(request.POST["quantity"])
        else:
            quantity = 1
        if "color" in request.POST:
            color = request.POST["color"]
        else:
            color = "#000000"
        # product_exists = Cart.cart_products.get(product)
        if request.user.is_authenticated:
            user_cart = Cart.objects.get(user=request.user)
            try:
                the_p = user_cart.cart_products.get(id=product_id)
            except MultipleObjectsReturned:
                all_duplicated = user_cart.cart_products.filter(id=product_id)[1:]
                for item in all_duplicated:
                    user_cart.cart_products.remove(item)
                message = "Multiple items found in your cart. Deleting Now."
                message_type = "info"
            except ObjectDoesNotExist:
                detailed_cart = CartDetails.objects.create(
                    cart = user_cart,
                    product = product,
                    quantity = quantity,
                    color = color
                )
                detailed_cart.save()
                message = "Item added to cart"
                message_type = "success"
            else:
                complete_cart = CartDetails.objects.get(cart=user_cart, product=product)
                complete_cart.quantity += quantity
                complete_cart.save()
                quantity = complete_cart.quantity
                message = "Cart Updated Successfully"
                message_type = "success"
            return JsonResponse({"message": message, "type": message_type}, status=200)
        else:
            cart = request.session.get("user-cart", json.dumps({}))
            user_cart = json.loads(cart)
            if product_id in user_cart:
                product = user_cart[product_id]
                product[0] += 1
                message = "Cart Updated Successfully"
                quantity = product[0]
            else:
                user_cart[int(product_id)] = [quantity,color.strip("#")]
                message = "Item Added To Cart"
            request.session['user-cart'] = json.dumps(user_cart)
            return JsonResponse({"message": message, "type": "success"}, status=200)
    else:
        request.session['action_message'] = ["Invalid Request", "error"]
        return redirect('home')

def remove_from_cart(request):
    if is_ajax(request) and request.method == "POST":
        product_id = request.POST["product_id"]
        product = Product.objects.get(id=product_id)
        # product_exists = Cart.cart_products.get(product)
        if request.user.is_authenticated:
            user_cart = Cart.objects.get(user=request.user)
            try:
                the_p = user_cart.cart_products.get(id=product_id)
            except MultipleObjectsReturned:
                all_duplicated = user_cart.cart_products.filter(id=product_id)[1:]
                for item in all_duplicated:
                    user_cart.cart_products.remove(item)
                message = "Multiple items found in your cart. Deleting All Now."
                message_type = "info"
                messages.success(message="All Items Deleted")
            except ObjectDoesNotExist:
                message = "You have not added this item to your cart"
                message_type = "error"
            else:
                user_cart.cart_products.remove(product)
                message = "Item Removed From Cart"
                message_type = "success"
            return JsonResponse({"message": message, "type": message_type}, status=200)
        else:
            cart = request.session.get("user-cart", json.dumps({}))
            user_cart = json.loads(cart)
            if product_id in user_cart:
                del user_cart[product_id]
                message = "Item Removed From Cart"
                message_type = "success"
            else:
                message = "You have not added this item to your cart"
                message_type = "success"
            request.session['user-cart'] = json.dumps(user_cart)
            return JsonResponse({"message": message, "type": "success"}, status=200)
    else:
        request.session['action_message'] = ["Invalid Request", "error"]
        return redirect('home')

def add_to_wishlist(request):
    if is_ajax(request) and request.method == "POST":
        product_id = request.POST["product_id"]
        product = Product.objects.get(id=product_id)
        if request.user.is_authenticated:
            user_wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
            print(user_wishlist)
            try:
                the_p = user_wishlist.wish_products.get(id=product_id)
            except MultipleObjectsReturned:
                all_duplicated = user_wishlist.wish_products.filter(id=product_id)[1:]
                for item in all_duplicated:
                    user_wishlist.wish_products.remove(item)
                message = "Multiple items found in your Wishlist. Deleting Now."
                message_type = "info"
            except ObjectDoesNotExist:
                user_wishlist.wish_products.add(product)
                user_wishlist.save()
                message = "Item added to Wishlist"
                message_type = "success"
            else:
                message = "This item already exists in your wishlist"
                message_type = "info"
        else:
            message = "You have to create an account to add items to your wishlist"
            message_type = "info"
        return JsonResponse({"message": message, "type": message_type}, status=200)
    else:
        request.session['action_message'] = ["Invalid Request", "error"]
        return redirect('home')

def remove_from_wishlist(request):
    pass
    
def update_password(request):
    if is_ajax(request) and request.method == 'POST':
        uid = request.POST["uid"]
        user = CustomAccount.objects.get(pk=uid)
        password1 = request.POST['new_pass1']
        password2 = request.POST['new_pass2']
        if password1 == password2:
            user.set_password(password1)
            user.save()
            return JsonResponse({'message': 'Password changed successfully. You can now login', 'type': 'success'}, status=200)
            # request.session['open_login'] = ["Password changed successfully. You can now login", "success", True]
            # return redirect('home')
        else:
            return JsonResponse({'message': 'Your passwords don\'t match', 'type': 'error'}, status=200)
    else:
        if "confirmed" in request.session:
            del request.session['confirmed']
            uid = request.session["uid"]
            return render(request, 'accounts/change_password.html', context={"user_id": uid})
        else:
            request.session['action_message'] = ["Invalid Request", "error"]
            return redirect('home')
