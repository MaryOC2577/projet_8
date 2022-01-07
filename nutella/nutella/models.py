from django.db import models
from django.shortcuts import get_object_or_404
from django.db.models import Q
from login.models import User


class Category(models.Model):
    name = models.CharField(max_length=400, unique=True)

    # def get_pk_category_by_name(self, cat_name):
    #     return Category.objects.get(name=cat_name)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stores = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    image = models.URLField(default="")
    nutrition = models.URLField(default="")
    categories = models.ManyToManyField(Category)

    def get_six_better_substitutes(self, product):
        # return [
        #     Product.objects.get(pk=155),
        #     Product.objects.get(pk=154),
        #     Product.objects.get(pk=153),
        #     Product.objects.get(pk=152),
        #     Product.objects.get(pk=151),
        #     Product.objects.get(pk=150),
        # ]
        # id_categories = []

        # catname = "pizza"

        # id_categories = Category.objects.get(
        #     pk=Category.get_pk_category_by_name(catname)
        # )
        # for category in self.categories:
        #     len(category.products)
        # # Product.objects.get(categories=id_categories).order_by(nutriscore)

        # return Product.objects.filter(categories__id=id_categories).order_by("nutriscore")[:5]

        # récupérer le produit choisit par l'utilisateur
        current_product = get_object_or_404(Product, product=product)
        # récupérer le nutriscore du produit choisit par l'utilisateur
        grade = current_product.nutriscore
        # retourner les 6 produits avec le meilleur nutriscore possible
        six_better_products = (
            Product.objects.filter(category=current_product.categories)
            .filter(Q(nutriscore=grade))
            .order_by("nutriscore")[:5]
        )
        for element in six_better_products:
            print("test :", element.name)
        else:
            print("Pas de substitut disponile.")
        return six_better_products


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
