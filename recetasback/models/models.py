"""Modelos de datos"""

from pydantic import BaseModel

class RecipeBase(BaseModel):
    name: str
    ingredients: str
    image: str
    link: str
    visit_count: int

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

# Modelo de base de datos (SQLAlchemy)
from sqlalchemy import Column, Integer, String
from database import Base

class RecipeDB(Base):
    __tablename__ = "recipes" #columna unica para cada receta que va a servir para identificarlas de manera unica

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String)
    image = Column(String)
    link = Column(String)
    visit_count = Column(Integer)