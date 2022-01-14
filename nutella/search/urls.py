from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path("", views.SearchView.as_view(), name="search"),
    path("result/", views.ProductResult.as_view(), name="result"),
    path("oneproduct/<int:pk>/", views.OneProduct.as_view(), name="oneproduct"),
    path("substitutes/<int:pk>/", views.Substitutes.as_view(), name="substitutes"),
    path("savefavorite/<int:pk>/", views.SaveFavorites.as_view(), name="favorite"),
]
