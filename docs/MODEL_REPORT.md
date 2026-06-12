# MODEL_REPORT.md

# Rapport du Modèle de Machine Learning

## 1. Objectif

L'objectif du projet EdTech Analytics est de développer un modèle capable de prédire le risque de décrochage étudiant à partir de données académiques et comportementales issues de la plateforme d'apprentissage.

Cette prédiction permet d'identifier précocement les étudiants en difficulté afin de mettre en place des actions d'accompagnement adaptées.

---

## 2. Description du Dataset

### Source

Open University Learning Analytics Dataset (OULAD)

### Caractéristiques

| Indicateur          | Valeur  |
| ------------------- | ------- |
| Nombre d'étudiants  | 32 593  |
| Nombre de variables | 20      |
| Variable cible      | dropout |

### Variable cible

```text
dropout = 1 → étudiant décrocheur
dropout = 0 → étudiant non décrocheur
```

---

## 3. Préparation des données

Les données ont été préparées à travers un pipeline ETL comprenant :

* Nettoyage des données
* Traitement des valeurs manquantes
* Suppression des doublons
* Transformation des variables
* Construction de nouvelles variables

### Variables principales utilisées

| Variable         | Description                       |
| ---------------- | --------------------------------- |
| avg_score        | Moyenne des notes                 |
| total_clicks     | Nombre total d'interactions       |
| low_activity     | Faible activité sur la plateforme |
| low_score        | Faibles résultats académiques     |
| engagement_score | Niveau global d'engagement        |

---

## 4. Méthodologie

Les données ont été divisées en :

* 80 % pour l'entraînement
* 20 % pour les tests

La performance des modèles a été évaluée à l'aide des métriques suivantes :

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

---

## 5. Modèles entraînés

Les modèles suivants ont été comparés :

1. Dummy Classifier
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. XGBoost

---

## 6. Résultats des expérimentations

| Modèle              | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------- | --------- | ------ | -------- | ------- |
| Dummy Classifier    | 0.699    | 0.000     | 0.000  | 0.000    | 0.500   |
| Logistic Regression | 0.997    | 0.992     | 0.998  | 0.995    | 0.997   |
| Decision Tree       | 0.999    | 0.998     | 0.999  | 0.998    | 0.999   |
| Random Forest       | 0.998    | 0.995     | 0.999  | 0.997    | 0.999   |
| XGBoost             | 0.999    | 0.999     | 0.997  | 0.998    | 0.998   |

---

## 7. Sélection du modèle

Le modèle retenu pour le déploiement est :

### Decision Tree Classifier

Performances obtenues :

| Métrique  | Valeur  |
| --------- | ------- |
| Accuracy  | 99.91 % |
| Precision | 99.80 % |
| Recall    | 99.89 % |
| F1-Score  | 99.85 % |
| ROC-AUC   | 99.90 % |

---

## 8. Justification du choix

Le modèle Decision Tree a été sélectionné pour plusieurs raisons :

* Excellentes performances globales
* Très faible taux d'erreur
* Interprétabilité élevée
* Temps de prédiction rapide
* Facilité d'intégration dans une API de production

Contrairement aux modèles plus complexes, l'arbre de décision permet également d'expliquer les décisions prises auprès des responsables pédagogiques.

---

## 9. MLOps et Suivi des Expériences

Afin de garantir la traçabilité du projet, les expérimentations ont été suivies avec MLflow.

Fonctionnalités utilisées :

* Suivi des paramètres
* Enregistrement des métriques
* Comparaison des modèles
* Gestion des versions
* Conservation des artefacts

Cette approche garantit la reproductibilité des résultats obtenus.

---

## 10. Déploiement

Le modèle retenu a été intégré dans :

### API FastAPI

Endpoints :

```text
GET /
GET /health
POST /predict
GET /metrics
```

### Dashboard Streamlit

Fonctionnalités :

* Formulaire de prédiction
* Affichage des probabilités
* Jauge de risque
* Liste des étudiants à risque
* Visualisations interactives

---

## 11. Limites

Certaines limites doivent être prises en compte :

* Le dataset provient d'un contexte universitaire spécifique.
* Les comportements étudiants peuvent évoluer dans le temps.
* Le modèle nécessite des données suffisamment complètes pour maintenir ses performances.

---

## 12. Perspectives d'amélioration

Les améliorations futures envisagées sont :

* Réentraînement automatique du modèle
* Déploiement Cloud
* Intégration de nouvelles sources de données
* Alertes automatiques aux responsables pédagogiques
* Explication détaillée des prédictions (Explainable AI)

---

## 13. Conclusion

Les résultats obtenus démontrent la capacité du Machine Learning à détecter efficacement les étudiants présentant un risque de décrochage.

Le modèle Decision Tree atteint un niveau de performance très élevé tout en restant interprétable et facilement déployable.

L'intégration dans une architecture complète associant FastAPI, Streamlit, Docker, MLflow et PostgreSQL permet de proposer une solution opérationnelle de détection précoce du décrochage étudiant.
