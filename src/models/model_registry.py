import mlflow
from mlflow.tracking import MlflowClient

MLFLOW_TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "edtech_dropout_prediction"
MODEL_NAME = "edtech_dropout_model"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


def get_best_decision_tree_run():
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)

    if experiment is None:
        raise ValueError(f"Expérience introuvable : {EXPERIMENT_NAME}")

    runs = mlflow.search_runs(
    experiment_ids=[experiment.experiment_id],
    filter_string="tags.mlflow.runName = 'DecisionTree_Production_Model'",
    order_by=["start_time DESC"],
    max_results=1
    )
    if runs.empty:
        raise ValueError("Aucun run 'Arbre de décision' trouvé dans MLflow")

    run_id = runs.iloc[0]["run_id"]
    return run_id


def register_model():
    client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

    run_id = get_best_decision_tree_run()

    model_uri = f"runs:/{run_id}/model"

    registered_model = mlflow.register_model(
        model_uri=model_uri,
        name=MODEL_NAME
    )

    client.set_registered_model_alias(
        name=MODEL_NAME,
        alias="Production",
        version=registered_model.version
    )

    print("Modèle enregistré dans MLflow Registry")
    print("Nom :", MODEL_NAME)
    print("Version :", registered_model.version)
    print("Alias : Production")


if __name__ == "__main__":
    register_model()
