# api.py — FastAPI сервер
# Установить: pip install fastapi uvicorn scikit-learn joblib pandas
# Запустить:  uvicorn api:app --reload
# Docs:       http://127.0.0.1:8000/docs

from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Demo ML API")

MODEL_PATH = Path(__file__).parent / "model_pipeline.joblib"
pipeline = joblib.load(MODEL_PATH)


# Схема входного запроса — описывает поля и их типы
class OrderIn(BaseModel):
    age: int
    income: float
    city: str


@app.post("/predict")
def predict(order: OrderIn):
    # Pydantic уже проверил типы — просто берём данные
    df = pd.DataFrame([order.model_dump()])

    proba = pipeline.predict_proba(df)[:, 1][0]
    pred  = int(proba >= 0.5)

    return {
        "prediction":  pred,             # 0 или 1
        "probability": round(proba, 4),  # вероятность класса 1
    }
