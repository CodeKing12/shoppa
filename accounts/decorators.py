from .models import Cart, CartDetails
from products.models import Product
import json

def insert_cart(function):
    def wrap(request, *args, **kwargs):
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
        return function(request, *args, **kwargs)
            
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap