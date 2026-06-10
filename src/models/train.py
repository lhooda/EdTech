"""
import mlflow
import mlflow.xgboost
import xgboost as xgb
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def load_data():
    engine = create_engine("postgresql://devuser:devpass123@localhost:5432/edtech_db")
    df = pd.read_sql("SELECT * FROM learning_features", engine)
    return df

def train_model():
    df = load_data()

    X = df.drop(columns=["dropout"])
    y = df["dropout"]

    dtrain = xgb.DMatrix(X, label=y)

    params = {
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "max_depth": 6,
        "eta": 0.1
    }

    with mlflow.start_run():
        model = xgb.train(params, dtrain, num_boost_round=50)

        mlflow.log_params(params)
        mlflow.xgboost.log_model(model, artifact_path="model")

        print("Modèle entraîné et loggé dans MLflow.")

if __name__ == "__main__":
    train_model()

"""


import pickle
import json
import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from src.models.data_preparation import prepare_data


# ============================
# 1) LOAD DATA
# ============================
def load_data():
    df = pd.read_csv("data/processed/ml_dataset.csv")
    return df


# ============================
# 2) TRAIN ALL MODELS
# ============================
def train_all_models():
    df = load_data()
    X_train, X_test, y_train, y_test, preprocessor = prepare_data(df)

    models = {
        "Dummy": DummyClassifier(strategy="most_frequent"),
        "LogisticRegression": LogisticRegression(max_iter=200),
        "DecisionTree": DecisionTreeClassifier(),
        "RandomForest": RandomForestClassifier(n_estimators=200),
        "XGBoost": xgb.XGBClassifier(eval_metric="logloss")
    }

    results = {}

    for name, model in models.items():
        print(f"\n=== Training {name} ===")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        results[name] = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_pred)
        }

    return results, models, preprocessor


# ============================
# 3) SAVE BEST MODEL
# ============================
def save_best_model(results, models, preprocessor):
    best_model_name = max(results, key=lambda m: results[m]["f1"])
    best_model = models[best_model_name]

    print(f"\n>>> Best model: {best_model_name}")

    # Sauvegarde du modèle
    with open("models/best_model.pkl", "wb") as f:
        pickle.dump(best_model, f)

    # Sauvegarde du preprocess (colonnes + transformations)
    with open("models/model_columns.pkl", "wb") as f:
        pickle.dump(preprocessor, f)

    print("Best model saved.")


# ============================
# 4) SAVE METRICS FOR HOUDA
# ============================
def save_metrics(results):
    with open("models/metrics.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Metrics saved for Houda.")


# ============================
# 5) MAIN
# ============================
if __name__ == "__main__":
    results, models, preprocessor = train_all_models()
    save_best_model(results, models, preprocessor)
    save_metrics(results)
