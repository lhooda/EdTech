import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Sécurité : remplir les valeurs manquantes
    df["avg_score"] = df["avg_score"].fillna(0)
    df["total_clicks"] = df["total_clicks"].fillna(0)

    # Feature 1 : étudiant avec faible activité
    df["low_activity"] = (df["total_clicks"] < 100).astype(int)

    # Feature 2 : étudiant avec faible score
    df["low_score"] = (df["avg_score"] < 40).astype(int)

    # Feature 3 : score d'engagement simple
    df["engagement_score"] = df["total_clicks"] * 0.6 + df["avg_score"] * 0.4

    return df