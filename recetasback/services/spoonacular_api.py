"""Toma lista de ingredientes como argumentos y usa api para buscar recetas con los ingredientes"""
import requests

# URL base de la API de Spoonacular
SPOONACULAR_API_BASE_URL = "https://spoonacular.com/food-api"

# Tu clave de API de Spoonacular
API_KEY = "66c2e3303dfd43ca8f52b7a8327a5158"

# Función para buscar recetas por ingredientes
def fetch_recipes_by_ingredients(ingredients):#toma una lista de ingredientes como argumento y utiliza la API de Spoonacular para buscar recetas que contengan esos ingrediente
    endpoint = "/recipes/findByIngredients"
    url = f"{SPOONACULAR_API_BASE_URL}{endpoint}"

    params = {
        "apiKey": API_KEY,
        "ingredients": ",".join(ingredients),  # Convierte la lista de ingredientes en una cadena separada por comas
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Si ocurre un error en la solicitud, lanzará una excepción
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al realizar la solicitud a Spoonacular API: {e}")