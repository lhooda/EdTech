from src.pipeline.data_loader import load_oulad_dataset
from src.pipeline.processors import preprocess_oulad
import os

def run():
    datasets = load_oulad_dataset()

    df = preprocess_oulad(datasets)

    print(df.head())
    print("Shape:", df.shape)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(
        "data/processed/ml_dataset.csv",
        index=False
    )

    print("Dataset sauvegardé dans data/processed/ml_dataset.csv")

if __name__ == "__main__":
    run()