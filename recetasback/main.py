# importaciones base para el endpoint
from fastapi import FastAPI

from .routers import random_recipe_routers

import uvicorn


app = FastAPI()


app.include_router(random_recipe_routers.router)

# ejecucion del codigo
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
