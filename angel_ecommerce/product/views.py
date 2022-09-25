from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from product.models import Category, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from product.serializers import CategorySerializer
from product.renderers import ProductRenderer
from rest_framework.permissions import IsAuthenticated

class ListCategoryViews(APIView):
    renderer_classes = [ProductRenderer]
    def get(self, format=None):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
