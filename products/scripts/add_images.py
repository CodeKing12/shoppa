from products.models import Product
from django.core.files import File
from shoppa.settings import BASE_DIR
import os

def run_me():
    all_products = Product.objects.all()
    for product in all_products:
        # print(product)
        pass
    
    the_p = all_products[11]
    print(the_p.name, the_p.image)
    file_path = 'products/scripts/Laptops/'
    file_name = 'center_facing6.png'
    the_file = file_path + file_name
    content = File(open(BASE_DIR / the_file, 'rb'))
    the_p.image.save(file_name, content, save=True)
    print(the_p.image)
