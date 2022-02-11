from django.urls import path
from django.urls.conf import include
from . import views

app_name = "favorite"

urlpatterns = [
    path("", views.ShowFavorites.as_view(), name="myfavorites"),
]
