from django.urls import path
from product.views import ListCategoryViews, RegisterCategoryViews, ListProductViews, RegisterProductViews
from product.views import ListVariationViews, RegisterVariationViews, ListReviewRatingViews, RegisterReviewRatingViews
from product.views import  ListProductViews, RegisterProductGalleryViews

urlpatterns = [
    path('categories/', ListCategoryViews.as_view(), name='categories'),
    path('registration-categories/', RegisterCategoryViews.as_view(), name='registration-categories'),
    path('products/', ListProductViews.as_view(), name='products'),
    path('registration-products/', RegisterProductViews.as_view(), name='registration-products'),
    path('variations/', ListVariationViews.as_view(), name='variations'),
    path('registration-variations/', RegisterVariationViews.as_view(), name='registration-variations'),
    path('reviewRating/', ListReviewRatingViews.as_view(), name='reviewRating'),
    path('registration-reviewRating/', RegisterReviewRatingViews.as_view(), name='registration-reviewRating'),
    path('product-galleries/', ListProductViews.as_view(), name='product-galleries'),
    path('registration-product-galleries/', RegisterProductGalleryViews.as_view(), name='registration-product-galleries'),
]