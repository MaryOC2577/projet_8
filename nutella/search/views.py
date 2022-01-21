from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, ListView, DetailView, CreateView
from nutella.models import Product, Category, Favorite


class ProductResult(ListView):
    template_name = "result.html"
    model = Product
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        expression = self.request.GET.get("expression", "").title()
        print("expression :", expression)
        return Product.objects.filter(name__contains=expression) if expression else []

    def get_context_data(self, **kwargs):
        kwargs["expression"] = self.request.GET.get("expression", "")

        return super().get_context_data(**kwargs)


class OneProduct(DetailView):
    template_name = "product.html"

    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        kwargs["substitutes"] = self.get_object().get_six_better_substitutes()
        self.request.session["product_id"] = self.get_object().id
        return super().get_context_data(**kwargs)


class Substitutes(ListView):
    template_name = "substitutes.html"

    model = Product
    context_object_name = "products"


class SearchView(View):
    def get(self, request):
        return render(request, "search.html")


class SaveFavorites(View):
    def get(self, request, pk):

        favsave = Favorite(product=Product.objects.get(pk=pk), user=request.user)
        favsave.save()
        print("test request get", request.GET)
        return redirect("oneproduct", self.request.session["product_id"])
