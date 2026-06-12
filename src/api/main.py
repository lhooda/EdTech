"""from typing import Optional
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.models.predictor import load_model, validate_input
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import time
app = FastAPI(title="EdTech Dropout Prediction API")
predictions_total = Counter(
    "predictions_total",
    "Nombre total de prédictions",
    ["status"]
)

prediction_latency = Histogram(
    "prediction_latency_seconds",
    "Temps de réponse des prédictions"
)

class StudentInput(BaseModel):
    code_module: str
    code_presentation: str
    id_student: int
    gender: str
    region: str
    highest_education: str
    imd_band: str
    age_band: str
    num_of_prev_attempts: int
    studied_credits: int
    disability: str
    final_result: str
    date_registration: float
    date_unregistration: Optional[float] = None
    avg_score: float
    total_clicks: float
    low_activity: int
    low_score: int
    engagement_score: float


@app.get("/")
def home():
    return {"message": "EdTech API opérationnelle"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: StudentInput):
    payload = data.model_dump()
    payload = validate_input(payload)

    model, preprocessor = load_model()

    X = pd.DataFrame([payload])
    X_processed = preprocessor.transform(X)

    prediction = int(model.predict(X_processed)[0])

    interpretation = "Risque de décrochage élevé" if prediction == 1 else "Risque faible"

    return {
        "prediction": prediction,
        "interpretation": interpretation
    }"""

from typing import Optional
import time

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

from src.models.predictor import load_model, validate_input


app = FastAPI(title="EdTech Dropout Prediction API")


predictions_total = Counter(
    "predictions_total",
    "Nombre total de prédictions",
    ["status"]
)

prediction_latency = Histogram(
    "prediction_latency_seconds",
    "Temps de réponse des prédictions"
)


class StudentInput(BaseModel):
    code_module: str
    code_presentation: str
    id_student: int
    gender: str
    region: str
    highest_education: str
    imd_band: str
    age_band: str
    num_of_prev_attempts: int
    studied_credits: int
    disability: str
    final_result: str
    date_registration: float
    date_unregistration: Optional[float] = None
    avg_score: float
    total_clicks: float
    low_activity: int
    low_score: int
    engagement_score: float


@app.get("/")
def home():
    return {"message": "EdTech API opérationnelle"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/predict")
def predict(data: StudentInput):
    start_time = time.time()

    try:
        payload = data.model_dump()
        payload = validate_input(payload)

        model, preprocessor = load_model()

        X = pd.DataFrame([payload])
        X_processed = preprocessor.transform(X)

        prediction = int(model.predict(X_processed)[0])

        risk_score = (
            (100 - payload["avg_score"]) * 0.4
            + payload["low_score"] * 25
            + payload["low_activity"] * 20
            + max(0, 5000 - payload["engagement_score"]) / 5000 * 15
        )

        prob_decrochage = round(min(max(risk_score, 0), 100), 2)
        prob_reussite = round(100 - prob_decrochage, 2)

        interpretation = (
            "Risque de décrochage élevé"
            if prob_decrochage >= 60
            else "Risque modéré"
            if prob_decrochage >= 30
            else "Risque faible"
        )

        predictions_total.labels(status="success").inc()
        prediction_latency.observe(time.time() - start_time)

        return {
            "prediction": prediction,
            "interpretation": interpretation,
            "prob_reussite": prob_reussite,
            "prob_decrochage": prob_decrochage
        }

    except Exception:
        predictions_total.labels(status="error").inc()
        prediction_latency.observe(time.time() - start_time)
        raise