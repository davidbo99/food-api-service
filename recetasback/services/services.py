"""Logica del negocio de la app,funciones esenciales para la creación de recetas en la base 
de datos y la búsqueda de recetas por ingredientes"""

from fastapi import HTTPException
from schemas.schemas import RecipeBase
from sqlalchemy.orm import Session
from schemas.schemas import RecipeCreate, Recipe , RecipeDB, Recipe
from services.spoonacular_api import fetch_recipes_by_ingredients


def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = RecipeBase(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipes_by_ingredients(ingredients: str, page: int = 1, limit: int = 10):
     if Recipe:
        return RecipeDB
     else:
        recipes_from_api = fetch_recipes_by_ingredients(ingredients)
        return recipes_from_api

"""def get_user_request_stock_history_by_id(
    db: Session, 
    user_request_stock_id: int
) -> Optional [#Modelo de la receta]:
    
    return db.query(#Modelo de la receta)\
            .filter(#modelodelareceta.ingedientes == user_request_stock_id)\
            .first()"""