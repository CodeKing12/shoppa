from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator
from vendors import models as acc_models
from django.utils.text import slugify

PHONE_MANUFACTURER_CHOICES = [
    ('SAMSUNG', 'SAMSUNG'),
    ('ACER', 'ACER'),
    ('ALCATEL', 'ALCATEL'),
    ('ALLVIEW', 'ALLVIEW'),
    ('AMAZON', 'AMAZON'),
    ('AMOI', 'AMOI'),
    ('APPLE', 'APPLE'),
    ('ARCHOS', 'ARCHOS'),
    ('ASUS', 'ASUS'),
    ('AT&T', 'AT&T'),
    ('BENEFON', 'BENEFON'),
    ('BENQ', 'BENQ'),
    ('BENQ-SIEMENS', 'BENQ-SIEMENS'),
    ('BIRD', 'BIRD'),
    ('BLACKBERRY', 'BLACKBERRY'),
    ('BLACKVIEW', 'BLACKVIEW'),
    ('BLU', 'BLU'),
    ('BOSCH', 'BOSCH'),
    ('BQ', 'BQ'),
    ('CASIO', 'CASIO'),
    ('CELKON', 'CELKON'),
    ('CHEA', 'CHEA'),
    ('COOLPAD', 'COOLPAD'),
    ('DELL', 'DELL'),
    ('EMPORIA', 'EMPORIA'),
    ('ENERGIZER', 'ENERGIZER'),
    ('ERICSSON', 'ERICSSON'),
    ('ETEN', 'ETEN'),
    ('FAIRPHONE', 'FAIRPHONE'),
    ('FUJITSU SIEMENS', 'FUJITSU SIEMENS'),
    ('GARMIN-ASUS', 'GARMIN-ASUS'),
    ('GIGABYTE', 'GIGABYTE'),
    ('GIONEE', 'GIONEE'),
    ('GOOGLE', 'GOOGLE'),
    ('HAIER', 'HAIER'),
    ('HONOR', 'HONOR'),
    ('HP', 'HP'),
    ('HTC', 'HTC'),
    ('HUAWEI', 'HUAWEI'),
    ('I-MATE', 'I-MATE'),
    ('I-MOBILE', 'I-MOBILE'),
    ('ICEMOBILE', 'ICEMOBILE'),
    ('INFINIX', 'INFINIX'),
    ('INNOSTREAM', 'INNOSTREAM'),
    ('INQ', 'INQ'),
    ('INTEX', 'INTEX'),
    ('JOLLA', 'JOLLA'),
    ('KARBONN', 'KARBONN'),
    ('KYOCERA', 'KYOCERA'),
    ('LAVA', 'LAVA'),
    ('LEECO', 'LEECO'),
    ('LENOVO', 'LENOVO'),
    ('LG', 'LG'),
    ('MAXON', 'MAXON'),
    ('MAXWEST', 'MAXWEST'),
    ('MEIZU', 'MEIZU'),
    ('MICROMAX', 'MICROMAX'),
    ('MICROSOFT', 'MICROSOFT'),
    ('MITAC', 'MITAC'),
    ('MITSUBISHI', 'MITSUBISHI'),
    ('MODU', 'MODU'),
    ('MOTOROLA', 'MOTOROLA'),
    ('MWG', 'MWG'),
    ('NEC', 'NEC'),
    ('NEONODE', 'NEONODE'),
    ('NIU', 'NIU'),
    ('NOKIA', 'NOKIA'),
    ('NVIDIA', 'NVIDIA'),
    ('O2', 'O2'),
    ('ONEPLUS', 'ONEPLUS'),
    ('OPPO', 'OPPO'),
    ('ORANGE', 'ORANGE'),
    ('PALM', 'PALM'),
    ('PANASONIC', 'PANASONIC'),
    ('PANTECH', 'PANTECH'),
    ('PARLA', 'PARLA'),
    ('PHILIPS', 'PHILIPS'),
    ('PLUM', 'PLUM'),
    ('POSH', 'POSH'),
    ('PRESTIGIO', 'PRESTIGIO'),
    ('QMOBILE', 'QMOBILE'),
    ('QTEK', 'QTEK'),
    ('RAZER', 'RAZER'),
    ('REALME', 'REALME'),
    ('SAGEM', 'SAGEM'),
    ('SENDO', 'SENDO'),
    ('SEWON', 'SEWON'),
    ('SHARP', 'SHARP'),
    ('SIEMENS', 'SIEMENS'),
    ('SONIM', 'SONIM'),
    ('SONY', 'SONY'),
    ('SONY ERICSSON', 'SONY ERICSSON'),
    ('SPICE', 'SPICE'),
    ('T-MOBILE', 'T-MOBILE'),
    ('TCL', 'TCL'),
    ('TECNO', 'TECNO'),
    ('TEL.ME.', 'TEL.ME.'),
    ('TELIT', 'TELIT'),
    ('THURAYA', 'THURAYA'),
    ('TOSHIBA', 'TOSHIBA'),
    ('ULEFONE', 'ULEFONE'),
    ('UNNECTO', 'UNNECTO'),
    ('VERTU', 'VERTU'),
    ('VERYKOOL', 'VERYKOOL'),
    ('VIVO', 'VIVO'),
    ('VK MOBILE', 'VK MOBILE'),
    ('VODAPHONE', 'VODAPHONE'),
    ('WIKO', 'WIKO'),
    ('WND', 'WND'),
    ('XCUTE', 'XCUTE'),
    ('XIAOMI', 'XIAOMI'),
    ('XOLO', 'XOLO'),
    ('YEZZ', 'YEZZ'),
    ('YOTA', 'YOTA'),
    ('YU', 'YU'),
    ('ZTE', 'ZTE'),
]

PHONE_OS_CHOICES = [
    ('Android', 'Android'),
    ('iOS', 'iOS'),
    ('Blackberry OS', 'Blackberry OS'),
    ('Windows OS', 'Windows OS'),
]

PC_OS_CHOICES = [
    ('Linux', 'Linux'),
    ('macOS', 'macOS'),
    ('Windows OS', 'Windows OS'),
]

PC_MANUFACTURER_CHOICES = [
    ('AORUS', 'AORUS'),
    ('HP', 'HP'),
    ('LENOVO', 'LENOVO'),
    ('MSI', 'MSI'),
    ('ASUS', 'ASUS'),
    ('DELL', 'DELL'),
    ('ACER', 'ACER'),
    ('GIGABYTE', 'GIGABYTE'),
    ('MICROSOFT', 'MICROSOFT'),
    ('ALIENWARE', 'ALIENWARE'),
    ('APPLE', 'APPLE'),
    ('RAZER', 'RAZER'),
    ('SAMSUNG', 'SAMSUNG'),
    ('LG', 'LG'),
    ('TOSHIBA', 'TOSHIBA'),
    ('FUJITSU', 'FUJITSU'),
    ('PANASONIC', 'PANASONIC'),
    ('HUAWEI', 'HUAWEI'),
    ('DYNABOOK', 'DYNABOOK'),
    ('LAPTOPMEDIA', 'LAPTOPMEDIA'),
    ('INFINIX', 'INFINIX'),
    ('XIAOMI', 'XIAOMI'),
    ('SONY', 'SONY'),
    ('TOSHIBA', 'TOSHIBA'),
    ('DURABOOK', 'DURABOOK'),
    ('GOOGLE', 'GOOGLE'),
    ('NOKIA', 'NOKIA'),
    ('VAIO', 'VAIO'),
    ('PACKARD BELL', 'PACKARD BELL'),
    ('MSi', 'MSi'),
    ('HYUNDAI TECHNOLOGY', 'HYUNDAI TECHNOLOGY'),
]

GAME_OS_CHOICES = [
    ('Linux', 'Linux'),
    ('macOS', 'macOS'),
    ('Windows 10', 'Windows 10'),
    ('Windows 7', 'Windows 7'),
    ('Windows 8', 'Windows 8'),
    ('Windows Vista', 'Windows Vista'),
]

SIM_SLOT_CHOICES =  [
    ('Single Sim', 'Single Sim'),
    ('Dual Sim', 'Dual Sim')
]

NETWORK_CHOICES = [
    ('2G', '2G'),
    ('3G', '3G'),
    ('4G', '4G'),
    ('5G', '5G')
]

HARD_DISK_CHOICES = [
    ('SSD', 'SSD'),
    ('HDD', 'HDD')
]

PROCESSOR_TYPE_CHOICES = [
    ('64-Bit', '64-Bit'),
    ('32-Bit', '32-Bit')
]

class Product(models.Model):
    name = models.CharField(max_length=250, help_text="Name of Product")
    image = models.ImageField(upload_to="products_images/", blank=True)
    description = RichTextUploadingField()
    price = models.PositiveIntegerField()
    previous_price = models.PositiveIntegerField(blank=True, default=0)
    percent_off = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    slug = models.SlugField(auto_created=True, blank=True, max_length=300)
    PHONE = 'PHONE'
    PC = 'PC'
    REFURBISHED = 'REFURBISHED'
    ACCESSORIES = 'ACCESSORY'
    APPLIANCES = 'APPLIANCE'
    GAMES = 'GAME'

    PRODUCT_CHOICES = [
        (PHONE, 'PHONE'),
        (PC, 'LAPTOP'),
        (REFURBISHED, 'REFURBISHED PRODUCT'),
        (ACCESSORIES, 'TECH ACCESSORY'),
        (APPLIANCES, 'OFFICE APPLIANCE'),
        (GAMES, 'VIDEO GAME'),
    ]
    category = models.CharField(max_length=100, choices=PRODUCT_CHOICES)
    
    # Add the stars and reviews
    is_cleaned = False
    
    def __str__(self):
        return self.name

    def clean(self):
        self.is_cleaned = True

        if self.previous_price > 0 and self.previous_price < self.price:
            self.percent_off = int((self.price / self.previous_price) * 100)
        else:
            self.percent_off = 0
        
        folder = ""
        image_url = ""
        if self.category == 'PHONE': 
            folder = "phone_products"
        elif self.category == 'LAPTOP':
            folder = "laptop_products"
        elif self.category == 'REFURBISHED PRODUCT':
            folder = "refurbished_products"
        elif self.category == 'TECH ACCESSORY':
            folder = "accessory_products"
        elif self.category == 'OFFICE APPLIANCE':
            folder = "appliance_products"
        elif self.category == 'VIDEO GAME':
            folder = "game_products"
        else:
            raise ValueError

        if folder not in image_url:
            image_url = self.image.url
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
    front_camera = models.IntegerField() # Measured in MP
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

class Game(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name="game_info")
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

    # Look for how to do a multiselect field for model choices like the processor type, os_type

class MoreProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='all_product_images')

class ProductReviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = RichTextUploadingField()

# Allow vendors to schedule products

# Create new models and make all the choice fields to be one-to-many fields so that it will be more dynamic