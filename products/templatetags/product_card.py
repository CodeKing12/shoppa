from django import template

register = template.Library()

@register.inclusion_tag('product-card.html')
def show_product(product):
    return {'product': product}