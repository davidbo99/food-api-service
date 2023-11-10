"""Logica del negocio de la app,funciones esenciales para la creación de recetas en la base 
de datos y la búsqueda de recetas por ingredientes"""

from fastapi import HTTPException
from ..schemas.schemas import RecipeBase
from sqlalchemy.orm import Session
import requests
import os, json


SPOONACULAR_API_BASE_URL = "https://api.spoonacular.com"


API_KEY = os.environ.get("SPOONACULAR_API_KEY", None)



def create_recipe(db: Session, recipe: RecipeBase):
    db_recipe = RecipeBase(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe



def get_recipes_by_ingredients(ingredients: str):
    recipes = fetch_recipes_by_ingredients(ingredients)
    detailed_recipes = []

    for recipe in recipes:
        recipe_details = fetch_recipe_details(recipe['id'])
        extended_ingredients_list = recipe_details.get('extendedIngredients', [])
        aisles_set = {ingredient.get('aisle') for ingredient in extended_ingredients_list if ingredient.get('aisle') is not None}
        aisles = list(aisles_set)

        detailed_recipes.append({
            "id": recipe['id'],
            "title": recipe['title'],
            "image": recipe['image'],
            "dairyFree": recipe_details.get('dairyFree'),
            "glutenFree": recipe_details.get('glutenFree'),
            "ketogenic": recipe_details.get('ketogenic'),
            "vegan": recipe_details.get('vegan'),
            "instructions": recipe_details.get('instructions', ''),
            "extendedIngredients": aisles
        })
    
    return detailed_recipes

def fetch_recipes_by_ingredients(ingredients: str):
    endpoint = "/recipes/findByIngredients"
    headers_api = {
        "x-api-key": API_KEY,
    }
    url = f"{SPOONACULAR_API_BASE_URL}{endpoint}?ingredients={ingredients}&number=20"
    return json.loads(requests.request("GET", url, headers=headers_api).text)

def fetch_recipe_details(recipe_id: int):
    endpoint = f"/recipes/{recipe_id}/information"
    headers_api = {
        "x-api-key": API_KEY,
    }
    url = f"{SPOONACULAR_API_BASE_URL}{endpoint}"
    return json.loads(requests.request("GET", url, headers=headers_api).text)