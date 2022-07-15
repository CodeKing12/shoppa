from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import MoreProductImages, ProductReviews, Product, PC, Phone, Game

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock', 'category']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['product', 'ram', 'storage', 'manufacturer', 'os_type']

class PCAdmin(admin.ModelAdmin):
    list_display = ['product', 'manufacturer', 'ram', 'storage', 'os_type', 'hard_disk', 'processor_type']

class GameAdmin(admin.ModelAdmin):
    list_display = ['product', 'min_ram', 'processor_type', 'min_storage', 'min_dx_version', 'os_type', 'size']

class ProductReviewsAdmin(admin.ModelAdmin):
    pass
class ProductReviewsAdmin(admin.StackedInline):
    model = ProductReviews

class MoreProductImagesAdmin(admin.ModelAdmin):
    pass

class AvailableColorsAdmin(admin.ModelAdmin):
    pass

class MoreProductImagesAdmin(admin.StackedInline):
    model = MoreProductImages
    verbose_name = 'More Product Images'
    verbose_name_plural = 'More Product Images'
    extra = 2
    max = 10

# class AvailableColorsAdmin(admin.StackedInline):
#     model = AvailableColors
#     extra = 1
#     verbose_name_plural = 'Available Colors'

admin.site.register(Product, ProductAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(PC, PCAdmin)
admin.site.register(Game, GameAdmin)
admin.register(MoreProductImages, MoreProductImagesAdmin)
# admin.register(AvailableColors, AvailableColorsAdmin)
admin.register(ProductReviews, ProductReviewsAdmin)