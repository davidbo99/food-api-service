from fastapi import APIRouter, HTTPException
from ..services.recipe_service import get_recipes_by_nutrients

router = APIRouter(prefix='/recipes')


@router.get("/recipes")
def get_recipes(min_calories: int = 0, max_calories: int = 20000):
    response = get_recipes_by_nutrients(min_calories, max_calories)
    # validaciones para las respuestas de la petición
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Error")
