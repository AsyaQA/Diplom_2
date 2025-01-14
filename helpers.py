from random import randint, choice
from string import ascii_letters

import requests

from urls import Urls


def random_email():
    return f"{"".join(choice(ascii_letters) for _ in range(3))}{randint(100, 999)}@mail.com"

def random_password():
    return f"{choice(ascii_letters)}{randint(1000, 9999)}{choice(ascii_letters)}"

def random_name():
    return "".join(choice(ascii_letters) for _ in range(6))

def get_register_params():
    register_params = {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }
    return register_params

def get_ingredients():
    ingredients = requests.get(f"{Urls.BASE_URL}{Urls.INGREDIENTS}")
    return ingredients.json()["data"]

def get_list_id_ingredients():
    ingredients_id = []
    for value in get_ingredients():
        ingredients_id.append(value["_id"])
    return ingredients_id
