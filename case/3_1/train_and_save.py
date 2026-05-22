# train_and_save.py — обучаем игрушечную модель и сохраняем пайплайн
# Запустить один раз: python train_and_save.py

from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

# --- Игрушечный датасет (не ecommerce!) ---
data = pd.DataFrame({
    "age":      [25, 40, 35, 22, 58, 30, 45, 29],
    "income":   [30000, 80000, 55000, 25000, 120000, 42000, 95000, 38000],
    "city":     ["Moscow", "SPb", "Moscow", "Kazan", "SPb", "Kazan", "Moscow", "SPb"],
    "approved": [0, 1, 1, 0, 1, 0, 1, 0],   # таргет
})

X = data.drop(columns=["approved"])
y = data["approved"]

# --- Пайплайн ---
preprocessor = ColumnTransformer(transformers=[
    ("num", "passthrough", ["age", "income"]),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), ["city"]),
])

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier",   RandomForestClassifier(n_estimators=50, random_state=42)),
])

pipeline.fit(X, y)

MODEL_PATH = Path(__file__).parent / "model_pipeline.joblib"
joblib.dump(pipeline, MODEL_PATH)
print(f"Сохранено: {MODEL_PATH}")
