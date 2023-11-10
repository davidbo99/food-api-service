from fastapi import APIRouter, Query
from ..services.services import get_recipes_by_ingredients
from typing import List

router = APIRouter()

@router.get("/recipes/")
def search_recipes(ingredient: str = Query(...)):
    recipes = get_recipes_by_ingredients(ingredient)
    return {"recipes": recipes}