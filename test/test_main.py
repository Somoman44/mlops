import numpy as np
from fastapi.testclient import TestClient
from unittest.mock import patch
import pytest
from app.main import app
from datetime import date

client = TestClient(app)

def test_api_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Status":"Okay"}

@patch("app.main.model")
def test_predict_price_success(mock_model):
    mock_model.predict.return_value = np.array([450000])
    valid_payload = {
        "name": "Maruti Swift Dzire VDI",
        "year": 2018,
        "km_driven": 45000,
        "fuel": "Diesel",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First OWner" 
    }
    response = client.post("/predict",json=valid_payload)
    
    assert response.status_code == 200
    assert "price" in response.json()
    assert response.json()["price"] == 450000

def test_predict_price_invalid_year():
    invalid_payload = {
        "name": "Maruti Swift Dzire VDI",
        "year": date.today().year + 1,
        "km_driven": 45000,
        "fuel": "Diesel",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First OWner" 
    }
    response = client.post("/predict",json=invalid_payload)

    assert response.status_code == 422
    assert "Input should be less than or equal to" in response.json()["detail"][0]["msg"]