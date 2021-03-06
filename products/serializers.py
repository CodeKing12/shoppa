from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ("id", "name", "image", "description", "price", "previous_price", "percent_off", "in_stock", "category")
        fields = "__all__"
