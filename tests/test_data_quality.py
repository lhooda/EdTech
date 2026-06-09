import pandas as pd

df = pd.read_csv("data/processed/ml_dataset.csv")

def test_dataset_not_empty():
    assert len(df) > 0

def test_dropout_exists():
    assert "dropout" in df.columns

def test_dropout_binary():
    assert set(df["dropout"].unique()).issubset({0, 1})

def test_features_exist():
    required = [
        "avg_score",
        "total_clicks",
        "low_activity",
        "low_score",
        "engagement_score"
    ]

    for col in required:
        assert col in df.columns

def test_no_null_target():
    assert df["dropout"].isnull().sum() == 0