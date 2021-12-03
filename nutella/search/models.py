from django.db import models
from django.views.generic import ListView
from nutella.models import Product, Category


class SearchProduct(ListView):

    # products = Product()
    # categories = Category()

    # def find_product(self, name):
    #     for product in self.products:
    #         if product.name == name:
    #             return product

    model = Product
    context_object_name = "products"
