import json
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("edtech_dropout_prediction")

with open("models/metrics.json", "r") as f:
    metrics = json.load(f)

for model_name, values in metrics.items():

    with mlflow.start_run(run_name=model_name):

        mlflow.log_param("model", model_name)

        mlflow.log_metric("accuracy", values["accuracy"])
        mlflow.log_metric("precision", values["precision"])
        mlflow.log_metric("recall", values["recall"])
        mlflow.log_metric("f1", values["f1"])
        mlflow.log_metric("roc_auc", values["roc_auc"])

print("MLflow rempli avec succès")
