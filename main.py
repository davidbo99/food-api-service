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



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()