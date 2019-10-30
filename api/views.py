from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Tag, Restaurant
from .serializers import TagListSerializer, RestaurantListSerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
