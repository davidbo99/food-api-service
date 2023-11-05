from fastapi import APIRouter, HTTPException
from ..services.random_recipe_service import get_random_recipes

router = APIRouter(prefix='/random_recipes')


@router.get("/random_recipes/")
def get_random_recipes_function():
    response = get_random_recipes()
    # validaciones para las respuestas de la petición
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Error")
