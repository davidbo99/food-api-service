from fastapi import APIRouter
from ..services.services import get_recipes_by_ingredients

router = APIRouter()

@router.get("/recipes/")
def search_recipes(ingredients: str, page: int = 1, limit: int = 10):
    recipes = get_recipes_by_ingredients(ingredients, page, limit)
    return {"recipes": recipes}