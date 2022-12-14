from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from product.models import Category, Product, Variation, ReviewRating, ProductGallery
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from product.serializers import CategorySerializer, CategoryRegistrationSerializer, ProductSerializer, ProductRegistrationSerializer
from product.serializers import VariationSerializer, VariationRegistrationSerializer, ReviewRatingSerializer, ReviewRatingRegistrationSerializer
from product.serializers import ProductGallerySerializer, ProductGalleryRegistrationSerializer
from product.renderers import ProductRenderer
from rest_framework.permissions import IsAuthenticated


class ListCategoryViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RegisterCategoryViews(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRegistrationSerializer

class ListProductViews(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RegisterProductViews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRegistrationSerializer

class ListVariationViews(generics.ListAPIView):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer

class RegisterVariationViews(generics.CreateAPIView):
    queryset = Variation.objects.all()
    serializer_class = VariationRegistrationSerializer

class ListReviewRatingViews(generics.ListAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewRatingSerializer

class RegisterReviewRatingViews(generics.CreateAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewRatingRegistrationSerializer

class ListProductGalleryViews(generics.ListAPIView):
    queryset = ProductGallery.objects.all()
    serializer_class = ProductGallerySerializer

class RegisterProductGalleryViews(generics.CreateAPIView):
    queryset = ProductGallery.objects.all()
    serializer_class = ProductGalleryRegistrationSerializer

'''class RegisterCategoryViews(APIView):
    renderer_classes = [ProductRenderer]
    #permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = CategoryRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)'''

'''class ListProductViews(APIView):
    renderer_classes = [ProductRenderer]
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)'''

'''class RegisterProductViews(APIView):
    renderer_classes = [ProductRenderer]
    #permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = ProductRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)'''


'''class ...View(APIView):

    def get(self, request, *args, **kwargs):

        queryset = ....objects.all()

        serializer = ...Serializer(queryset, many=True, context={"request":request})

        return Response(serializer.data, status=status.HTTP_200_OK)'''

