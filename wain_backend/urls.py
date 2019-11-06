
from django.contrib import admin
from django.urls import path
from api.views import RestaurantListView, TagListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("tags/", TagListView.as_view(), name="tag-list"),

    path("restaurants/", RestaurantListView.as_view(), name="restaurants-list")

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
