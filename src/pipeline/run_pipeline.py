import os
import pandas as pd
from src.pipeline.feature_engineering import add_features

def run():
    df = pd.read_csv("data/processed/ml_dataset.csv")

    df = add_features(df)

    print(df.head())
    print("Shape:", df.shape)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/ml_dataset.csv", index=False)

    print("Features ajoutées et dataset sauvegardé dans data/processed/ml_dataset.csv")

if __name__ == "__main__":
    run()