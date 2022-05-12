from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator
from vendors import models as acc_models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    description = RichTextUploadingField()
    category = models.ManyToManyField(Category)
    # vendor = models.ForeignKey(acc_models.VendorAccount, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    previous_price = models.PositiveIntegerField(blank=True, default=0)
    percent_off = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    # Add the stars and reviews

    def save(self, *args, **kwargs):
        self.percent_off = int((self.previous_price / self.price) * 100)
        super(Product, self).save(*args, **kwargs)

class MoreProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='all_product_images')

class ProductReviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = RichTextUploadingField()

# Allow vendors to schedule products