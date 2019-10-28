from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Flavour(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    BUDGET_CHOICES = (
        ("$", "$"),
        ("$$", "$$"),
        ("$$$", "$$$"),
        ("$$$$", "$$$$"),
    )
    name = models.CharField(max_length=15)
    budget = models.CharField(max_length=15, choices=BUDGET_CHOICES)
    categories = models.ManyToManyField(
        Category, related_name="restaurants")
    flavours = models.ManyToManyField(
        Flavour, related_name="restaurants")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
