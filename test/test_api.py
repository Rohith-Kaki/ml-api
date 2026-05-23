from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"status": "ok"}

def test_predict():
	response = client.post("/predict", json={"features":[1,2,3,4]})
	assert response.status_code == 200
	assert "predicition" in response.json()

