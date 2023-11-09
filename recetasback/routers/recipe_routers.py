from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from ..services.recipe_service import get_recipes_by_nutrients

router = APIRouter(prefix='/recipes')

@router.get("/recipes")
def get_recipes(min_calories: int = 0, max_calories: int = 20000):
    response = get_recipes_by_nutrients(min_calories, max_calories)
    
    # Validaciones para las respuestas de la petición
    if response.status_code == 200:
        return response.json()
    else:
        # Usar JSONResponse para personalizar el código de estado de la respuesta
        return JSONResponse(content={"detail": "Error"}, status_code=response.status_code)