
from django.contrib import admin
from django.urls import path
from api.views import CategoryListView, FlavourListView, RestaurantListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("flavours/", FlavourListView.as_view(), name="flavours-list"),
    path("restaurants/", RestaurantListView.as_view(), name="restaurants-list")

]
