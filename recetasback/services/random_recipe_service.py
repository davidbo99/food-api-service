import requests
import os


# "definicion" de las variables de entorno
URL = os.getenv("SPOONACULAR_URL")
KEY = os.getenv("SPOONACULAR_API_KEY")


def get_random_recipes():
    url = URL
    headers = {'x-api-key': KEY}
    response = requests.get(url, headers=headers)
    return response
