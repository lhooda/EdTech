from src.models.predictor import predict_from_json

example = {
    "code_module": "AAA",
    "code_presentation": "2013J",
    "id_student": 11391,
    "gender": "M",
    "region": "East Anglian Region",
    "highest_education": "HE Qualification",
    "imd_band": "90-100%",
    "age_band": "55<=",
    "num_of_prev_attempts": 0,
    "studied_credits": 240,
    "disability": "N",
    "final_result": "Pass",
    "date_registration": -159.0,
    "date_unregistration": None,
    "avg_score": 82.0,
    "total_clicks": 934.0,
    "low_activity": 0,
    "low_score": 0,
    "engagement_score": 593.2
}

print("Prédiction :", predict_from_json(example))
