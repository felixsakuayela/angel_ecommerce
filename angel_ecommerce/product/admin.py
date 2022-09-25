from django.contrib import admin
from product.models import Category, Product, Variation, ReviewRating, ProductGallery

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)