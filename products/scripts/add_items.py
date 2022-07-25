import random
from lorem_text import lorem

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

def get_bool():
    return random.choice([True, False])

def generate_text(length, type):
    if isinstance(length, list):
        the_length = random.randrange(length[0], length[1])
    else:
        the_length = length

    if type == 'words':
        text = lorem.words(the_length)
    elif type == 'sentences':
        text = lorem.sentence(the_length)
    elif type == 'paragraphs':
        text = lorem.paragraphs(the_length)
    else:
        text = 'Invalid Input for Type'
    
    return text

def get_choice(choice_list):
    choice_tuple = random.choice(choice_list)
    return choice_tuple[0]

def random_foreign(model):
    total_objects = model.objects.all().count()
    rand_obj_id = random.randrange(1, total_objects+1)
    return model.objects.get(id=rand_obj_id)

# Let all other values like weight, faceunlock, accelerometer, be generated on the spot so they can be different
