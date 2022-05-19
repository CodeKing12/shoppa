import random
from products.models import GAME_OS_CHOICES, PROCESSOR_TYPE_CHOICES, Product, Game
from .add_items import generate_price, generate_text, get_bool, get_choice

# Let all other values like weight, faceunlock, accelerometer, be generated on the spot so they can be different

def generate_game_data(number_of_items):
    generated_info =  []
    for number in range(number_of_items):
        price, previous_price = generate_price('phone')
        generated_info.append(
            {
                "name": "",
                "image": "",
                "description": generate_text(),
                "price": price,
                "previous_price": previous_price, # Check how invidivually access each variable in the return statement
                "in_stock": get_bool(),
                "product_type": "GAME",
                "min_ram": "",
                "min_storage": "",
                "developers": "",
                "recom_ram": "",
                "recom_storage": "",
                "min_processor": "",
                "recom_processor": "",
                "processor_type": get_choice(PROCESSOR_TYPE_CHOICES),
                "os_type": get_choice(GAME_OS_CHOICES),
                "min_dx_version": "",
                "recom_dx_version": "",
                "size": "",
                "min_graphics_card": "",
                "recom_graphics_card": "",
            }
        )
    return generated_info


def add_to_db(number_of_items):
    all_generated_info = generate_game_data(number_of_items)

    for product_info in all_generated_info:
        name = product_info["name"]
        image = product_info["image"]
        description = product_info["description"]
        price = product_info["price"]
        previous_price = product_info["previous_price"]
        in_stock = product_info["in_stock"]
        product_type = product_info["product_type"]
        min_ram = product_info["min_ram"]
        min_storage = product_info["min_storage"]
        developers = product_info["developers"]
        recom_ram = product_info["recom_ram"]
        recom_storage = product_info["recom_storage"]
        min_processor = product_info["min_processor"]
        recom_processor = product_info["recom_processor"]
        processor_type = product_info["processor_type"]
        os_type = product_info["os_type"]
        min_dx_version = product_info["min_dx_version"]
        recom_dx_version = product_info["recom_dx_version"]
        size = product_info["size"]
        min_graphics_card = product_info["min_graphics_card"]
        recom_graphics_card = product_info["recom_graphics_card"]

        new_product = Product.objects.create(name=name, image=image, description=description, price=price, previous_price=previous_price, in_stock=in_stock, product_type=product_type)
        new_product.save()
        new_game = Game.objects.create(product=new_product, min_ram=min_ram, min_storage=min_storage, developers=developers, recom_ram=recom_ram, recom_storage=recom_storage, min_processor=min_processor, recom_processor=recom_processor, processor_type=processor_type, os_type=os_type, min_dx_version=min_dx_version, recom_dx_version=recom_dx_version, size=size, min_graphics_card=min_graphics_card, recom_graphics_card=recom_graphics_card)
        new_game.save()