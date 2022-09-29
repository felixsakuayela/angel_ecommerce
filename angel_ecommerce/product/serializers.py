from django.forms import ImageField
from rest_framework import serializers
from product.models import Category, Product, Variation, ReviewRating, ProductGallery


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'slug', 'description', 'cat_image']

class CategoryRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = fields = ['category_name', 'slug', 'description', 'cat_image']

'''    def create(self, validate_data):
        return Category.objects.create_category(**validate_data)'''

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
        return Category.objects.created_date(**validate_data)

class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['product', 'variation_category', 'variation_value', 'is_active', 'created_date']

class VariationRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['product', 'variation_category', 'variation_value', 'is_active', 'created_date']
        extra_kwargs = {
            'created_date': {'read_only': True},
        }

    def create(self, validate_data):
        return Variation.objects.created_date(**validate_data)

class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewRating
        fields = ['product', 'user', 'subject', 'review', 'rating', 'rating', 'ip', 'status', 'created_at', 'updated_at']

class ReviewRatingRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewRating
        fields = ['product', 'user', 'subject', 'review', 'rating', 'rating', 'ip', 'status', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_date': {'read_only': True}, 'updated_at': {'read_only': True},
        }

    def create(self, validate_data):
        return ReviewRating.objects.created_at(**validate_data)

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['product', 'image', ]

class ProductGalleryRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['product', 'image', ]

