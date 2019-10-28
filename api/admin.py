from django.contrib import admin
from .models import Restaurant, Flavour, Category
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Flavour)
admin.site.register(Category)
