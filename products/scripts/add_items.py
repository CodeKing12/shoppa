import random
from products.models import PHONE_MANUFACTURER_CHOICES, PHONE_OS_CHOICES, PC_OS_CHOICES, PC_MANUFACTURER_CHOICES, GAME_OS_CHOICES

def generate_price(device):
    if device == "phone":
        start = 20000
        end = 200000
        step = 2000
    elif device == "pc":
        start = 50000
        end = 500000
        step = 5000
    elif device == "accessory":
        start = 1000
        end = 100000
        step = 500
    else:
        start = 30000
        end = 700000
        step = 4000
    price = random.randrange(start, end, step)
    determine_previous = random.choice([True, False])
    if determine_previous == True:
        previous_price = random.randrange(price, price*1.5, step)
    else:
        previous_price = 0

    return price, previous_price

def is_in_stock():
    return random.choice([True, False])

def generate_description():
    length = random.randrange(300, 1000)

def get_manufacturer(device):
    if device == "phone":
        choice_list = PHONE_MANUFACTURER_CHOICES
    elif device == 'pc':
        choice_list = PC_MANUFACTURER_CHOICES
    else:
        choice_list = ["No Manufacturer"]
    choice_tuple = random.choice(choice_list)
    return choice_tuple[0]

def get_os(device):
    if device == "phone":
        choice_list = PHONE_OS_CHOICES
    elif device == 'pc':
        choice_list = PC_OS_CHOICES
    elif device == 'game':
        choice_list = GAME_OS_CHOICES
    else:
        choice_list = ["No Operating System Installed"]
    choice_tuple = random.choice(choice_list)
    return choice_tuple[0]