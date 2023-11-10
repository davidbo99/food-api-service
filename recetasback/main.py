# importaciones necesarias para el funcionamiento de la API
from fastapi import FastAPI
from recetasback.dependencies.containers import Container
from .routers import recipe_routers


app = FastAPI()


container = Container()
container.wire(modules=[__name__])
db = container.db()
app.container = container
app.include_router(recipe_routers.router)
