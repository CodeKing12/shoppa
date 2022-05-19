import random
from products.models import PHONE_MANUFACTURER_CHOICES, PHONE_OS_CHOICES, PC_OS_CHOICES, PC_MANUFACTURER_CHOICES, GAME_OS_CHOICES, SIM_SLOT_CHOICES, NETWORK_CHOICES, Product, Phone
from .add_items import generate_price, generate_text, get_bool, get_choice

def generate_phone_data(number_of_items):
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
                "product_type": "PHONE",
                "ram": random.randrange(150),
                "storage": random.randrange(0, 200, 2),
                "manufacturer": get_choice(PHONE_MANUFACTURER_CHOICES),
                "model": "",
                "weight": random.random(random.randrange(3, 100)),
                "screen_size": random.random(random.randrange(3, 50)),
                "resolution": "",
                "os_type": get_choice(PHONE_OS_CHOICES),
                "os_version": "",
                "cpu": "",
                "gpu": "",
                "sim_slots": get_choice(SIM_SLOT_CHOICES),
                "front_camera": random.randrange(10, 100, 5),
                "back_camera": random.randrange(12, 156, 4),
                "battery": random.randrange(500, 10000, 500),
                "wifi": get_bool(),
                "bluetooth": get_bool(),
                "hotspot": get_bool(),
                "fingerprint": get_bool(),
                "face_unlock": get_bool(),
                "accelerometer": get_bool(),
                "gyro": get_bool(),
                "compass": get_bool(),
                "network": get_choice(NETWORK_CHOICES),
                "sd_card": get_bool(),
                "water_proof": get_bool(),
                "water_resistant": get_bool(),
                "dust_resistant": get_bool(),
            }
        )

    return generated_info


def add_to_db(number_of_items):
    all_generated_info = generate_phone_data(number_of_items)

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
        gpu = product_info["gpu"]
        sim_slots = product_info["sim_slots"]
        front_camera = product_info["front_camera"]
        back_camera = product_info["back_camera"]
        battery = product_info["battery"]
        wifi = product_info["wifi"]
        bluetooth = product_info["bluetooth"]
        hotspot = product_info["hotspot"]
        fingerprint = product_info["fingerprint"]
        face_unlock = product_info["face_unlock"]
        accelerometer = product_info["accelerometer"]
        gyro = product_info["gyro"]
        compass = product_info["compass"]
        network = product_info["network"]
        sd_card = product_info["sd_card"]
        water_proof = product_info["water_proof"]
        water_resistant = product_info["water_resistant"]
        dust_resistant = product_info["dust_resistant"]

        new_product = Product.objects.create(name=name, image=image, description=description, price=price, previous_price=previous_price, in_stock=in_stock, product_type=product_type)
        new_product.save()
        new_phone = Phone.objects.create(product=new_product, ram=ram, storage=storage, manufacturer=manufacturer, model=model, weight=weight, screen_size=screen_size, resolution=resolution, os_type=os_type, os_version=os_version, cpu=cpu, gpu=gpu, sim_slots=sim_slots, front_camera=front_camera, wifi=wifi, back_camera=back_camera, bluetooth=bluetooth, battery=battery, hotspot=hotspot, fingerprint=fingerprint, face_unlock=face_unlock, accelerometer=accelerometer, gyro=gyro, compass=compass, network=network, sd_card=sd_card, water_proof=water_proof, water_resistant=water_resistant, dust_resistant=dust_resistant)
        new_phone.save()
