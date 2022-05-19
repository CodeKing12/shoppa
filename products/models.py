from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator
from vendors import models as acc_models

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    description = RichTextUploadingField()
    price = models.PositiveIntegerField()
    previous_price = models.PositiveIntegerField(blank=True, default=0)
    percent_off = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    PHONE = 'PHONE'
    LAPTOP = 'LAPTOP'
    REFURBISHED = 'REFURBISHED'
    ACCESSORIES = 'ACCESSORIES'
    APPLIANCES = 'APPLIANCES'
    GAMES = 'GAMES'

    PRODUCT_CHOICES = [
        (PHONE, 'PHONES'),
        (LAPTOP, 'LAPTOPS'),
        (REFURBISHED, 'REFURBISHED GOODS'),
        (ACCESSORIES, 'TECH ACCESSORIES'),
        (APPLIANCES, 'OFFICE APPLIANCES'),
        (GAMES, 'VIDEO GAMES'),
    ]
    product_type = models.CharField(max_length=100, choices=PRODUCT_CHOICES)
    # Add the stars and reviews

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.percent_off = int((self.previous_price / self.price) * 100)
        super(Product, self).save(*args, **kwargs)

class Phone(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name="phone_info")
    ram = models.IntegerField()
    storage = models.IntegerField()
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
    manufacturer = models.CharField(max_length=60, choices=PHONE_MANUFACTURER_CHOICES, default='SAMSUNG')
    model = models.CharField(max_length=100)
    weight = models.CharField(max_length=40) # Measured in grams
    screen_size = models.FloatField() # Measured  in inches
    resolution = models.CharField(max_length=40) # Measured in pixels
    PHONE_OS_CHOICES = [
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('Blackberry OS', 'Blackberry OS'),
        ('Windows OS', 'Windows OS'),
    ]
    os_type = models.CharField(max_length=50, choices=PHONE_OS_CHOICES)
    os_version = models.FloatField()
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    sim_slots = models.CharField(max_length=50, choices = [
        ('Single Sim', 'Single Sim'),
        ('Dual Sim', 'Dual Sim')
    ])
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
    network = models.CharField(max_length=10, choices = [
        ('2G', '2G'),
        ('3G', '3G'),
        ('4G', '4G'),
        ('5G', '5G'),
    ])
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
    manufacturer = models.CharField(max_length=60, choices=PC_MANUFACTURER_CHOICES, default='SAMSUNG')
    model = models.CharField(max_length=100)
    graphics_card = models.CharField(max_length=150)
    hard_disk = models.CharField(max_length=25, choices=[
        ('SSD', 'SSD'),
        ('HDD', 'HDD')
    ])
    weight = models.CharField(max_length=40) # Measured in grams
    screen_size = models.FloatField() # Measured  in inches
    resolution = models.CharField(max_length=40) # Measured in pixels
    PC_OS_CHOICES = [
        ('Linux', 'Linux'),
        ('macOS', 'macOS'),
        ('Windows OS', 'Windows OS'),
    ]
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
    processor_type = models.CharField(max_length=20, choices=[
        ('64-Bit', '64-Bit'),
        ('32-Bit', '32-Bit')
    ])
    network = models.CharField(max_length=10, choices = [
        ('2G', '2G'),
        ('3G', '3G'),
        ('4G', '4G'),
        ('5G', '5G'),
    ])
    sd_card_slot = models.BooleanField()
    water_proof = models.BooleanField()
    water_resistant = models.BooleanField()
    dust_resistant = models.BooleanField()

    def __str__(self):
        return self.product.name

class Game(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name="game_info")
    min_ram = models.IntegerField()
    recom_ram = models.IntegerField()
    min_processor = models.CharField(max_length=100)
    recom_processor = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=20, choices=[
        ('64-Bit', '64-Bit'),
        ('32-Bit', '32-Bit')
    ])
    min_storage = models.IntegerField()
    recom_storage = models.IntegerField()
    GAME_OS_CHOICES = [
        ('Linux', 'Linux'),
        ('macOS', 'macOS'),
        ('Windows 10', 'Windows 10'),
        ('Windows 7', 'Windows 7'),
        ('Windows 8', 'Windows 8'),
        ('Windows Vista', 'Windows Vista'),
    ]
    os_type = models.CharField(max_length=50, choices=GAME_OS_CHOICES)
    min_dx_version = models.IntegerField()
    recom_dx_version = models.IntegerField()
    size = models.IntegerField()

    # Look for how to do a multiselect field for model choices like the processor type, os_type

class MoreProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='all_product_images')

class ProductReviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = RichTextUploadingField()

# Allow vendors to schedule products