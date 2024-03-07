import re
import random
from typing import Dict, List
from string import ascii_letters

from django.contrib.auth.models import User

from apps.product.sample_data import *
from apps.product.models import *


def random_character(n=10):
    return ''.join(random.choices(ascii_letters, k=n))


def generate_hashtags(data: Dict) -> List[Hashtag]:
    hashtags = [re.sub(r'\s+', '', product) for products_list in data.values() for product in products_list]
    return [Hashtag(name=tag) for tag in hashtags]


def generate_categories(data: Dict) -> List[Category]:
    categories = []
    for category in data.keys():
        categories.append(
            Category(
                name_en=category,
                notes=category,
                hashtag=Hashtag.objects.create(
                    name=re.sub(r'\s+', '', category)
                )
            )
        )
    return categories


def generate_users(data: List) -> List[User]:
    users = []
    for user in data:
        username = user.lower().replace(" ", "_")
        name_elements = user.split()
        usr = User.objects.create(
            username=username,
            first_name=name_elements.pop(0),
            last_name=" ".join(name_elements),
        )
        usr.set_password(username)
        usr.save(update_fields=['password'])
        users.append(usr)
    return users


def generate_merchants(users) -> List[Merchant]:
    return [Merchant(owner=user, name=user.username) for user in users]


def generate_products(product_data: Dict, merchants: List[Merchant]) -> List[Product]:
    product_objs = []
    for category, products in product_data.items():
        category_obj = Category.objects.get(name_en=category)
        for product in products:
            product_objs.append(
                Product(
                    name=product,
                    quantity=random.randint(20, 100),
                    merchant=merchants[random.randint(0, len(merchants) - 1)],
                    category=category_obj,
                )
            )
    return product_objs


def generate_data():
    hashtags = generate_hashtags(PRODUCTS)
    Hashtag.objects.bulk_create(hashtags)

    categories = generate_categories(PRODUCTS)
    Category.objects.bulk_create(categories)

    users = generate_users(USER)

    merchants = generate_merchants(users)
    Merchant.objects.bulk_create(merchants)

    products = generate_products(PRODUCTS, merchants)
    Product.objects.bulk_create(products)

    return True
