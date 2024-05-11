from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['product_id', 'item_name', 'item_description', 'price', 'quantity', 'image_url']