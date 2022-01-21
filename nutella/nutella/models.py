from django.db import models
from django.shortcuts import get_object_or_404
from django.db.models import Q
from login.models import User


class Category(models.Model):
    name = models.CharField(max_length=400, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stores = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    image = models.URLField(default="")
    nutrition = models.URLField(default="")
    categories = models.ManyToManyField(Category)

    def get_six_better_substitutes(self):

        unavaillable_substitutes = list(
            set([favorite.product.id for favorite in Favorite.objects.all()])
        )

        # récupérer le nutriscore du produit choisit par l'utilisateur
        grade = self.nutriscore
        # retourner les 6 produits avec le meilleur nutriscore possible
        six_better_products = (
            Product.objects.filter(
                categories=[category.id for category in self.categories.all()][0]
            )
            .filter(Q(nutriscore=grade))
            .exclude(id__in=unavaillable_substitutes)
            .order_by("nutriscore")[:5]
        )
        for element in six_better_products:
            print("test :", element.name)
        else:
            print("Pas de substitut disponible.")
        return six_better_products


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
