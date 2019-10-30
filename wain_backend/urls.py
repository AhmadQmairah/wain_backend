
from django.contrib import admin
from django.urls import path
from api.views import RestaurantListView, TagListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("tags/", TagListView.as_view(), name="tag-list"),

    path("restaurants/", RestaurantListView.as_view(), name="restaurants-list")

]
