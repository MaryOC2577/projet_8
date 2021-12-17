from django.db import models
from login.models import User


class Category(models.Model):
    name = models.CharField(max_length=400, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    stores = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    image = models.URLField(default="")
    nutrition = models.URLField(default="")
    categories = models.ManyToManyField(Category)

    def get_six_better_substitutes(self):
        return [
            Product.objects.get(pk=221),
            Product.objects.get(pk=222),
            Product.objects.get(pk=223),
            Product.objects.get(pk=224),
            Product.objects.get(pk=225),
            Product.objects.get(pk=226),
        ]


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
