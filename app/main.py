import mlflow
import pandas as pd
from pydantic import BaseModel,Field
from typing import Literal
from datetime import date
from fastapi import FastAPI

model = mlflow.pyfunc.load_model('../saved_pipeline')

app = FastAPI()

class data(BaseModel):
    name: str
    year: int = Field(ge=1900,le=date.today().year)
    km_driven: int
    fuel: Literal['Petrol','Diesel','CNG','LPG','Electric']
    seller_type: Literal['Individual','Dealer','Trustmark Dealer']
    transmission: Literal['Manual','Automatic']
    owner: Literal['Test Drive Car','First OWner','Second Owner','Third Owner','Fourth & Above Owner']

@app.get("/")
def api_check():
    return{"Status":"Okay"}

@app.post("/predict")
def predict_price(car_data : data):
    d = car_data.model_dump()
    X = pd.DataFrame([d])

    pred = model.predict(X)

    return {"price":pred[0].item()}

