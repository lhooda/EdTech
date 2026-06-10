# MODEL REPORT - Jour 3

## Objectif

L'objectif de ce projet est de prédire le risque de décrochage étudiant à partir des données académiques et comportementales issues du dataset OULAD.

---

## Dataset

* Source : OULAD (Open University Learning Analytics Dataset)
* Nombre de lignes : 32 593
* Nombre de variables : 20
* Variable cible : `dropout`

---

## Préparation des données

Les données ont été nettoyées et transformées dans le pipeline ETL.

Les principales features utilisées sont :

* avg_score
* total_clicks
* low_activity
* low_score
* engagement_score

---

## Modèles entraînés

Les modèles suivants ont été testés :

1. Dummy Classifier
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. XGBoost

---

## Résultats

| Modèle              | Accuracy | Precision | Recall | F1-score | ROC-AUC |
| ------------------- | -------- | --------- | ------ | -------- | ------- |
| Dummy               | 0.699    | 0.000     | 0.000  | 0.000    | 0.500   |
| Logistic Regression | 0.997    | 0.992     | 0.998  | 0.995    | 0.997   |
| Decision Tree       | 0.999    | 0.998     | 0.999  | 0.998    | 0.999   |
| Random Forest       | 0.998    | 0.995     | 0.999  | 0.997    | 0.999   |
| XGBoost             | 0.999    | 0.999     | 0.997  | 0.998    | 0.998   |

---

## Modèle retenu

Decision Tree

---

## Justification

Le modèle Decision Tree présente les meilleures performances globales :

* Accuracy : 99.91 %
* Precision : 99.80 %
* Recall : 99.89 %
* F1-score : 99.85 %
* ROC-AUC : 99.90 %

Ce modèle a été sélectionné pour le déploiement dans l'API FastAPI.

---

## MLOps

Les expériences ont été suivies à l'aide de MLflow.

Les métriques des différents modèles ont été enregistrées afin de garantir la traçabilité et la reproductibilité des résultats.

---

## Conclusion

Le modèle Decision Tree a été retenu comme meilleur modèle pour la prédiction du décrochage étudiant. Il sera utilisé lors du Jour 4 pour l'intégration dans l'API et l'interface utilisateur.
