import streamlit as st
import requests

st.set_page_config(page_title="EdTech Analytics", layout="wide")

st.title("EdTech Analytics")
st.subheader("Prédiction du risque de décrochage étudiant")

api_url = "http://api:8000"

avg_score = st.slider("Moyenne des notes", 0, 100, 50)
total_clicks = st.slider("Nombre total de clics", 0, 5000, 500)

low_activity = 1 if total_clicks < 100 else 0
low_score = 1 if avg_score < 40 else 0
engagement_score = total_clicks * 0.6 + avg_score * 0.4

st.write("Faible activité :", low_activity)
st.write("Faible score :", low_score)
st.write("Score d'engagement :", round(engagement_score, 2))

if st.button("Tester la connexion API"):
    try:
        response = requests.get(f"{api_url}/health")
        st.success(response.json())
    except Exception as e:
        st.error(f"Erreur API : {e}")