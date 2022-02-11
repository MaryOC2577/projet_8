from django.core.management.base import BaseCommand, CommandError
import requests
import pprint
from nutella.models import Category, Product

from requests.models import encode_multipart_formdata


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("category", nargs="+", type=str)

    def handle(self, *args, **options):
        category_name = options["category"]
        response = requests.get(
            f"https://fr.openfoodfacts.org/cgi/search.pl?search_terms={category_name}&search_simple=1&action=process&json=1&page=1&page_size=2000"
        )

        product_list = []

        nb_products = 20
        product_list = response.json()

        for product_data in product_list["products"]:
            categories = []
            category_list = product_data["categories"].replace(", ", ",").split(",")

            product = product_list["products"]

            for cat_name in category_list:
                cat = Category.objects.get_or_create(name=cat_name)[0]
                cat.save()
                categories.append(cat)

            if not product_data["categories_lc"] == "fr":
                continue

            # for product in products:
            #     if product["name"] == product_data["product_name_fr"]:
            #         continue
            #     else:
            product = Product(
                name=product_data["product_name_fr"],
                stores=product_data["stores"],
                nutriscore=(product_data["nutrition_grade_fr"]).upper(),
                url=product_data["url"],
                image=product_data["image_url"],
                nutrition=product_data["image_nutrition_url"],
            )

            product.save()
            product.categories.add(*[cat.id for cat in categories])
            product.save()

            print(
                "Nom du produit : ",
                product_data["product_name_fr"],
                "\nCatégories : ",
                product_data["categories"],
                "\nMagasins :",
                product_data["stores"],
                "\nNutriscore : ",
                product_data["nutrition_grade_fr"],
                "\nUrl : ",
                product_data["url"],
                "\n",
            )
