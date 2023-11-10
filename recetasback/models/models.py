"""Modelos de datos"""

from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from database import Base

class RecipeDB(Base):
    __tablename__ = "recipes"

    id = Column(String, primary_key=True)
    title = Column(String)
    image = Column(String)
    readyInMinutes = Column(Integer)
    dairyFree = Column(Boolean)
    glutenFree = Column(Boolean)
    ketogenic = Column(Boolean)
    vegan = Column(Boolean)
    instructions = Column(String)
    extendedIngredients_aisle = Column(ARRAY(String))