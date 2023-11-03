from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI()


@app.get("/recipes/")
def get_recipes(minCalories: int, maxCalories: int):
    # Obtén recetas basadas en un rango de calorías específico.
    url = f"https://api.spoonacular.com/recipes/findByNutrients?\
        minCalories={minCalories}&maxCalories={maxCalories}"
    headers = {'x-api-key': 'b31d2b784b94458f80d709dfb07840ed'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Error")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
