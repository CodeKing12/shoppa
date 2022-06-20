import random
from ..models import HARD_DISK_CHOICES, PC_OS_CHOICES, PC_MANUFACTURER_CHOICES, PROCESSOR_TYPE_CHOICES, NETWORK_CHOICES, Product, PC
from .add_items import generate_price, generate_text, get_bool, get_choice

image_list = ["c06545784.png", "c06545809.png", "c06565650.png", "c06586688.png", "c06612716.png", "c06622124.png", "c06642041.png", "c06724597.png", "c06753948.png", "c06754480.png", "c06887069.png", "c06972410.png", "c06986556.png", "c07046186.png", "c07047495.png", "c07047522.png", "c07263741.png", "c07581462.png", "c07607047.png", "c07846831.png", "c07847061.png", "c07847242.png", "c07920755.png", "c07920814.png", "c07920872.png", "c07921067.png", "c07921096.png", "c07922556.png", "c07951380.png", "c07960791.png", "c07963500.png", "c07964700.png", "c07965315.png", "c07965818.png", "c07965873.png", "c07966511.png", "c07966541.png", "c07968249.png", "c07968624.png", "c07968696.png", "c07969313.png", "c07973207.png", "c07973455.png", "c07973484.png", "c07973596.png", "c07974013.png", "c07974881.png", "c07975141.png", "c07975509.png", "c07978875.png", "c07983015.png", "c07983989.png", "c07984278.png", "c07984316.png", "c07984345.png", "c07994844.png", "c07999602.png", "c07999631.png", "c07999660.png", "c08000638.png", "c08001685.png", "c08001745.png", "c08049850.png", "c08049879.png", "c08049914.png", "c08049943.png", "c08049972.png", "c08065836.png", "c08065880.png", "c08065929.png", "c08175554.png", "c08175612.png", "c08194265.png", "c08194294.png", "c08194323.png", "c08216704.png", "c08238459.png", "center_facing.png", "center_facing2.png", "center_facing3.png", "center_facing4.png", "center_facing5.png", "center_facing6.png", "center_facing1.png"]
used_images = []
 # Let all other values like weight, faceunlock, accelerometer, be generated on the spot so they can be different

def generate_pc_data(number_of_items):
    generated_info =  []
    for number in range(number_of_items):
        unique_image = False
        while unique_image == False:
            image = random.choice(image_list)
            if image not in used_images:
                used_images.append(image)
                unique = True
                break
        price, previous_price = generate_price('phone')
        generated_info.append(
            {
                "name": generate_text([2, 20], 'words'),
                "image": image,
                "description": generate_text([2, 6], 'paragraphs'),
                "price": price,
                "previous_price": previous_price, # Check how invidivually access each variable in the return statement
                "in_stock": get_bool(),
                "product_type": "LAPTOP",
                "ram": random.randrange(500),
                "storage": random.randrange(100, 2000, 50),
                "manufacturer": get_choice(PC_MANUFACTURER_CHOICES),
                "model": generate_text([2, 10], 'words'),
                "weight": random.uniform(100, 500),
                "screen_size": random.uniform(50, 200),
                "resolution": generate_text([1, 4], 'words'),
                "os_type": get_choice(PC_OS_CHOICES),
                "os_version": random.randrange(2, 20),
                "cpu": generate_text([2, 12], 'words'),
                "graphics_card": generate_text([2, 14], 'words'),
                "hard_disk": get_choice(HARD_DISK_CHOICES),
                "motherboard": generate_text([2, 12], 'words'),
                "battery": random.randrange(2500, 50000, 500),
                "wifi": get_bool(),
                "bluetooth": get_bool(),
                "hotspot": get_bool(),
                "fingerprint": get_bool(),
                "face_unlock": get_bool(),
                "processor": generate_text([2, 10], 'words'),
                "processor_type": get_choice(PROCESSOR_TYPE_CHOICES),
                "network": get_choice(NETWORK_CHOICES),
                "sd_card_slot": get_bool(),
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
        sd_card_slot = product_info["sd_card_slot"]
        water_proof = product_info["water_proof"]
        water_resistant = product_info["water_resistant"]
        dust_resistant = product_info["dust_resistant"]

        new_product = Product.objects.create(name=name, image=image, description=description, price=price, previous_price=previous_price, in_stock=in_stock, product_type=product_type)
        new_product.save()
        new_pc = PC.objects.create(product=new_product, ram=ram, storage=storage, manufacturer=manufacturer, model=model, weight=weight, screen_size=screen_size, resolution=resolution, os_type=os_type, os_version=os_version, cpu=cpu, graphics_card=graphics_card, hard_disk=hard_disk, motherboard=motherboard, wifi=wifi, processor=processor, bluetooth=bluetooth, battery=battery, hotspot=hotspot, fingerprint=fingerprint, face_unlock=face_unlock, processor_type=processor_type, network=network, sd_card_slot=sd_card_slot, water_proof=water_proof, water_resistant=water_resistant, dust_resistant=dust_resistant)
        new_pc.save()

add_to_db(10)