from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path("", views.Favorite_view(), name="favorites"),
]
