"""Obtener Recetas"""

from fastapi import FastAPI, HTTPException
import requests
import uvicorn

#Importar variables de entorno
import os
from dotenv import load_dotenv


#Importar CORS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Cargar archivo .env
load_dotenv()


# Llamar variables de entorno:
URL = os.getenv("URL")
key = os.getenv("API_KEY")


#Habilitar cors para permitir el acceso desde el origen del frontend
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Listar recetas.
@app.get("/recipe-list/")
def get_recipes_list():
    params = {
        'apiKey': key,
        'number': '20',
        # 'cuisine': '', 
        # 'diet': '', 
        # 'query': '', 
    }
    print(params)
    url = URL
    print(url)
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        return data['results']
    else:
        raise HTTPException(status_code=500, detail="Error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
