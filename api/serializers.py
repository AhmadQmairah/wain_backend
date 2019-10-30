from rest_framework import serializers
from .models import Category, Flavour, Restaurant


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FlavourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavour
        fields = "__all__"


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
