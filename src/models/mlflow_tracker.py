import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

EXPERIMENT_NAME = "edtech_dropout_prediction"

def setup_mlflow():
    mlflow.set_experiment(EXPERIMENT_NAME)
    print(f"Experiment : {EXPERIMENT_NAME}")