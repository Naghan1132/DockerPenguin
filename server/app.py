from fastapi import FastAPI
from pymongo import MongoClient
import pandas as pd
import joblib 
from pydantic import BaseModel

app = FastAPI()
client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection

class Item(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    #island: object
    #sex: object


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/show_columns")
async def show_columns():
    df = pd.read_csv("penguins.csv")
    columns_data = df.to_dict(orient="split")["data"]
    return {"results": columns_data}



@app.post("/predict")
async def predict(item: Item):
    # Votre logique de prétraitement des données ici
    model = joblib.load("model.pkl")
    data = item.dict()
    data = pd.DataFrame([data])
    #[item.bill_depth_mm,item.bill_length_mm,item.flipper_length_mm,item.body_mass_g,item.island,item.sex]
    # Utiliser le modèle pour faire une prédiction
    print(data)
    prediction = model.predict(data) 
    
    return {"prediction": prediction[0]}
