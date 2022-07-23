from django_seed import Seed
from django.core.files import File
import os, django, sys

sys.path.append("/home/egyptian-overlord/Documents/shoppa")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoppa.settings")
django.setup()

from django.contrib.contenttypes.models import ContentType
from shoppa.settings import BASE_DIR
from products.models import GameGenres, Product, PC, Game, Phone

def run_me(model):
    all_products = model.objects.all()
    # for product in all_products:
        # print(product)
        # pass
    
    the_p = all_products[11]
    print(the_p.name, the_p.image)
    file_path = 'media/products_images/laptop_products/'
    file_name = 'c08238459.png'
    the_file = file_path + file_name
    content = File(open(BASE_DIR / the_file, 'rb'))
    the_p.image.save(file_name, content, save=True)
    print(the_p.image)


# run_me(Product)
# print(help(Product))
game_content_type = ContentType.objects.get(app_label="products", model="game")

# print(ContentType.objects.get(app_label="products", model="pc").id)

seeder = Seed.seeder(locale="en_GB")
seeder.add_entity(Product, 10, {
    "content_type": game_content_type,
    "category": "PC"
})
seeder.add_entity(GameGenres, 5)
seeder.add_entity(Game, 5)

inserted_pks = seeder.execute()
print(inserted_pks)
