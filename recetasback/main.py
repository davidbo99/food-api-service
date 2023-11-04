# importaciones necesarias para el funcionamiento de la API
from fastapi import FastAPI

from .routers import recipe_routers

import uvicorn


app = FastAPI()

app.include_router(recipe_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
