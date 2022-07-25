import random, os, django, sys

sys.path.append("/home/egyptian-overlord/Documents/shoppa")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoppa.settings")
django.setup()


from products.models import PHONE_MANUFACTURER_CHOICES, PHONE_OS_CHOICES, PC_OS_CHOICES, PC_MANUFACTURER_CHOICES, GAME_OS_CHOICES, SIM_SLOT_CHOICES, NETWORK_CHOICES, Product, Phone
from products.scripts.add_items import generate_price, generate_text, get_bool, get_choice

image_list = [
"galaxy-tab-s6-lite.jpeg", "galaxy-tab-s6-lite-2022-lte-sm-p619-.jpeg", "huawei-enjoy-20e.jpeg", "huawei-enjoy-20-se.jpeg", "huawei-gt-runner.jpeg", "huawei-mate40-pro.jpeg", "huawei-mate-40.jpeg", "huawei-matepad-11-2021.jpeg", "huawei-matepad-104-2022.jpeg", "huawei-matepad-pro-108-2021-new.jpeg", "huawei-matepad-pro-126-2021-new.jpeg", "huawei-matepad-se.jpeg", "huawei-mate-x2-new.jpeg", "huawei-mate-xs-2.jpeg", "huawei-nova-8.jpeg", "huawei-nova-8-5g.jpeg", "huawei-nova-8i.jpeg", "huawei-nova-8-pro-5g.jpeg", "huawei-nova-8-se.jpeg", "huawei-nova-8-se-youth.jpeg", "huawei-nova-9-5g.jpeg", "huawei-nova-9-pro-5g-.jpeg", "huawei-nova-9-se.jpeg", "huawei-nova-y60.jpeg", "huawei-nova-y70-plus.jpeg", "huawei-p40-4g.jpeg", "huawei-p50.jpeg", "huawei-p50e.jpeg", "huawei-p50-pocket.jpeg", "huawei-p50-pro.jpeg", "infinix-hot9.jpeg", "infinix-hot9-play.jpeg", "infinix-hot9-pro.jpeg", "infinix-hot10.jpeg", "infinix-hot10-lite-.jpeg", "infinix-hot10-play.jpeg", "infinix-hot11.jpeg", "infinix-hot11-play.jpeg", "infinix-hot11s.jpeg", "infinix-hot12.jpeg", "infinix-hot-10i.jpeg", "infinix-hot-10s--.jpeg", "infinix-hot-10t-.jpeg", "infinix-hot-11-2022.jpeg", "infinix-hot-12i.jpeg", "infinix-note7.jpeg", "infinix-note7lite.jpeg", "infinix-note8-.jpeg", "infinix-note11.jpeg", "infinix-note12.jpeg", "infinix-note12-g96.jpeg", "infinix-note12i.jpeg", "infinix-note-8i-.jpeg", "infinix-note-10.jpeg", "infinix-note-10-pro-.jpeg", "infinix-note-11i.jpeg", "infinix-note-11-pro.jpeg", "infinix-note-11s.jpeg", "infinix-s5-lite-new.jpeg", "infinix-s5-pro-new.jpeg", "infinix-smart4-x653.jpeg", "infinix-smart5-.jpeg", "infinix-smart-5pro.jpeg", "infinix-smart-6.jpeg", "infinix-smart-6-hd.jpeg", "infinix-smart-hd-2021.jpeg", "infinix-zero8.jpeg", "infinix-zero-5g.jpeg", "infinix-zero-8i.jpeg", "infinix-zero-x-.jpeg", "infinix-zero-x-neo-.jpeg", "samsung-galaxy-a01.jpeg", "samsung-galaxy-a01core-sm-a013.jpeg", "samsung-galaxy-a02.jpeg", "samsung-galaxy-a2-core-sm-a260f.jpeg", "samsung-galaxy-a02s-sm-a025-new.jpeg", "samsung-galaxy-a03.jpeg", "samsung-galaxy-a03-core.jpeg", "samsung-galaxy-a03s.jpeg", "samsung-galaxy-a6s-.jpeg", "samsung-galaxy-a8s-.jpeg", "samsung-galaxy-a10.jpeg", "samsung-galaxy-a10e-sm-a102u.jpeg", "samsung-galaxy-a10s.jpeg", "samsung-galaxy-a11.jpeg", "samsung-galaxy-a12-nacho.jpeg", "samsung-galaxy-a12-sm-a125.jpeg", "samsung-galaxy-a13.jpeg", "samsung-galaxy-a13-5g-.jpeg", "samsung-galaxy-a20.jpeg", "samsung-galaxy-a20e.jpeg", "samsung-galaxy-a20s-sm-a207.jpeg", "samsung-galaxy-a21-r.jpeg", "samsung-galaxy-a21s-.jpeg", "samsung-galaxy-a22.jpeg", "samsung-galaxy-a22-5g.jpeg", "samsung-galaxy-a23.jpeg", "samsung-galaxy-a30.jpeg", "samsung-galaxy-a30s.jpeg", "samsung-galaxy-a31.jpeg", "samsung-galaxy-a32-4g-new.jpeg", "samsung-galaxy-a32-5g.jpeg", "samsung-galaxy-a33-5g.jpeg", "samsung-galaxy-a40.jpeg", "samsung-galaxy-a41.jpeg", "samsung-galaxy-a42-5g.jpeg", "samsung-galaxy-a50s.jpeg", "samsung-galaxy-a50-sm-a505f-ds.jpeg", "samsung-galaxy-a51-5g.jpeg", "samsung-galaxy-a51-5g-uw.jpeg", "samsung-galaxy-a51-sm-a515.jpeg", "samsung-galaxy-a52-4g.jpeg", "samsung-galaxy-a52-5g.jpeg", "samsung-galaxy-a52s-5g.jpeg", "samsung-galaxy-a53-5g-.jpeg", "samsung-galaxy-a60-.jpeg", "samsung-galaxy-a70.jpeg", "samsung-galaxy-a70s-.jpeg", "samsung-galaxy-a71.jpeg", "samsung-galaxy-a71-5g.jpeg", "samsung-galaxy-a71-5g-uw.jpeg", "samsung-galaxy-a72-4g.jpeg", "samsung-galaxy-a73-5g.jpeg", "samsung-galaxy-a80-.jpeg", "samsung-galaxy-a90-5g.jpeg", "samsung-galaxy-f02s.jpeg", "samsung-galaxy-f12.jpeg", "samsung-galaxy-f22.jpeg", "samsung-galaxy-f41-sm-f415fds.jpeg", "samsung-galaxy-f42-5g.jpeg", "samsung-galaxy-f52-5g.jpeg", "samsung-galaxy-f62.jpeg", "samsung-galaxy-fold.jpeg", "samsung-galaxy-fold-5g.jpeg", "samsung-galaxy-j2-core-2020.jpeg", "samsung-galaxy-m01.jpeg", "samsung-galaxy-m01s-m017f.jpeg", "samsung-galaxy-m02.jpeg", "samsung-galaxy-m02s.jpeg", "samsung-galaxy-m10-m105f.jpeg", "samsung-galaxy-m10s-m107f.jpeg", "samsung-galaxy-m11-sm-m115.jpeg", "samsung-galaxy-m12.jpeg", "samsung-galaxy-m13.jpeg", "samsung-galaxy-m20-m205f.jpeg", "samsung-galaxy-m21.jpeg", "samsung-galaxy-m21-2021.jpeg", "samsung-galaxy-m21s.jpeg", "samsung-galaxy-m22-.jpeg", "samsung-galaxy-m23.jpeg", "samsung-galaxy-m30-.jpeg", "samsung-galaxy-m30s-.jpeg", "samsung-galaxy-m31s.jpeg", "samsung-galaxy-m31-sm-m315f.jpeg", "samsung-galaxy-m32.jpeg", "samsung-galaxy-m32-5g-.jpeg", "samsung-galaxy-m32-5g-new.jpeg", "samsung-galaxy-m33.jpeg", "samsung-galaxy-m40-m405f.jpeg", "samsung-galaxy-m42.jpeg", "samsung-galaxy-m51.jpeg", "samsung-galaxy-m53-5g.jpeg", "samsung-galaxy-m62.jpeg", "samsung-galaxy-note10-.jpeg", "samsung-galaxy-note10-plus-.jpeg", "samsung-galaxy-note20-5g-r.jpeg", "samsung-galaxy-note20-ultra-.jpeg", "samsung-galaxy-quantum-2-sm-a826s.jpeg", "samsung-galaxy-s10.jpeg", "samsung-galaxy-s10-5g.jpeg", "samsung-galaxy-s10e.jpeg", "samsung-galaxy-s10-plus-new.jpeg", "samsung-galaxy-s20-.jpeg", "samsung-galaxy-s20-fe-4g.jpeg", "samsung-galaxy-s20-fe-5g.jpeg", "samsung-galaxy-s20-plus.jpeg", "samsung-galaxy-s20-ultra-.jpeg", "samsung-galaxy-s21-5g-r.jpeg", "samsung-galaxy-s21-fe-5g.jpeg", "samsung-galaxy-s21-plus-5g-.jpeg", "samsung-galaxy-s21-ultra-5g-.jpeg", "samsung-galaxy-s22-5g.jpeg", "samsung-galaxy-s22-plus-5g.jpeg", "samsung-galaxy-s22-ultra-5g.jpeg", "samsung-galaxy-tab-a7-104-2020.jpeg", "samsung-galaxy-tab-a7-lite.jpeg", "samsung-galaxy-tab-a8-105-2021-new.jpeg", "samsung-galaxy-tab-a-80-2019-r.jpeg", "samsung-galaxy-tab-a-84-2020.jpeg", "samsung-galaxy-tab-a-101-2019.jpeg", "samsung-galaxy-tab-a-105-.jpeg", "samsung-galaxy-tab-active3.jpeg", "samsung-galaxy-tab-active-pro-sm-t547.jpeg", "samsung-galaxy-tab-advanced2-sm-t583.jpeg", "samsung-galaxy-tab-a-s-pen-sm-p205.jpeg", "samsung-galaxy-taba-t387-sm-t387.jpeg", "samsung-galaxy-tab-s4-2018-r.jpeg", "samsung-galaxy-tab-s5e-sm-t725.jpeg", "samsung-galaxy-tab-s6.jpeg", "samsung-galaxy-tab-s6-5g-sm-t866n.jpeg", "samsung-galaxy-tab-s7-1.jpeg", "samsung-galaxy-tab-s7-fe.jpeg", "samsung-galaxy-tab-s7-plus1.jpeg", "samsung-galaxy-tab-s8.jpeg", "samsung-galaxy-tab-s8-plus.jpeg", "samsung-galaxy-tab-s8-ultra.jpeg", "samsung-galaxy-watch3.jpeg", "samsung-galaxy-watch4.jpeg", "samsung-galaxy-watch4-classic.jpeg", "samsung-galaxy-xcover-4s-sm-g398.jpeg", "samsung-galaxy-xcover-5.jpeg", "samsung-galaxy-xcover-fieldpro-sm-g889f.jpeg", "samsung-galaxy-xcover-pro-.jpeg", "samsung-galaxy-z-flip3-5g.jpeg", "samsung-galaxy-z-flip-01.jpeg", "samsung-galaxy-z-flip-5g-mystic-bronze.jpeg", "samsung-galaxy-z-fold2-5g.jpeg", "samsung-galaxy-z-fold3-5g.jpeg", "sasmung-galaxy-note10-lite-r.jpeg", "sasmung-galaxy-s10-lite-.jpeg", "s-l225.jpeg", "zero-x-series.jpeg"
]
used_images= []

def generate_phone_data(number_of_items):
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
                "category": "PHONE",
                "category_url": "phones",
                "ram": random.randrange(150),
                "storage": random.randrange(0, 200, 2),
                "manufacturer": get_choice(PHONE_MANUFACTURER_CHOICES),
                "model": generate_text([2, 10], 'words'),
                "weight": random.uniform(3, 100),
                "screen_size": random.uniform(3, 50),
                "resolution": generate_text([1, 4], 'words'),
                "os_type": get_choice(PHONE_OS_CHOICES),
                "os_version": random.uniform(2, 20),
                "cpu": generate_text([2, 12], 'words'),
                "gpu": generate_text([2, 12], 'words'),
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
        category = product_info["category"]
        category_url = product_info["category_url"]
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

        new_product = Product.objects.create(name=name, image=image, description=description, price=price, previous_price=previous_price, in_stock=in_stock, category=category, category_url=category_url)
        new_product.save()
        new_phone = Phone.objects.create(product=new_product, ram=ram, storage=storage, manufacturer=manufacturer, model=model, weight=weight, screen_size=screen_size, resolution=resolution, os_type=os_type, os_version=os_version, cpu=cpu, gpu=gpu, sim_slots=sim_slots, front_camera=front_camera, wifi=wifi, back_camera=back_camera, bluetooth=bluetooth, battery=battery, hotspot=hotspot, fingerprint=fingerprint, face_unlock=face_unlock, accelerometer=accelerometer, gyro=gyro, compass=compass, network=network, sd_card=sd_card, water_proof=water_proof, water_resistant=water_resistant, dust_resistant=dust_resistant)
        new_phone.save()

        print(new_product.id, new_phone.product.name)
        print(new_phone.manufacturer)

add_to_db(20)