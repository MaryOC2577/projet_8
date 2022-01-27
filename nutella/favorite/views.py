from msilib.schema import ListView
from django.shortcuts import render, redirect
from nutella.models import Favorite
from login.models import User
from django.contrib import messages


class ShowFavorites(ListView):
    template_name = "favorites.html"
    model = Favorite
    context_object_name = "favorites"

    user = User()

    if user.is_authenticated == False:
        messages.add_message(
            messages.SUCCESS, "Vous devez être connecté pour consulter la page favoris."
        )
        redirect("login")

    def delete_favorite(self, id):
        pass
