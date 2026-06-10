import pickle
import pandas as pd

# ============================
# 1) Charger le modèle
# ============================
with open("models/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# ============================
# 2) Charger le preprocessor
# ============================
with open("models/model_columns.pkl", "rb") as f:
    preprocessor = pickle.load(f)

print("✅ Modèle et preprocessor chargés.")


# ============================
# 3) Exemple de données (tiré de ton CSV)
# ============================
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
    "dropout": 0,
    "low_activity": 0,
    "low_score": 0,
    "engagement_score": 593.2
}

print("📌 Exemple chargé.")


# ============================
# 4) Fonction de prédiction
# ============================
def predict_example(example_dict):
    X = pd.DataFrame([example_dict])
    X_processed = preprocessor.transform(X)
    y_pred = model.predict(X_processed)
    return int(y_pred[0])


# ============================
# 5) Lancer la prédiction
# ============================
result = predict_example(example)
print("🎯 Prédiction du modèle :", result)
