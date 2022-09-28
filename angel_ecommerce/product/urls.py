from django.urls import path
from product.views import ListCategoryViews, RegisterCategoryViews, ListProductViews, RegisterProductViews

urlpatterns = [
    path('categories/', ListCategoryViews.as_view(), name='categories'),
    path('registration-categories/', RegisterCategoryViews.as_view(), name='registration-categories'),
    path('products/', ListProductViews.as_view(), name='products'),
    path('registration-products/', RegisterProductViews.as_view(), name='registration-products'),
]