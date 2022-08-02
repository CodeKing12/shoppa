from accounts.models import Cart
from accounts.scripts import get_cart
from products.models import Product
import json 

def cart(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.get(user=request.user)
        subtotal = 0
        id_cart = 0
        # for item in user_cart.cartdetails_set.all():
        #     subtotal += item.total()
    else:
        # Retrieve session cart if user is not authenticated
        id_cart = get_cart(request.session)
        cart = {"items": [], "metadata": {}}

        # Turn the ids in the carts to a list
        cartlist = list(id_cart.keys())

        # Convert the string ids to integers
        for item in cartlist:
            pid = int(item)
            # Retrieve the objects for each id from the database and add them to a new list
            item_object = Product.objects.get(id=pid)
            cart["items"].append({"product": item_object, "quantity": id_cart[item]["quantity"]})

        # user_cart = Product.objects.filter(id__in=[])
    
    return {"user_cart": cart}