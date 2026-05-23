import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    with patch("app.cache") as mock_cache:
        mock_cache.get.return_value = None
        response = client.post("/predict", json={"features": [1, 2, 3, 4]})
        assert response.status_code == 200
        assert "prediction" in response.json()

def test_predict_cache_hit():
    with patch("app.cache") as mock_cache:
        mock_cache.get.return_value = b"4.2"
        response = client.post("/predict", json={"features": [1, 2, 3, 4]})
        assert response.status_code == 200
        assert response.json()["source"] == "cache"
