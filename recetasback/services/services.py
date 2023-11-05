"""Logica del negocio de la app,funciones esenciales para la creación de recetas en la base 
de datos y la búsqueda de recetas por ingredientes"""

from fastapi import HTTPException
from models.models import RecipeBase
from sqlalchemy.orm import Session
from models import RecipeCreate


def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = RecipeBase(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipes_by_ingredients(ingredients: str, page: int = 1, limit: int = 10):
    # Implementa la lógica para buscar recetas por ingredientes en la base de datos.
    # Si no se encuentran, usa fetch_recipes_by_ingredients desde spoonacular_api.
    pass