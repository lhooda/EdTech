# BACKLOG AGILE - Projet EdTech Analytics

## Sprint Jour 1 - Infrastructure & Architecture

### Tâches réalisées

* Création du repository GitHub
* Mise en place de l'architecture du projet
* Création du document ARCHITECTURE.md
* Configuration Docker Compose
* Déploiement PostgreSQL
* Déploiement MLflow
* Déploiement FastAPI
* Déploiement Streamlit
* Tests de communication entre services

### Statut

✅ Terminé

---

## Sprint Jour 2 - Data Pipeline & Processing

### Ingestion des données

* Chargement du dataset OULAD
* Création de data_loader.py

### ETL

* Nettoyage des données
* Gestion des valeurs manquantes
* Fusion des tables OULAD
* Création du dataset consolidé

### Feature Engineering

* Création de avg_score
* Création de total_clicks
* Création de dropout
* Création de low_activity
* Création de low_score
* Création de engagement_score
* Création du module feature_engineering.py

### Stockage

* Génération de ml_dataset.csv
* Sauvegarde dans data/processed/

### Tests

* Exécution complète de la pipeline
* Validation du dataset final

### Statut

🟡 En cours (90%)

### Reste à faire

* Analyse exploratoire des données (EDA)
* Contrôle qualité des données
* Documentation des insights

---

## Sprint Jour 3 - Machine Learning & MLflow

### À réaliser

* Séparation Train/Test
* Modèle Baseline
* Logistic Regression
* Random Forest
* XGBoost
* Évaluation des performances
* Tracking MLflow
* Enregistrement du meilleur modèle

### Statut

⏳ À faire

---

## Sprint Jour 4 - API & Dashboard

### À réaliser

* Endpoint prédiction FastAPI
* Endpoint statistiques
* Connexion MLflow
* Dashboard Streamlit
* Visualisations interactives

### Statut

⏳ À faire

---

## Sprint Jour 5 - Monitoring & Présentation

### À réaliser

* Tests end-to-end
* Documentation finale
* README
* Préparation du pitch
* Démonstration

### Statut

⏳ À faire
