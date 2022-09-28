from rest_framework import serializers
from product.models import Category

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


