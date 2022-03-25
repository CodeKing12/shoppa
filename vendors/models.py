from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator

# Create your models here.
class VendorAccount(models.Model):
    owner_first_name = models.CharField(max_length=100)
    owner_middle_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner_dob = models.DateTimeField()
    owner_id = models.ImageField(upload_to='vendors_id')
    owner_image = models.ImageField(upload_to='vendors_images')
    cac_reg_num = models.IntegerField() # Providing this speeds up verification
    tax_id_num = models.IntegerField(blank=True) # Required
    nin = models.IntegerField() # Optional but speeds up registration
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=70, null=True, blank=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=400)
    date_joined = models.DateTimeField(default=timezone.now)
    business_name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=200)
    business_description = models.TextField(max_length=160)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True) 
    whatsapp_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    company_start_date = models.DateTimeField()
    amount_made = models.IntegerField()
    orders_completed = models.IntegerField()
    products_in_stock = models.IntegerField()

    def __str__(self):
        return self.business_name

class VendorReviews(models.Model):
    vendor = models.ForeignKey(VendorAccount, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = models.TextField(max_length=200)

class VendorMessages(models.Model):
    vendor = models.ForeignKey(VendorAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    message = models.TextField(max_length=200)
    # Take email, phone_number, first and last name from user details