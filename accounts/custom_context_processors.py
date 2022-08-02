from accounts.models import Cart, Wishlist
from accounts.scripts import get_cart
from products.models import Product
import json 

def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        subtotal = 0
        for item in cart.cartdetails_set.all():
            subtotal += item.total()
        cart_item_count = cart.get_item_count()
        wishlist_item_count = Wishlist.objects.get(user=request.user).get_item_count()
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
    
    return {"user_cart": cart, "cart_subtotal": subtotal, "cart_item_count": cart_item_count, "wishlist_item_count": wishlist_item_count}