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

import json
import pickle
import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from src.models.data_preparation import prepare_data


def load_data():
    return pd.read_csv("data/processed/ml_dataset.csv")


def train_all_models():
    df = load_data()
    X_train, X_test, y_train, y_test, preprocessor = prepare_data(df)

    models = {
        "Dummy": DummyClassifier(strategy="most_frequent"),
        "LogisticRegression": LogisticRegression(max_iter=500),
        "DecisionTree": DecisionTreeClassifier(max_depth=10, random_state=42),
        "RandomForest": RandomForestClassifier(n_estimators=200, random_state=42),
        "XGBoost": xgb.XGBClassifier(eval_metric="logloss", random_state=42)
    }

    results = {}

    for name, model in models.items():
        print(f"\n=== Training {name} ===")

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        results[name] = {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred, zero_division=0)),
            "recall": float(recall_score(y_test, y_pred, zero_division=0)),
            "f1": float(f1_score(y_test, y_pred, zero_division=0)),
            "roc_auc": float(roc_auc_score(y_test, y_pred))
        }

        if name == "DecisionTree":
            print("\n=== Cross Validation DecisionTree ===")
            cv_scores = cross_val_score(
                model,
                X_train,
                y_train,
                cv=5,
                scoring="f1"
            )

            results[name]["cross_val_f1_scores"] = [float(score) for score in cv_scores]
            results[name]["cross_val_f1_mean"] = float(cv_scores.mean())
            results[name]["cross_val_f1_std"] = float(cv_scores.std())

            print("CV scores:", cv_scores)
            print("CV F1 mean:", cv_scores.mean())
            print("CV F1 std:", cv_scores.std())

    return results, models, preprocessor


def save_best_model(results, models, preprocessor):
    best_model_name = max(results, key=lambda m: results[m]["f1"])
    best_model = models[best_model_name]

    print(f"\n>>> Best model: {best_model_name}")

    with open("models/best_model.pkl", "wb") as f:
        pickle.dump(best_model, f)

    with open("models/model_columns.pkl", "wb") as f:
        pickle.dump(preprocessor, f)

    print("Best model saved.")


def save_metrics(results):
    with open("models/metrics.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Metrics saved for Houda.")


if __name__ == "__main__":
    results, models, preprocessor = train_all_models()
    save_best_model(results, models, preprocessor)
    save_metrics(results)