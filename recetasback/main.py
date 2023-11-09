"""Main del proyecto"""

from fastapi import FastAPI
from recetasback.dependencies.containers import Container
from recetasback.routers import endpoints


app = FastAPI()


if __name__ == '__main__':
    """Punto de inicio en el que se crea el contenedor, la inyección de la base de datos y el sistema de rutas"""
    container = Container()
    container.wire(modules=[__name__])
    db = container.db()
    app.container = container
    app.include_router(endpoints.router)
