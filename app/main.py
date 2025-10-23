from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import joblib
import pandas as pd
from .schemas import HeartInput
import os

app = FastAPI(title="Heart Disease Prediction API", version="1.0.0")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "heart_model.joblib")
model = joblib.load(MODEL_PATH)

FEATURE_ORDER = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/info")
async def info():
    return {
        "model": "RandomForestClassifier",
        "features": FEATURE_ORDER,
        "n_features": len(FEATURE_ORDER)
    }

@app.post("/predict")
async def predict(data: HeartInput):
    try:
        # Convert Pydantic → dict → DataFrame (single row)
        row = pd.DataFrame([data.dict()], columns=FEATURE_ORDER)
        prob = model.predict_proba(row)[0][1]      # probability of class 1
        pred = bool(model.predict(row)[0])
        return {"heart_disease": pred, "probability": round(prob, 4)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))