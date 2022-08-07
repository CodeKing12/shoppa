from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.conf import settings
from colorfield.fields import ColorField
from django.core.validators import RegexValidator
import secrets, string, random

from products.models import Product

ORDER_STATUS_CHOICES = [
    ("Delivered", "Completed"),
    ("In Progress", "In Progress"),
    ("Delayed", "Delayed"),
    ("Cancelled", "Cancelled")
]

TICKET_TYPE_CHOICES = [
    ("Website Issues", "Website Issues"),
    ("Complaint", "Complaint"),
    ("Inquiry", "Inquiry"),
    ("Order Issues", "Order Issues"),
]

TICKET_PRIORITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    ("Urgent", "Urgent"),
]

TICKET_STATUS_CHOICES = [
    ("Open", "Open"),
    ("Closed", "Closed")
]

def alpha_numeric(length):
    order_num = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for x in range(length))
    return order_num

# Remember to remove the blank=true from important model fields before you go live

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    cart_products = models.ManyToManyField("products.Product", blank=True, through='CartDetails')
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.user.first_name + "'s Cart"

    def get_item_count(self):
        return self.cart_products.all().count()

    def get_subtotal(self):
        for product in self.cart_products:
            # print(help(product))
            break

class CartDetails(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField(blank=True)
    color = ColorField(default="#ffffff", blank=True)
    
    def __str__(self):
        return self.cart.user.first_name + "'s Cart"

    def total(self):
        return self.product.price * self.quantity

class Wishlist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    wish_products = models.ManyToManyField(Product, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def get_item_count(self):
        return self.wish_products.all().count()

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

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=300, blank=True)
    postcode = models.IntegerField(blank=True, default=000000)

    def is_completed(self):
        if (self.state == "" or self.state == " ") and (self.city == "" or self.city == " ") and (self.street == "" or self.street == " "):
            return False
        else:
            return True

class UserOrders(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    total = models.IntegerField()
    date_purchased = models.DateTimeField(default=timezone.now)
    order_number = models.CharField(max_length=12, unique=True)# Generate an alphanumeric value here
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES)

    def save(self, *args, **kwargs):
        order_number = self.order_number
        if len(order_number) != 12 and type(order_number) != str:
            alpha_num = alpha_numeric(12)
            self.order_number = str(alpha_num)
        super(UserOrders, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name}'s Orders"

class UserTickets(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length = 250)
    date_submitted = models.DateTimeField(default=timezone.now)
    ticket_type = models.CharField(max_length=100, choices=TICKET_TYPE_CHOICES)
    priority = models.CharField(max_length=100, choices=TICKET_PRIORITY_CHOICES)
    status = models.CharField(max_length=100, choices=TICKET_STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.first_name}'s Tickets"
    

# from accounts.models import Wishlist, Cart, CartDetails, CustomAccount
# from products.models import *
# user = CustomAccount.objects.get(email='ithink@mail.com')
# cart = Cart.objects.get_or_create(user=user)[0]
# wish = Wishlist.objects.get_or_create(user=user)[0]
# p1 = Product.objects.get(id=2)
# p2 = Product.objects.get(id=3)
# p3 = Product.objects.get(id=5)
# p4 = Product.objects.get(id=6)
# cd1 = CartDetails.objects.get(cart=cart, product=p1)

# Add a orders model to track a user's orders 
# Add a order-code field to track each product in the cart (for checkout and for the orders page.)