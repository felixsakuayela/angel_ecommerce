from django.urls import path
from product.views import ListCategoryViews

urlpatterns = [
    path('categories/', ListCategoryViews.as_view(), name='categories'),
    #path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
]