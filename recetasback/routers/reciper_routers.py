from fastapi import  APIRouter, Query
from ..services.services import get_recipes_by_ingredients

router = APIRouter()

"""Endpoint para obtener las recetas de acuerdo a los ingredientes igresados
Ejemplo de petición: http://localhost:8000/recipes/?ingredient=apples&ingredient=flour
"""
@router.get("/recipes/")
def search_recipes(ingredient: str = Query(...)):
    return get_recipes_by_ingredients(ingredient)