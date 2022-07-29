from django import template

register = template.Library()

@register.inclusion_tag("products/product_card.html")
def product_card(product):
    return {"product": product}

@register.inclusion_tag("products/product_slider.html")
def product_slider(product_list):
    return {"product_list": product_list}

@register.inclusion_tag("products/product_grid.html")
def products_grid(product_list):
    return {"product_list": product_list}