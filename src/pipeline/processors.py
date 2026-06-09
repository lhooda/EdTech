import pandas as pd

def preprocess_oulad(datasets):
    student_info = datasets["studentInfo"]
    registration = datasets["studentRegistration"]
    assessments = datasets["studentAssessment"]
    vle = datasets["studentVle"]

    # Nettoyage
    student_info = student_info.dropna(subset=["gender", "age_band"])
    registration = registration.dropna(subset=["date_registration"])

    # Fusion
    df = student_info.merge(
        registration,
        on=["id_student", "code_module", "code_presentation"],
        how="left"
    )

    # Moyenne des scores
    avg_scores = assessments.groupby("id_student")["score"].mean().reset_index()
    avg_scores.rename(columns={"score": "avg_score"}, inplace=True)
    df = df.merge(avg_scores, on="id_student", how="left")

    # Activité VLE
    vle_activity = vle.groupby("id_student")["sum_click"].sum().reset_index()
    vle_activity.rename(columns={"sum_click": "total_clicks"}, inplace=True)
    df = df.merge(vle_activity, on="id_student", how="left")

    # Remplir les NaN
    df["avg_score"] = df["avg_score"].fillna(0)
    df["total_clicks"] = df["total_clicks"].fillna(0)

    # Variable cible
    df["dropout"] = df["date_unregistration"].notna().astype(int)

    return df
