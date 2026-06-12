# BACKLOG_AGILE.md

# Backlog Agile – Projet EdTech Analytics

## DONE 

### Sprint 1 – Mise en place de l'infrastructure

* Création de l'architecture globale du projet
* Configuration de Docker Compose
* Déploiement des conteneurs :

  * FastAPI
  * Streamlit
  * PostgreSQL
  * MLflow
* Configuration des volumes Docker
* Validation de la communication entre services

---

### Sprint 2 – Data Engineering

* Import du dataset OULAD
* Analyse exploratoire des données (EDA)
* Nettoyage des données
* Gestion des valeurs manquantes
* Suppression des doublons
* Transformation des variables
* Création des indicateurs comportementaux
* Construction du dataset final pour le Machine Learning
* Validation qualité des données

---

### Sprint 3 – Machine Learning

* Définition de la variable cible (dropout)
* Séparation Train / Test
* Entraînement de plusieurs modèles :

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Gradient Boosting
  * XGBoost
* Comparaison des performances
* Sélection du meilleur modèle
* Sauvegarde du modèle final

---

### Sprint 4 – MLOps

* Intégration de MLflow
* Tracking des expériences
* Enregistrement des métriques
* Versionnement des modèles
* Comparaison des résultats

---

### Sprint 5 – API FastAPI

* Création de l'endpoint `/`
* Création de l'endpoint `/health`
* Création de l'endpoint `/predict`
* Chargement automatique du modèle
* Retour des probabilités de prédiction
* Tests des endpoints

---

### Sprint 6 – Dashboard Streamlit

* Création de l'interface utilisateur
* Formulaire de prédiction étudiant
* Affichage des probabilités de décrochage
* Visualisation par jauge dynamique
* Répartition décrocheurs / non décrocheurs
* Importance des variables
* Tableau des étudiants à risque détectés
* Visualisation détaillée des étudiants à risque

---

### Sprint 7 – Monitoring

* Intégration Prometheus
* Collecte des métriques API
* Configuration Grafana
* Création des dashboards de monitoring

---

## TODO 

### Améliorations futures

* Ajout d'alertes automatiques pour les étudiants à risque
* Envoi d'emails aux responsables pédagogiques
* Mise à jour automatique des données
* Déploiement Cloud (AWS / Azure)
* Authentification utilisateurs
* Tableau de bord multi-écoles
* Réentraînement automatique du modèle

---

## MVP Livré 

Le MVP final comprend :

* Pipeline de données complet
* Modèle de Machine Learning opérationnel
* Tracking MLflow
* API FastAPI
* Dashboard Streamlit interactif
* Monitoring Prometheus/Grafana
* Déploiement Docker Compose

---

## État du projet

| Fonctionnalité      | Statut      |
| ------------------- | ----------- |
| Data Engineering    | Terminé   |
| Machine Learning    | Terminé   |
| API FastAPI         | Terminé   |
| Dashboard Streamlit | Terminé   |
| MLflow              | Terminé   |
| Docker              | Terminé   |
| Monitoring          | Terminé   |
| Documentation       | Terminée  |

