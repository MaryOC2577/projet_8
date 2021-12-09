from django.db import models
from django.views.generic import ListView
from nutella.models import Product, Category


class SearchProduct(ListView):
    model = Product
    context_object_name = "products"
