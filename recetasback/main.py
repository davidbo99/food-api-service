"""Main del proyecto"""

from fastapi import FastAPI
from recetasback.dependencies.containers import Container
from recetasback.routers import reciper_routers


app = FastAPI()

"""Punto de inicio en el que se crea el contenedor, la inyección de la base de datos y el sistema de rutas"""
container = Container()
container.init_resources()
container.wire(modules=[__name__])
db = container.db()
app.container = container
app.include_router(reciper_routers.router)
