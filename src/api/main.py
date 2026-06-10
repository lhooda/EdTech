from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from src.models.predictor import predict_from_json

app = FastAPI(title="EdTech Dropout Prediction API")


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
    prediction = predict_from_json(payload)

    return {
        "prediction": int(prediction),
        "interpretation": "Risque de décrochage élevé" if prediction == 1 else "Risque faible"
    }