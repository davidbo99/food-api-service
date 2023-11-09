"""Define una ruta para crear nuevas recetas y otra ruta para buscar recetas por ingredientes"""

from ast import get_docstring
from fastapi import FastAPI, Depends
from models.models import RecipeCreate
from sqlalchemy.orm import Session
from database import SessionLocal
from services import create_recipe, get_recipes_by_ingredients
from schemas import RecipeResponse


app = FastAPI()

"""Rutas FastAPI""" 
@app.post("/recipes/", response_model=RecipeResponse)#devuelve la respuesta de acuerdo con el esquema RecipeResponse
def create_new_recipe(recipe: RecipeCreate, db: Session = Depends(get_docstring)):#llama a la función create_recipe del módulo services para crear una nueva receta en la base de datos utilizando la sesión db. Luego, se devuelve la receta creada.
    return create_recipe(db, recipe)

@app.get("/recipes/")
def search_recipes(ingredients: str, page: int = 1, limit: int = 10):
    recipes = get_recipes_by_ingredients(ingredients, page, limit)
    return {"recipes": recipes}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()