import pandas as pd
import os

def load_oulad_dataset(base_path="data/raw/oulad"):
    datasets = {}

    files = {
        "studentInfo": "studentInfo.csv",
        "courses": "courses.csv",
        "studentRegistration": "studentRegistration.csv",
        "studentAssessment": "studentAssessment.csv",
        "studentVle": "studentVle.csv",
        "vle": "vle.csv",
        "assessments": "assessments.csv"
    }

    for name, filename in files.items():
        path = os.path.join(base_path, filename)
        datasets[name] = pd.read_csv(path)

    return datasets
