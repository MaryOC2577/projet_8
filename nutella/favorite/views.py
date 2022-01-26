from msilib.schema import ListView
from django.shortcuts import render
from nutella.models import Favorite


class ShowFavorites(ListView):
    template_name = "favorites.html"
    model = Favorite()
    context_object_name = "favorites"
