# importaciones base para el endpoint
from fastapi import FastAPI, HTTPException
import requests
import uvicorn

# imoortaciones para las variables de entorno
import os
from dotenv import load_dotenv


app = FastAPI()


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# "definicion" de las variables de entorno
URL = os.getenv("URL")
KEY = os.getenv("KEY")


@app.get('/random/')
def get_random_recipes():
    url = URL
    headers = {'x-api-key': KEY}
    response = requests.get(url, headers=headers)

    # validaciones para las respuestas de la petición
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Error")


# ejecucion del codigo
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
