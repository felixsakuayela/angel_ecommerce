from django.urls import path
from product.views import ListCategoryViews, RegisterCategoryViews, ListProductViews, RegisterProductViews, ListVariationViews, RegisterVariationViews

urlpatterns = [
    path('categories/', ListCategoryViews.as_view(), name='categories'),
    path('registration-categories/', RegisterCategoryViews.as_view(), name='registration-categories'),
    path('products/', ListProductViews.as_view(), name='products'),
    path('registration-products/', RegisterProductViews.as_view(), name='registration-products'),
    path('variations/', ListVariationViews.as_view(), name='variations'),
    path('registration-variations/', RegisterVariationViews.as_view(), name='registration-variations'),
]