# imoortaciones para las variables de entorno
import os

import requests

# "definicion" de las variables de entorno
URL = os.environ.get("SPOONACULAR_URL", None)
KEY = os.environ.get("SPOONACULAR_API_KEY", None)


def get_recipes_by_nutrients(min_calories: int = 0, max_calories: int = 20000):
    url = f"{URL}/recipes/findByNutrients?\
    minCalories={min_calories}&maxCalories={max_calories}"
    headers = {'x-api-key': KEY}
    response = requests.get(url, headers=headers)
    return response


""" recorrer el response (con un for) y hacer un request a la API de recipe
information ussando el ID de cada uno de los elementos de response
"""
