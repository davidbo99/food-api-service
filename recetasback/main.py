from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/recipes/")
def get_recipes(nutrients: str):
    """
    Obtén recetas basadas en un nutriente específico.
    """
    url = f"https://api.spoonacular.com/recipes/\
    findByNutrients?nutrients={nutrients}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Company doesn'texists")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
