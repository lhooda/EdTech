import pickle
import pandas as pd

# ============================
# 1) Charger modèle + preprocessor
# ============================
def load_model():
    with open("models/best_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("models/model_columns.pkl", "rb") as f:
        preprocessor = pickle.load(f)

    return model, preprocessor


# ============================
# 2) Vérifier les données d'entrée
# ============================
def validate_input(payload: dict):
    required_cols = [
        "code_module", "code_presentation", "id_student", "gender", "region",
        "highest_education", "imd_band", "age_band", "num_of_prev_attempts",
        "studied_credits", "disability", "final_result", "date_registration",
        "date_unregistration", "avg_score", "total_clicks",
        "low_activity", "low_score", "engagement_score"
    ]

    missing = [col for col in required_cols if col not in payload]
    if missing:
        raise ValueError(f"Colonnes manquantes : {missing}")

    return payload


# ============================
# 3) Fonction principale appelée par l’API
# ============================
def predict_from_json(payload: dict):
    # 1) Vérifier les données
    payload = validate_input(payload)

    # 2) Charger modèle + preprocessor
    model, preprocessor = load_model()

    # 3) Transformer en DataFrame
    X = pd.DataFrame([payload])

    # 4) Appliquer le preprocessor
    X_processed = preprocessor.transform(X)

    # 5) Prédire
    y_pred = model.predict(X_processed)

    return int(y_pred[0])
