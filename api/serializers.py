from rest_framework import serializers
from .models import Tag, Restaurant


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
