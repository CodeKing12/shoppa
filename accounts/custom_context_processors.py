from django.shortcuts import get_object_or_404
from accounts.models import Cart, Wishlist
from accounts.scripts import get_cart
from products.models import Product
import json
from django.contrib import messages
from accounts.scripts import add_to_cart, add_to_wishlist, parse_message, remove_from_wishlist, remove_from_cart, clear_wishlist, clear_cart

def cart(request):
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
    if request.method == "POST":
        if "add_to_cart" in request.POST:
            print(request.POST)
            product_id = request.POST["add_to_cart"]
            product = get_object_or_404(Product, id=int(product_id))

            try:
                quantity = request.POST["quantity"][0]
            except KeyError:
                quantity = "1"

            message, message_type = add_to_cart(request=request, product=product, quantity=quantity)
            parse_message(request, message, message_type)

        elif "add_to_wishlist" in request.POST:
            product_id = request.POST["add_to_wishlist"]
            product = get_object_or_404(Product, id=int(product_id))

            message, message_type = add_to_wishlist(user=request.user, product=product)
            parse_message(request, message, message_type)

        elif "remove_from_wishlist" in request.POST:
            product_id = request.POST["remove_from_wishlist"]
            product = get_object_or_404(Product, id=int(product_id))

            message, message_type = remove_from_wishlist(user=request.user, product=product)
            parse_message(request, message, message_type)

        elif "remove_from_cart" in request.POST:
            product_id = request.POST["remove_from_cart"]
            product = get_object_or_404(Product, id=int(product_id))

            message, message_type = remove_from_cart(request=request, product=product)
            parse_message(request, message, message_type)

        elif "clear_wishlist" in request.POST:
            message, message_type = clear_wishlist(user=request.user)
            parse_message(request, message, message_type)
        
        elif "clear_cart" in request.POST:
            message, message_type = clear_cart(request=request)
            parse_message(request, message, message_type)

    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        subtotal = 0
        for item in cart.cartdetails_set.all():
            subtotal += item.total()
        cart_item_count = cart.get_item_count()
        wishlist_item_count = Wishlist.objects.get_or_create(user=request.user)[0].get_item_count()
    else:
        wishlist_item_count = 0
        # Retrieve session cart if user is not authenticated
        id_cart = get_cart(request.session)
        cart = {"items": [], "metadata": {}}

        # Turn the ids in the carts to a list
        cartlist = list(id_cart.keys())

        # Convert the string ids to integers
        subtotal = 0
        for item in cartlist:
            pid = int(item)
            # Retrieve the objects for each id from the database and add them to a new list
            item_object = Product.objects.get(id=pid)
            quantity = id_cart[item]["quantity"]
            cart["items"].append({"product": item_object, "quantity": quantity})
            subtotal += int(quantity) * int(item_object.price)
        
        cart_item_count = len(cartlist)
    
    return {"user_cart": cart, "cart_subtotal": subtotal, "cart_item_count": cart_item_count, "wishlist_item_count": wishlist_item_count, "open_login": open_login}