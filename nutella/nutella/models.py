from django.db import models
from login.models import User


class Category(models.Model):
    name = models.CharField(max_length=400, unique=True)

    def get_pk_category_by_name(self, cat_name):
        return Category.objects.get(name=cat_name)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stores = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    image = models.URLField(default="")
    nutrition = models.URLField(default="")
    categories = models.ManyToManyField(Category)

    def get_six_better_substitutes(self):
        # return [
        #     Product.objects.get(pk=155),
        #     Product.objects.get(pk=154),
        #     Product.objects.get(pk=153),
        #     Product.objects.get(pk=152),
        #     Product.objects.get(pk=151),
        #     Product.objects.get(pk=150),
        # ]
        id_categories = []
        catname = "pizza"

        id_categories = Category.objects.get(
            pk=Category.get_pk_category_by_name(catname)
        )

        return Product.objects.get(categories=id_categories)


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
