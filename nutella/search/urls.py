from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path("", views.SearchView.as_view(), name="search"),
    path("result/", views.ProductResult.as_view(), name="result"),
    path("oneproduct", views.OneProduct.as_view(), name="oneproduct"),
]
