"""Modelos de datos"""
from pydantic import BaseModel



class RecipeBase(BaseModel):
    name: str
    ingredients: str
    image: str
    link: str
    visit_count: int


class Recipe(RecipeBase):
    id: int


