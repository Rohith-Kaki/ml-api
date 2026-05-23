from fastapi import FastAPI
import os
import redis

app = FastAPI()
cache = redis.Redis(host="redis", port=6379)

@app.get("/")
def root():
	return {"status": "ok"}

@app.post("/predict")
def predict(data:dict):
	features = data.get("features", [])
	key = str(features)
	cached = cache.get(key)
	if cached:
		return {"prediction": float(cached), "source": "cache"}
	result = sum(features) * 0.42
	cache.set(key, result)
	return {"prediciton":result, "source":"computed"}
