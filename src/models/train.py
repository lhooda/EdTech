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
