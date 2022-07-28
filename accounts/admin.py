from django.contrib import admin
from .models import CustomAccount, Cart, Wishlist, CartDetails, ApiUser
from vendors.models import VendorAccount
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomAccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number']
    ordering = ['-date_joined']
    list_filter = ['email', 'first_name', 'is_staff']
    add_fieldsets = (
        ('Create an Account', {'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
    fieldsets = (
        ('Edit Info', {'fields': ('first_name', 'last_name', 'email', 'password', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active',)})
    )

class ApiUserAdmin(admin.ModelAdmin):
    pass

class CartDetailsAdmin(admin.StackedInline):
    model = CartDetails
    extra = 1

class WishlistAdmin(admin.ModelAdmin):
    pass

class CartAdmin(admin.ModelAdmin):
    inlines = [CartDetailsAdmin]

class VendorAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomAccount, CustomAccountAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(ApiUser, ApiUserAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(VendorAccount, VendorAccountAdmin)
admin.register(CartDetails, CartDetailsAdmin)