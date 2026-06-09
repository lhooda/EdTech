# INSIGHTS - Analyse Exploratoire des Données

## Vue générale

Le dataset final contient **32 593 étudiants** et **20 variables** après les étapes de nettoyage, de transformation et de feature engineering.

## Répartition du décrochage

La variable cible **dropout** permet d'identifier les étudiants ayant abandonné leur parcours.

* Étudiants non décrocheurs : **22 560** (69,2 %)
* Étudiants décrocheurs : **10 033** (30,8 %)

Cette répartition est suffisamment équilibrée pour entraîner des modèles de Machine Learning.

## Variables créées

Afin d'améliorer les performances des futurs modèles prédictifs, plusieurs variables ont été construites :

* **avg_score** : moyenne des notes obtenues par l'étudiant.
* **total_clicks** : nombre total d'interactions sur la plateforme pédagogique.
* **low_activity** : indicateur de faible activité sur la plateforme.
* **low_score** : indicateur de faibles performances académiques.
* **engagement_score** : score global mesurant le niveau d'engagement de l'étudiant.

## Premières observations

L'analyse préliminaire met en évidence plusieurs tendances :

* Les étudiants ayant une faible activité sur la plateforme présentent un risque de décrochage plus élevé.
* Les étudiants ayant de faibles résultats académiques semblent davantage exposés au risque d'abandon.
* Les variables liées à l'engagement constituent des indicateurs pertinents pour la prédiction du décrochage.

## Conclusion

Le dataset est désormais prêt pour la phase de Machine Learning. Les variables créées permettront d'entraîner et de comparer plusieurs modèles prédictifs dans le cadre du Jour 3 du projet.
