from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from .model_choices import PROCESSOR_TYPE_CHOICES, PC_MANUFACTURER_CHOICES, PHONE_OS_CHOICES, PHONE_MANUFACTURER_CHOICES, PC_OS_CHOICES, GAME_OS_CHOICES, HARD_DISK_CHOICES, SIM_SLOT_CHOICES, PRODUCT_CHOICES, NETWORK_CHOICES
from .model_choices import PC as laptop_choice
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone

# class Category(models.Model):
#     name = models.CharField(max_length=200)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # details = GenericForeignKey("content_type", "object_id")

    # class Meta:
    #     indexes = [
    #         models.Index(fields=["content_type", "object_id"])
    #     ]

# default_content_type = ContentType.objects.get(app_label="products", model="pc")

class GameGenres(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, help_text="Name of Product")
    image = models.ImageField(upload_to="products_images/", blank=True)
    description = RichTextUploadingField()
    price = models.PositiveIntegerField()
    previous_price = models.PositiveIntegerField(blank=True, default=0)
    percent_off = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    slug = models.SlugField(auto_created=True, blank=True, max_length=300)
    category = models.CharField(max_length=100, choices=PRODUCT_CHOICES, default=laptop_choice)
    category_url = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=8)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    details = GenericForeignKey("content_type", "object_id")
    
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"])
        ]
    
    def get_absolute_url(self):
        return reverse("product-details", kwargs={"category_url": self.category_url, "slug": self.slug})

    # You can add details about the model field using the id (See your screenshots for the terminal example)
    # You can also add the details object directly using product.details = <object>
    # You can also add details by getting the content_type and then getting the object using the object id as an attribute in the get_object_for_this_type method
    
    # Add the stars and reviews
    is_cleaned = False
    
    def __str__(self):
        return self.name

    def clean(self):
        self.is_cleaned = True

        if self.previous_price > 0 and self.previous_price > self.price:
            self.percent_off = 100 - int((self.price / self.previous_price) * 100)
        else:
            self.percent_off = 0
        
        folder = ""
        image_url = ""
        if self.category == 'PHONE': 
            folder = "phone_products"
            self.category_url = "phones"

        elif self.category == 'PC':
            folder = "laptop_products"
            self.category_url = "laptops"

        elif self.category == 'REFURBISHED':
            folder = "refurbished_products"
            self.category_url = "refurbished"

        elif self.category == 'ACCESSORY':
            folder = "accessory_products"
            self.category_url = "accessories"

        elif self.category == 'APPLIANCE':
            folder = "appliance_products"
            self.category_url = "appliances"

        elif self.category == 'GAME':
            folder = "game_products"
            self.category_url = "games"

        else:
            raise ValueError

        image_url = self.image.url
        if folder not in image_url:
            if 'products_images' not in image_url:
                folder = 'products_images/' + folder
            folders_list = image_url.split('/')
            media_index = folders_list.index('media')
            folders_list[media_index] =  folder
            self.image = '/'.join(folders_list)

        self.slug = slugify(self.name)
        # self.category_slug = slugify(self.)

        super(Product, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.clean()
        self.object_id = self.id
        super(Product, self).save(*args, **kwargs)

class Phone(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name="phone_info")
    ram = models.IntegerField()
    storage = models.IntegerField()
    manufacturer = models.CharField(max_length=60, choices=PHONE_MANUFACTURER_CHOICES, default='SAMSUNG')
    model = models.CharField(max_length=100)
    weight = models.FloatField() # Measured in grams
    screen_size = models.FloatField() # Measured  in inches
    resolution = models.CharField(max_length=40) # Measured in pixels
    os_type = models.CharField(max_length=50, choices=PHONE_OS_CHOICES)
    os_version = models.FloatField()
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    sim_slots = models.CharField(max_length=50, choices=SIM_SLOT_CHOICES)
    front_camera = models.IntegerField() # Measured in MegaPixels (MP)
    back_camera = models.IntegerField() # Measured in MP
    battery = models.IntegerField() # Measured in mAh
    # colors = models.CharField(max_length=6)
    bluetooth = models.BooleanField()
    wifi = models.BooleanField()
    hotspot = models.BooleanField()
    fingerprint = models.BooleanField()
    face_unlock = models.BooleanField()
    accelerometer = models.BooleanField()
    gyro = models.BooleanField()
    compass = models.BooleanField()
    network = models.CharField(max_length=10, choices=NETWORK_CHOICES)
    sd_card = models.BooleanField()
    water_proof = models.BooleanField()
    water_resistant = models.BooleanField()
    dust_resistant = models.BooleanField()

    def __str__(self):
        return self.product.name

    # def save(self, *args, **kwargs):
    #     super(Product, self).save(*args, **kwargs)

class PC(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name="pc_info")
    ram = models.IntegerField()
    storage = models.IntegerField()
    manufacturer = models.CharField(max_length=60, choices=PC_MANUFACTURER_CHOICES, default='SAMSUNG')
    model = models.CharField(max_length=100)
    graphics_card = models.CharField(max_length=150)
    hard_disk = models.CharField(max_length=25, choices=HARD_DISK_CHOICES)
    weight = models.CharField(max_length=40) # Measured in grams
    screen_size = models.FloatField() # Measured  in inches
    resolution = models.CharField(max_length=40) # Measured in pixels
    os_type = models.CharField(max_length=50, choices=PC_OS_CHOICES)
    os_version = models.FloatField()
    cpu = models.CharField(max_length=120)
    motherboard = models.CharField(max_length=120)
    battery = models.IntegerField() # Measured in mAh
    # colors = models.CharField(max_length=6)
    bluetooth = models.BooleanField()
    wifi = models.BooleanField()
    hotspot = models.BooleanField()
    fingerprint = models.BooleanField()
    face_unlock = models.BooleanField()
    processor = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=20, choices=PROCESSOR_TYPE_CHOICES)
    network = models.CharField(max_length=10, choices=NETWORK_CHOICES)
    sd_card_slot = models.BooleanField()
    water_proof = models.BooleanField()
    water_resistant = models.BooleanField()
    dust_resistant = models.BooleanField()

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.content_type = ContentType.objects.get(app_label='products', model='pc')
        self.product.object_id = self.product.id
        self.product.details = self
        super(PC, self).save(*args, **kwargs)

class Game(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name="game_info")
    genre = models.ForeignKey(GameGenres, on_delete=models.CASCADE)
    min_ram = models.IntegerField()
    developers = models.CharField(max_length=80)
    recom_ram = models.IntegerField()
    min_processor = models.CharField(max_length=100)
    recom_processor = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=20, choices=PROCESSOR_TYPE_CHOICES)
    min_storage = models.IntegerField()
    recom_storage = models.IntegerField()
    os_type = models.CharField(max_length=50, choices=GAME_OS_CHOICES)
    min_dx_version = models.IntegerField()
    recom_dx_version = models.IntegerField()
    size = models.IntegerField()
    min_graphics_card = models.CharField(max_length=130)
    recom_graphics_card = models.CharField(max_length=130)

    def save(self, *args, **kwargs):
        self.product.content_type = ContentType.objects.get(app_label='products', model='game')
        self.product.object_id = self.product.id
        self.product.details = self
        super(Game, self).save(*args, **kwargs)

    # Look for how to do a multiselect field for model choices like the processor type, os_type

class MoreProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='all_product_images')

class ProductReviews(models.Model):
    reviewer = models.ForeignKey("accounts.CustomAccount", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    date_submitted = models.DateTimeField(default=timezone.now)
    review_title = models.CharField(max_length=150)
    review = RichTextUploadingField()

# Allow vendors to schedule products

# Create new models and make all the choice fields to be one-to-many fields so that it will be more dynamic