from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Category, Product, MoreProductImages, ProductReviews

# Register your models here.   

# class ProductReviewsAdmin(admin.ModelAdmin):
#     pass
# class ProductReviewsAdmin(admin.StackedInline):
#     model = ProductReviews

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

class CategoryAdmin(admin.ModelAdmin):
    def __str__(self):
        return 'Categories'

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    fields = ['name', 'price', 'product_image', 'in_stock', 'category', 'description']
    inlines = [MoreProductImagesAdmin]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.register(MoreProductImages, MoreProductImagesAdmin)
# admin.register(AvailableColors, AvailableColorsAdmin)
# admin.register(ProductReviews, ProductReviewsAdmin)