"""Logica del negocio de la app,funciones esenciales para la creación de recetas en la base 
de datos y la búsqueda de recetas por ingredientes"""

from fastapi import HTTPException
from schemas.schemas import RecipeBase
from sqlalchemy.orm import Session
from schemas.schemas import RecipeCreate, Recipe , RecipeDB, Recipe
from services.spoonacular_api import fetch_recipes_by_ingredients
import requests
import os


SPOONACULAR_API_BASE_URL = "https://spoonacular.com/food-api"


API_KEY = os.environ.get("SPOONACULAR_API_KEY", None)



def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = RecipeBase(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipes_by_ingredients(ingredients: str, page: int = 1, limit: int = 10):
     
    recipes_from_api = fetch_recipes_by_ingredients(ingredients)
    return recipes_from_api


def fetch_recipes_by_ingredients(ingredients):#toma una lista de ingredientes como argumento y utiliza la API de Spoonacular para buscar recetas que contengan esos ingrediente
    """Función para buscar recetas por ingredientes"""     
    endpoint = "/recipes/findByIngredients"
    url = f"{SPOONACULAR_API_BASE_URL}{endpoint}"

    params = {
        "apiKey": API_KEY,
        "ingredients": ",".join(ingredients),  # Convierte la lista de ingredientes en una cadena separada por comas
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al realizar la solicitud a Spoonacular API: {e}")