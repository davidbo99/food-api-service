# importaciones necesarias para el funcionamiento de la API
from fastapi import FastAPI

from .routers import recipe_routers

import uvicorn


app = FastAPI()

app.include_router(recipe_routers.router)