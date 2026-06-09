import pandas as pd

df = pd.read_csv("data/processed/ml_dataset.csv")

print("=== Dimensions du dataset ===")
print(df.shape)

print("\n=== Colonnes ===")
print(df.columns.tolist())

print("\n=== Valeurs manquantes ===")
print(df.isnull().sum())

print("\n=== Répartition dropout ===")
print(df["dropout"].value_counts(normalize=True) * 100)

print("\n=== Statistiques principales ===")
print(df[["avg_score", "total_clicks", "engagement_score"]].describe())

print("\n=== Moyenne par dropout ===")
print(df.groupby("dropout")[["avg_score", "total_clicks", "engagement_score"]].mean())