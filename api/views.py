from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Category, Flavour, Restaurant
from .serializers import CategoryListSerializer, FlavourListSerializer, RestaurantListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class FlavourListView(ListAPIView):
    queryset = Flavour.objects.all()
    serializer_class = FlavourListSerializer


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
