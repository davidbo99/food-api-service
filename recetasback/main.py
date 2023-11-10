# importaciones base para el endpoint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import random_recipe_routers
import os

app = FastAPI()

CONECTION = os.getenv("URL_CONECTION_FRONT")

# Configuración del middleware CORS ()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["CONECTION"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(random_recipe_routers.router)
