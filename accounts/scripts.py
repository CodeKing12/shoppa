from .models import Cart, CartDetails, Wishlist, CustomAccount
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from products.models import Product
from django.contrib import messages
import json


def get_cart(session):
    cart = session.get("user-cart")
    if cart == None:
        cart = json.dumps({})
        session["user-cart"] = cart
    return json.loads(cart)

def parse_message(request, message, message_type):
    if message_type == "info":
        messages.info(request, message=message)
    elif message_type == "success":
        messages.success(request, message=message)
    elif message_type == "warning":
        messages.warning(request, message=message)
    elif message_type == "error":
        messages.error(request, message=message)

def add_to_wishlist(user, product):
    # product_id = request.POST["product_id"]
    # product = Product.objects.get(id=product_id)
    if user.is_authenticated:
        user_wishlist = Wishlist.objects.get_or_create(user=user)[0]
        try:
            the_p = user_wishlist.wish_products.get(id=product.id)
        except MultipleObjectsReturned:
            all_duplicated = user_wishlist.wish_products.filter(id=product.id)[1:]
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
        message = "You need to be logged in to add items to your wishlist"
        message_type = "warning"

    return message, message_type
    # return JsonResponse({"message": message, "type": message_type}, status=200)

def add_to_cart(request, product, quantity):
    quantity = int(quantity)
    # product_exists = Cart.cart_products.get(product)
    user = request.user
    product_id = product.id
    if user.is_authenticated:
        user_cart = Cart.objects.get(user=user)
        user_wishlist = Wishlist.objects.get_or_create(user=user)[0]
        try:
            the_p = user_cart.cart_products.get(id=product.id)
        except MultipleObjectsReturned:
            all_duplicated = user_cart.cart_products.filter(id=product.id)[1:]
            for item in all_duplicated:
                user_cart.cart_products.remove(item)
            message = "Multiple items found in your cart. Deleting Now."
            message_type = "info"
        except ObjectDoesNotExist:
            detailed_cart = CartDetails.objects.create(
                cart = user_cart,
                product = product,
                quantity = quantity,
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
        user_wishlist.wish_products.remove(product)
        return message, message_type
    else:
        user_cart = get_cart(request.session)
        message_type = "info"
        message = user_cart
        
        if str(product_id) in user_cart:
            item = user_cart[str(product_id)]
            item_quantity = int(item["quantity"])
            item["quantity"] = str(item_quantity + quantity)
            message = "Cart Item Updated"
            quantity = item["quantity"]
        else:
            user_cart[int(product_id)] = {"quantity": quantity}
            message = "Item Added To Cart"
        request.session['user-cart'] = json.dumps(user_cart)
        message_type = "success"
        
        return message, message_type

    return message, message_type

def remove_from_wishlist(user, product):
    if user.is_authenticated:
        try:
            user_wishlist = Wishlist.objects.get(user=user)
        except ObjectDoesNotExist:
            message_type = "error"
            message = "You do not have a wishlist"
        else:
            user_wishlist.wish_products.remove(product)
            message_type = "success"
            message = "Product removed from wishlist"
    else:
        message = "You do not have an account with us"
        message_type = "error"

    return message, message_type