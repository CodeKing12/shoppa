from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.conf import settings
from colorfield.fields import ColorField
from django.core.validators import RegexValidator

from products.models import Product

# Remember to remove the blank=true from important model fields before you go live

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart_products = models.ManyToManyField("products.Product", blank=True, through='CartDetails')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.user.first_name + "'s Cart"

class CartDetails(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField(blank=True)
    color = ColorField(default="#ffffff", blank=True)
    def __str__(self):
        return self.cart.user.first_name + "'s Cart"

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wish_products = models.ManyToManyField(Product, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return self.user.first_name + "'s Wishlist"

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, phone_number, **extra_fields):
        if not email:
            return ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_apiuser', True)
        extra_fields.setdefault('is_vendor', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        if extra_fields.get('is_apiuser') is not True:
            raise ValueError(('Superuser must have is_apiuser=True.'))
        if extra_fields.get('is_vendor') is not True:
            raise ValueError(('Superuser must have is_vendor=True.'))

        return self.create_user(first_name=first_name, last_name=last_name, email=email, password=password, phone_number=phone_number, **extra_fields)
    
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# class PhoneBook(models.Model):
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_numbers = models.CharField(validators=[phone_regex], max_length=17, blank=True)

# class AddressBook(models.Model):
#     address = models.CharField(max_length=250)

class CustomAccount(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=70, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # phone_number = models.ForeignKey(PhoneBook, on_delete=models.CASCADE, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=250, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_apiuser = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    def get_full_name(self):
        return "%s %s"%(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

class ApiUser(models.Model):
    user = models.OneToOneField(CustomAccount, on_delete=models.CASCADE)
    product_groups = models.JSONField()

    def save(self, *args, **kwargs):
        if self.user.is_apiuser != True:
            raise ValueError
        super(ApiUser, self).save(*args, **kwargs)