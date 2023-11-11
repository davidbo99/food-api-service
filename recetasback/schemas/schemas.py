"""Modelos de datos"""
from typing import List, Optional
from pydantic import BaseModel, HttpUrl



class Recipe(BaseModel):
    id: int
    title: str
    image: HttpUrl
    dairyFree: bool
    glutenFree: bool
    ketogenic: Optional[bool]  # Usar Optional ya que ketogenic puede ser null/None
    vegan: bool
    instructions: str
    extendedIngredients: List[str]