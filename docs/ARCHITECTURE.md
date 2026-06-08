# Architecture du projet EdTech Analytics

## 1. Présentation du projet

Le projet **EdTech Analytics** vise à développer une plateforme intelligente permettant d’analyser les données pédagogiques des étudiants et de prédire le risque de décrochage.

L’objectif est d’aider les responsables pédagogiques à identifier rapidement les étudiants à risque afin de mettre en place des actions d’accompagnement adaptées.

---

## 2. Objectif de l’architecture

L’architecture du projet repose sur une approche **end-to-end Data & IA**.

Elle permet de couvrir tout le cycle de vie d’un projet data :

1. collecte des données,
2. nettoyage et préparation,
3. stockage,
4. entraînement du modèle de Machine Learning,
5. suivi des expériences avec MLflow,
6. exposition du modèle via API,
7. visualisation dans un dashboard,
8. monitoring applicatif.

---

## 3. Architecture globale

```text
Données OULAD / CSV
        │
        ▼
Collecte des données
src/data_collection/collect_oulad.py
        │
        ▼
Prétraitement des données
src/data_preprocessing/clean_oulad.py
        │
        ▼
Feature Engineering
Création des variables utiles pour le ML
        │
        ▼
Stockage des données
PostgreSQL / fichiers processed
        │
        ▼
Machine Learning
Scikit-learn / XGBoost
        │
        ▼
Tracking MLOps
MLflow
        │
        ▼
API de prédiction
FastAPI
        │
        ▼
Dashboard utilisateur
Streamlit
        │
        ▼
Monitoring
Prometheus / Grafana
```

---

## 4. Architecture des données

Le projet utilise le dataset public **OULAD (Open University Learning Analytics Dataset)**.

Les données sont organisées en trois niveaux.

### 4.1 Données brutes

Les fichiers bruts sont stockés dans :

```text
data/oulad/
```

Fichiers utilisés :

```text
assessments.csv
courses.csv
studentAssessment.csv
studentInfo.csv
studentRegistration.csv
studentVle.csv
vle.csv
```

### 4.2 Données nettoyées

Après nettoyage, les données sont stockées dans :

```text
data/processed/
```

Exemples de fichiers générés :

```text
students_clean.csv
activities_clean.csv
assessments_clean.csv
```

### 4.3 Dataset final pour le Machine Learning

Le dataset final prêt pour l’entraînement du modèle est stocké dans :

```text
data/ml_ready/ml_dataset.csv
```

Il contient les variables nécessaires à la prédiction du risque de décrochage.

---

## 5. Variables utilisées

### Informations étudiant

| Variable          | Description               |
| ----------------- | ------------------------- |
| student_id        | Identifiant étudiant      |
| age_band          | Tranche d’âge             |
| gender            | Sexe                      |
| highest_education | Niveau d’études           |
| region            | Région                    |
| disability        | Situation de handicap     |
| studied_credits   | Nombre de crédits étudiés |

### Variables comportementales

| Variable              | Description                |
| --------------------- | -------------------------- |
| login_count           | Nombre de connexions       |
| total_clicks          | Nombre total de clics      |
| activity_days         | Nombre de jours d’activité |
| forum_activity        | Activité sur les forums    |
| assignments_completed | Nombre de devoirs rendus   |

### Variables académiques

| Variable        | Description             |
| --------------- | ----------------------- |
| average_score   | Moyenne des notes       |
| final_score     | Score final             |
| attendance_rate | Taux de présence estimé |

### Variable cible

| Variable | Description          |
| -------- | -------------------- |
| dropout  | Risque de décrochage |

Définition :

```text
dropout = 1 : étudiant à risque de décrochage
dropout = 0 : étudiant non à risque
```

---

## 6. Architecture technique

### 6.1 PostgreSQL

PostgreSQL est utilisé pour stocker les données structurées du projet.

Rôle :

* stocker les données étudiantes,
* stocker les données nettoyées,
* permettre les requêtes analytiques,
* préparer l’intégration avec l’API et le dashboard.

### 6.2 FastAPI

FastAPI est utilisé pour créer l’API backend du projet.

Rôle :

* exposer le modèle de prédiction,
* recevoir les données d’un étudiant,
* retourner un score de risque de décrochage,
* fournir des endpoints de santé et de statistiques.

Endpoints prévus :

```text
GET /
GET /health
GET /students
POST /predict
GET /metrics
```

### 6.3 Streamlit

Streamlit est utilisé pour créer le dashboard interactif.

Rôle :

* visualiser les indicateurs clés,
* afficher les graphiques d’analyse,
* permettre une prédiction via formulaire,
* rendre la démonstration accessible au jury.

### 6.4 MLflow

MLflow est utilisé pour le suivi MLOps.

Rôle :

* suivre les expériences,
* enregistrer les paramètres des modèles,
* comparer les métriques,
* versionner le meilleur modèle.

### 6.5 Prometheus et Grafana

Prometheus et Grafana sont utilisés pour le monitoring.

Rôle :

* suivre le nombre de requêtes API,
* mesurer le temps de réponse,
* surveiller les erreurs,
* visualiser les métriques techniques.

### 6.6 Docker Compose

Docker Compose est utilisé pour orchestrer les services du projet.

Services prévus :

```text
postgres
fastapi
streamlit
mlflow
prometheus
grafana
```

---

## 7. Flux de données détaillé

```text
1. Les fichiers CSV OULAD sont placés dans data/oulad/

2. Le script collect_oulad.py vérifie la présence des fichiers nécessaires.

3. Le script clean_oulad.py nettoie les données :
   - valeurs manquantes,
   - doublons,
   - types de colonnes,
   - jointures entre fichiers.

4. Le feature engineering crée des variables utiles :
   - total_clicks,
   - login_count,
   - activity_days,
   - assignments_completed,
   - average_score,
   - dropout.

5. Le dataset final est sauvegardé dans data/ml_ready/ml_dataset.csv.

6. Les modèles ML sont entraînés sur ce dataset.

7. MLflow enregistre les expériences et les performances.

8. Le meilleur modèle est exposé via FastAPI.

9. Streamlit consomme l’API et affiche les résultats.

10. Prometheus et Grafana surveillent l’application.
```

---

## 8. Justification des choix technologiques

| Technologie    | Justification                                      |
| -------------- | -------------------------------------------------- |
| Python         | Langage principal pour Data Science et IA          |
| Pandas         | Nettoyage et manipulation des données              |
| PostgreSQL     | Base relationnelle fiable et structurée            |
| Scikit-learn   | Modèles ML classiques et robustes                  |
| XGBoost        | Modèle performant pour la classification           |
| MLflow         | Suivi des expériences et versionnement des modèles |
| FastAPI        | API rapide, moderne et adaptée au déploiement ML   |
| Streamlit      | Dashboard rapide à développer                      |
| Docker Compose | Orchestration locale simple et professionnelle     |
| Prometheus     | Collecte des métriques techniques                  |
| Grafana        | Visualisation des métriques de monitoring          |

---

## 9. Structure du projet

```text
EDTECH-ANALYTICS/
│
├── data/
│   ├── oulad/
│   ├── processed/
│   └── ml_ready/
│
├── src/
│   ├── data_collection/
│   │   └── collect_oulad.py
│   │
│   ├── data_preprocessing/
│   │   └── clean_oulad.py
│   │
│   ├── feature_engineering/
│   │   └── build_features.py
│   │
│   ├── models/
│   │   ├── train_model.py
│   │   └── predict.py
│   │
│   └── api/
│       └── main.py
│
├── dashboard/
│   └── app.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── BACKLOG.md
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── tests/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 10. Contraintes respectées

| Contrainte                             | Statut   |
| -------------------------------------- | -------- |
| Docker Compose avec minimum 3 services | Respecté |
| Repository Git versionné               | Respecté |
| Pipeline de données                    | Prévu    |
| Machine Learning                       | Prévu    |
| MLflow tracking et registry            | Prévu    |
| API REST                               | Prévu    |
| Dashboard interactif                   | Prévu    |
| Monitoring                             | Prévu    |
| Documentation technique                | Respecté |

---

## 11. Risques techniques

| Risque                | Solution                                     |
| --------------------- | -------------------------------------------- |
| Dataset complexe      | Commencer avec un sous-ensemble simple       |
| Temps limité          | Développer d’abord un MVP fonctionnel        |
| Modèle peu performant | Comparer plusieurs modèles                   |
| Erreurs Docker        | Tester les services un par un                |
| Démo instable         | Préparer une version locale simple et testée |

---

## 12. MVP retenu

Le MVP du projet comprend :

* un dataset nettoyé,
* un modèle ML entraîné,
* un suivi MLflow,
* une API FastAPI avec endpoint `/predict`,
* un dashboard Streamlit,
* une architecture Docker Compose fonctionnelle.

---

## 13. Conclusion

Cette architecture permet de construire une plateforme complète de Learning Analytics, depuis les données brutes jusqu’à la visualisation des prédictions.

Elle répond aux exigences du projet M1 Data & IA en intégrant les dimensions Data Engineering, Machine Learning, MLOps, API, dashboard et monitoring.
