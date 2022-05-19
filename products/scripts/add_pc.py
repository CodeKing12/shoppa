import random
from products.models import HARD_DISK_CHOICES, PC_OS_CHOICES, PC_MANUFACTURER_CHOICES, PROCESSOR_TYPE_CHOICES, NETWORK_CHOICES, Product, PC
from .add_items import generate_price, generate_text, get_bool, get_choice

# Let all other values like weight, faceunlock, accelerometer, be generated on the spot so they can be different

def generate_pc_data(number_of_items):
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
                "product_type": "PC",
                "ram": random.randrange(500),
                "storage": random.randrange(100, 2000, 50),
                "manufacturer": get_choice(PC_MANUFACTURER_CHOICES),
                "model": "",
                "weight": random.random(random.randrange(100, 500)),
                "screen_size": random.random(random.randrange(50, 200, 2)),
                "resolution": "",
                "os_type": get_choice(PC_OS_CHOICES),
                "os_version": "",
                "cpu": "",
                "graphics_card": "",
                "hard_disk": get_choice(HARD_DISK_CHOICES),
                "motherboard": "",
                "battery": random.randrange(2500, 50000, 500),
                "wifi": get_bool(),
                "bluetooth": get_bool(),
                "hotspot": get_bool(),
                "fingerprint": get_bool(),
                "face_unlock": get_bool(),
                "processor": get_bool(),
                "processor_type": get_choice(PROCESSOR_TYPE_CHOICES),
                "network": get_choice(NETWORK_CHOICES),
                "sd_card": get_bool(),
                "water_proof": get_bool(),
                "water_resistant": get_bool(),
                "dust_resistant": get_bool(),
            }
        )
    return generated_info


def add_to_db(number_of_items):
    all_generated_info = generate_pc_data(number_of_items)

    for product_info in all_generated_info:
        name = product_info["name"]
        image = product_info["image"]
        description = product_info["description"]
        price = product_info["price"]
        previous_price = product_info["previous_price"]
        in_stock = product_info["in_stock"]
        product_type = product_info["product_type"]
        ram = product_info["ram"]
        storage = product_info["storage"]
        manufacturer = product_info["manufacturer"]
        model = product_info["model"]
        weight = product_info["weight"]
        screen_size = product_info["screen_size"]
        resolution = product_info["resolution"]
        os_type = product_info["os_type"]
        os_version = product_info["os_version"]
        cpu = product_info["cpu"]
        graphics_card = product_info["graphics_card"]
        hard_disk = product_info["hard_disk"]
        motherboard = product_info["motherboard"]
        battery = product_info["battery"]
        wifi = product_info["wifi"]
        bluetooth = product_info["bluetooth"]
        hotspot = product_info["hotspot"]
        fingerprint = product_info["fingerprint"]
        face_unlock = product_info["face_unlock"]
        processor = product_info["processor"]
        processor_type = product_info["processor_type"]
        network = product_info["network"]
        sd_card = product_info["sd_card"]
        water_proof = product_info["water_proof"]
        water_resistant = product_info["water_resistant"]
        dust_resistant = product_info["dust_resistant"]

        new_product = Product.objects.create(name=name, image=image, description=description, price=price, previous_price=previous_price, in_stock=in_stock, product_type=product_type)
        new_product.save()
        new_pc = PC.objects.create(product=new_product, ram=ram, storage=storage, manufacturer=manufacturer, model=model, weight=weight, screen_size=screen_size, resolution=resolution, os_type=os_type, os_version=os_version, cpu=cpu, graphics_card=graphics_card, hard_disk=hard_disk, motherboard=motherboard, wifi=wifi, processor=processor, bluetooth=bluetooth, battery=battery, hotspot=hotspot, fingerprint=fingerprint, face_unlock=face_unlock, processor_type=processor_type, network=network, sd_card=sd_card, water_proof=water_proof, water_resistant=water_resistant, dust_resistant=dust_resistant)
        new_pc.save()