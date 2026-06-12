#  EdTech Analytics

## Prédiction du risque de décrochage étudiant

EdTech Analytics est une plateforme d'analyse de données éducatives utilisant le Machine Learning pour prédire le risque de décrochage des étudiants.

Le projet permet aux établissements d'enseignement de détecter précocement les étudiants en difficulté afin de mettre en place des actions de suivi adaptées.

---

## Objectifs

- Identifier les étudiants à risque.
- Aider les équipes pédagogiques à prendre des décisions.
- Visualiser les indicateurs clés dans un dashboard interactif.
- Fournir une API de prédiction exploitable.

---

## Fonctionnalités

### Dashboard Streamlit

- Visualisation des données
- Prédiction individuelle
- Probabilité de décrochage
- Étudiants à risque détectés
- Répartition décrocheurs / non décrocheurs
- Importance des variables

### API FastAPI

- Endpoint de prédiction
- Endpoint health check
- Endpoint monitoring

### Machine Learning

- Prétraitement des données
- Entraînement du modèle
- Sauvegarde du modèle
- Évaluation des performances

### Monitoring

- Prometheus
- Grafana

---

## Technologies

- Python
- FastAPI
- Streamlit
- Scikit-Learn
- Pandas
- Plotly
- Docker
- Prometheus
- Grafana

---

## Structure du projet

```text
EdTech/
│
├── data/
├── docs/
├── notebooks/
├── src/
│   ├── api/
│   ├── dashboard/
│   ├── models/
│   └── monitoring/
│
├── docker-compose.yml
├── requirements.txt
└── README.md