# ARCHITECTURE.md

# Architecture du projet EdTech Analytics

## 1. Présentation

EdTech Analytics est une plateforme de Learning Analytics permettant de prédire le risque de décrochage étudiant à partir des données académiques et comportementales des apprenants.

L'objectif est d'aider les universités et les écoles à détecter précocement les étudiants en difficulté afin de mettre en place des actions de suivi adaptées.

---

## 2. Architecture générale

```text
Dataset OULAD
      │
      ▼
Prétraitement des données
(Pandas)
      │
      ▼
Machine Learning
(Scikit-Learn)
      │
      ▼
API FastAPI
      │
      ▼
Dashboard Streamlit
      │
      ▼
Utilisateur final
```

---

## 3. Pipeline de données

### Étape 1 : Collecte

Le projet utilise le dataset public OULAD (Open University Learning Analytics Dataset).

Les données contiennent :

* informations étudiants
* résultats académiques
* activité sur la plateforme
* interactions pédagogiques

---

### Étape 2 : Prétraitement

Les données sont nettoyées avec Pandas :

* suppression des doublons
* gestion des valeurs manquantes
* transformation des variables
* fusion des tables

---

### Étape 3 : Feature Engineering

Création des variables utilisées par le modèle :

* avg_score
* total_clicks
* engagement_score
* low_score
* low_activity

---

### Étape 4 : Machine Learning

Le modèle est entraîné pour prédire :

```text
0 = Non décrocheur
1 = Décrocheur
```

Le modèle produit :

* une classe prédite
* une probabilité de décrochage
* une probabilité de réussite

---

## 4. API FastAPI

L'API expose plusieurs endpoints :

```text
GET /
GET /health
POST /predict
GET /metrics
```

Fonctions :

* recevoir les données étudiant
* lancer la prédiction
* retourner les probabilités

---

## 5. Dashboard Streamlit

Le dashboard permet :

### Formulaire de prédiction

* sélection d'un étudiant
* modification des variables
* lancement d'une prédiction

### Visualisations

* jauge de risque
* répartition décrocheurs / non décrocheurs
* importance des variables

### Détection des étudiants à risque

Les étudiants dont la probabilité de décrochage est élevée sont automatiquement affichés dans une section dédiée afin de faciliter leur suivi.

---

## 6. Monitoring

### Prometheus

Collecte :

* nombre de prédictions
* temps de réponse
* métriques système

Endpoint :

```text
/metrics
```

### Grafana

Visualisation :

* performances API
* nombre de requêtes
* suivi des prédictions

---

## 7. Technologies utilisées

| Technologie  | Utilisation             |
| ------------ | ----------------------- |
| Python       | Développement principal |
| Pandas       | Prétraitement           |
| Scikit-Learn | Machine Learning        |
| FastAPI      | API REST                |
| Streamlit    | Dashboard               |
| Plotly       | Visualisations          |
| Docker       | Conteneurisation        |
| Prometheus   | Monitoring              |
| Grafana      | Dashboard de monitoring |

---

## 8. Conclusion

L'architecture mise en place couvre l'ensemble de la chaîne de valeur d'un projet Data & IA : préparation des données, entraînement du modèle, exposition via API, visualisation dans un dashboard et monitoring de l'application.
