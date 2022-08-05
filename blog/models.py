from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from shoppa import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="blog_covers", blank=True)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=350)
    post = RichTextUploadingField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
