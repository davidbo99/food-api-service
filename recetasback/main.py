# importaciones base para el endpoint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import random_recipe_routers
import uvicorn


app = FastAPI()

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(random_recipe_routers.router)

# ejecucion del codigo
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
