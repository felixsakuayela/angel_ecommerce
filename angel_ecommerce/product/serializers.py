from rest_framework import serializers
from product.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'slug', 'description', 'cat_image']

class CategoryRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = fields = ['category_name', 'slug', 'description', 'cat_image']

    def create(self, validate_data):
        return Category.objects.create_category(**validate_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'description', 'price', 'images', 'stock', 'is_available', 'category', 'created_date', 'modified_date']

class ProductRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'description', 'price', 'images', 'stock', 'is_available', 'category', 'created_date', 'modified_date']
        extra_kwargs = {
            'created_date': {'read_only': True}, 'modified_date': {'read_only': True},
        }

    def create(self, validate_data):
        return Category.objects.create_category(**validate_data)