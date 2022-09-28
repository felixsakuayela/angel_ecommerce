from django.urls import path
from product.views import ListCategoryViews, RegisterCategoryViews

urlpatterns = [
    path('categories/', ListCategoryViews.as_view(), name='categories'),
    path('registration-categories/', RegisterCategoryViews.as_view(), name='registration-categories'),
]