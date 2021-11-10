from django.db import models
from login.models import User


class Category(models.Model):
    name = models.CharField(max_length=36, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    stores = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category)


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
