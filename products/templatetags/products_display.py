from django import template
from products.models import Product

register = template.Library()

@register.inclusion_tag("products/product_card.html")
def product_card(product):
    return {"product": product}

@register.inclusion_tag("products/product_slider.html")
def product_slider(product_list):
    return {"product_list": product_list}

@register.inclusion_tag("products/product_grid.html")
def products_grid(product_list):
    try:
        product_list = list(product_list)
        for item in product_list:
            if type(item) != Product:
                item_index = product_list.index(item)
                product_list[item_index] = item.product
    except:
        product_list = product_list
        
    return {"product_list": product_list}