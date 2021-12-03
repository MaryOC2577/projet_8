from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from nutella.models import Product, Category


class ProductResult(ListView):
    template_name = "result.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        expression = self.request.GET["expression"]
        print("expression :", expression)
        return Product.objects.filter(name__contains=expression)


class SearchView(View):
    def get(self, request):
        return render(request, "search.html")
