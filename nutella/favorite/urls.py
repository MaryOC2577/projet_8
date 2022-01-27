from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path("favorites/", views.ShowFavorites.as_view(), name="favorites"),
]
