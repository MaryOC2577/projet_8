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
            f"https://fr.openfoodfacts.org/cgi/search.pl?search_terms={category_name}&search_simple=1&action=process&json=1&page=1&page_size=20"
        )

        product_list = []

        nb_products = 20
        product_list = response.json()

        for product_data in product_list["products"]:
            categories = []
            category_list = []
            category_list.append(
                product_data["categories"].replace(", ", ",").split(",")
            )
            product = product_list["products"]

            for cat_name in category_list:
                categories.append(Category.objects.get_or_create(name=cat_name))
            breakpoint()
            product = Product(
                name=product["product_name_fr"],
                stores=product["stores"],
                nutriscore=product["nutrition_grade_fr"],
                url=product["url"],
                categories=categories,
            )

            print(
                "Nom du produit : ",
                product["product_name_fr"],
                "\nCatégories : ",
                product["categories"],
                "\nMagasins :",
                product["stores"],
                "\nNutriscore : ",
                product["nutrition_grade_fr"],
                "\nUrl : ",
                product["url"],
                "\n",
            )
