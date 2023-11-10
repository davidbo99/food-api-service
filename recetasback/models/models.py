"""Modelos de datos"""

from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from database import Base

class RecipeDB(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    image = Column(String)
    dairyFree = Column(Boolean)
    glutenFree = Column(Boolean)
    ketogenic = Column(Boolean, nullable=True)
    vegan = Column(Boolean)
    instructions = Column(String)
    extendedIngredients = Column(ARRAY(String))