from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "date_modified", "author"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)