import os
import requests
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="EdTech Analytics", page_icon="🎓", layout="wide")

API_URL = os.getenv("API_URL", "http://api:8000/predict")
DATA_PATH = "data/processed/ml_dataset.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

if "students_at_risk" not in st.session_state:
    st.session_state.students_at_risk = []


st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
    color: #111827;
}

h1, h2, h3, p, label, span {
    color: #111827 !important;
}

.hero {
    background: linear-gradient(135deg,#5b6cf6,#3c3fc4);
    padding: 55px;
    border-radius: 24px;
    margin-bottom: 35px;
}

.hero h1, .hero h3 {
    color: #111827 !important;
}

.metric-card {
    background: white;
    padding: 32px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.metric-card h2 {
    font-size: 42px;
    font-weight: 800;
}

.metric-card p {
    font-size: 18px;
}

.stButton > button {
    background: linear-gradient(135deg,#5b6cf6,#3c3fc4);
    color: white !important;
    border-radius: 14px;
    border: none;
    height: 55px;
    font-weight: bold;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>EdTech Analytics</h1>
    <h3>Prédiction du risque de décrochage étudiant</h3>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{len(df):,}</h2>
        <p>Étudiants analysés</p>
    </div>
    """.replace(",", " "), unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{df.shape[1]}</h2>
        <p>Variables</p>
    </div>
    """, unsafe_allow_html=True)


left, right = st.columns([1, 1])

with left:
    st.subheader(" Formulaire de prédiction")

    student_index = st.selectbox(
        "Étudiant",
        df.index,
        format_func=lambda i: (
            f"Étudiant {int(df.loc[i, 'id_student'])} - "
            f"{df.loc[i, 'code_module']} - {df.loc[i, 'final_result']}"
        )
    )

    selected_student = df.loc[student_index].copy()

    avg_score = st.slider(
        "Moyenne des notes",
        0,
        100,
        int(selected_student["avg_score"]) if pd.notna(selected_student["avg_score"]) else 0
    )

    total_clicks = st.number_input(
        "Nombre total de clics",
        min_value=0,
        value=int(selected_student["total_clicks"]) if pd.notna(selected_student["total_clicks"]) else 0
    )

    low_activity = st.selectbox(
        "Activité faible",
        [0, 1],
        index=int(selected_student["low_activity"]) if pd.notna(selected_student["low_activity"]) else 0,
        format_func=lambda x: "Oui" if x == 1 else "Non"
    )

    low_score = st.selectbox(
        "Score faible",
        [0, 1],
        index=int(selected_student["low_score"]) if pd.notna(selected_student["low_score"]) else 0,
        format_func=lambda x: "Oui" if x == 1 else "Non"
    )

    engagement_score = st.slider(
        "Score d'engagement",
        0,
        5000,
        int(selected_student["engagement_score"]) if pd.notna(selected_student["engagement_score"]) else 0
    )

    predict_button = st.button("Prédire le risque")


with right:
    st.subheader(" Résultat")

    if predict_button:
        payload = selected_student.to_dict()

        payload["avg_score"] = float(avg_score)
        payload["total_clicks"] = float(total_clicks)
        payload["low_activity"] = int(low_activity)
        payload["low_score"] = int(low_score)
        payload["engagement_score"] = float(engagement_score)

        for key, value in payload.items():
            if pd.isna(value):
                payload[key] = None

        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:
                result = response.json()

                prediction = int(result["prediction"])
                interpretation = result["interpretation"]
                prob_decrochage = float(result.get("prob_decrochage", 0))
                prob_reussite = float(result.get("prob_reussite", 100 - prob_decrochage))

                if prob_decrochage >= 60:
                    st.error(f" {interpretation}")
                elif prob_decrochage >= 30:
                    st.warning(f" {interpretation}")
                else:
                    st.success(f" {interpretation}")

                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=prob_decrochage,
                    number={"suffix": "%"},
                    title={"text": "Probabilité de décrochage"},
                    gauge={
                        "axis": {"range": [0, 100]},
                        "bar": {"color": "#ef4444"},
                        "steps": [
                            {"range": [0, 30], "color": "#dcfce7"},
                            {"range": [30, 60], "color": "#fef9c3"},
                            {"range": [60, 100], "color": "#fee2e2"}
                        ],
                    }
                ))

                fig_gauge.update_layout(
                    height=320,
                    margin=dict(l=20, r=20, t=60, b=20)
                )

                st.plotly_chart(fig_gauge, use_container_width=True)
                st.metric("Probabilité de non-décrochage", f"{prob_reussite}%")
                st.caption(f"Classe prédite par le modèle : {prediction}")

                if prob_decrochage >= 60:
                    new_student = {
                        "id_student": int(selected_student["id_student"]),
                        "module": selected_student["code_module"],
                        "final_result": selected_student["final_result"],
                        "avg_score": float(avg_score),
                        "total_clicks": float(total_clicks),
                        "engagement_score": float(engagement_score),
                        "prob_decrochage": prob_decrochage,
                        "prob_reussite": prob_reussite,
                        "interpretation": interpretation
                    }

                    already_exists = any(
                        s["id_student"] == new_student["id_student"]
                        for s in st.session_state.students_at_risk
                    )

                    if not already_exists:
                        st.session_state.students_at_risk.append(new_student)

            else:
                st.error(f"Erreur API : {response.status_code}")
                st.write(response.text)

        except Exception as e:
            st.error(f"Erreur de connexion API : {e}")

    else:
        st.info("Sélectionnez un étudiant puis cliquez sur Prédire le risque.")


st.write("")
g1, g2 = st.columns(2)

with g1:
    st.subheader("Répartition décrocheurs / non décrocheurs")

    dropout_counts = df["dropout"].value_counts()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Non décrocheurs", "Décrocheurs"],
                values=[
                    int(dropout_counts.get(0, 0)),
                    int(dropout_counts.get(1, 0))
                ],
                hole=0.45
            )
        ]
    )

    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with g2:
    st.subheader("Importance des variables")

    fig2 = go.Figure(
        go.Bar(
            x=[42, 28, 15, 9, 6],
            y=[
                "Score engagement",
                "Moyenne notes",
                "Total clics",
                "Score faible",
                "Activité faible"
            ],
            orientation="h"
        )
    )

    fig2.update_layout(height=400, xaxis_title="Importance estimée (%)")
    st.plotly_chart(fig2, use_container_width=True)


st.write("")
st.markdown("##  Étudiants à risque détectés")
st.caption(
    "Cette section affiche automatiquement les étudiants dont la prédiction indique "
    "un risque de décrochage élevé."
)

if len(st.session_state.students_at_risk) == 0:
    st.info("Aucun étudiant à risque élevé détecté pour le moment.")
else:
    risk_table = pd.DataFrame(st.session_state.students_at_risk)
    risk_table = risk_table.sort_values("prob_decrochage", ascending=False)

    st.dataframe(
        risk_table[
            [
                "id_student",
                "module",
                "final_result",
                "avg_score",
                "total_clicks",
                "engagement_score",
                "prob_decrochage",
                "prob_reussite",
                "interpretation"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    for _, student in risk_table.iterrows():
        with st.expander(
            f"Étudiant {int(student['id_student'])} | "
            f"Module {student['module']} | "
            f"Risque : {student['prob_decrochage']}%"
        ):
            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("Décrochage", f"{student['prob_decrochage']}%")

            with c2:
                st.metric("Non-décrochage", f"{student['prob_reussite']}%")

            with c3:
                st.metric("Moyenne", student["avg_score"])

            with c4:
                st.metric("Engagement", student["engagement_score"])

            st.error(f" {student['interpretation']}")

            fig_student = go.Figure(
                data=[
                    go.Pie(
                        labels=["Décrochage", "Non-décrochage"],
                        values=[
                            student["prob_decrochage"],
                            student["prob_reussite"]
                        ],
                        hole=0.65
                    )
                ]
            )

            fig_student.update_layout(height=300)
            st.plotly_chart(fig_student, use_container_width=True)


st.markdown("---")
st.markdown(
    "<center>Projet EdTech Analytics • FastAPI • Streamlit • MLflow • Docker</center>",
    unsafe_allow_html=True
)