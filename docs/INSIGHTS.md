# INSIGHTS.md

# Analyse Exploratoire des Données (EDA)

## 1. Objectif

Cette phase vise à explorer et comprendre les données du dataset OULAD afin d'identifier les facteurs susceptibles d'influencer le décrochage étudiant.

L'objectif est également de construire des variables pertinentes pour améliorer les performances du modèle de Machine Learning.

---

## 2. Description du dataset

Après les étapes de nettoyage et de préparation, le dataset final contient :

| Indicateur          | Valeur  |
| ------------------- | ------- |
| Nombre d'étudiants  | 32 593  |
| Nombre de variables | 20      |
| Variable cible      | dropout |

Le dataset regroupe des informations académiques, comportementales et d'engagement relatives aux étudiants de l'Open University.

---

## 3. Répartition du décrochage

La variable cible **dropout** permet d'identifier les étudiants ayant abandonné leur parcours académique.

| Classe          | Nombre | Pourcentage |
| --------------- | ------ | ----------- |
| Non décrocheurs | 22 560 | 69,2 %      |
| Décrocheurs     | 10 033 | 30,8 %      |

Cette distribution reste suffisamment équilibrée pour permettre l'entraînement de modèles de classification sans déséquilibre majeur.

---

## 4. Variables construites

Dans le cadre du Feature Engineering, plusieurs variables ont été créées afin de mieux représenter le comportement des étudiants.

### Variables académiques

* **avg_score** : moyenne générale obtenue par l'étudiant.
* **low_score** : indicateur signalant un niveau académique faible.

### Variables comportementales

* **total_clicks** : nombre total d'interactions sur la plateforme.
* **low_activity** : indicateur de faible activité numérique.

### Variables d'engagement

* **engagement_score** : score synthétique représentant le niveau global d'engagement de l'étudiant.

---

## 5. Analyse des comportements

L'analyse exploratoire a permis d'identifier plusieurs tendances importantes.

### Impact de l'activité numérique

Les étudiants ayant peu d'interactions avec la plateforme pédagogique présentent généralement un risque de décrochage plus élevé.

Une diminution du nombre de connexions et des interactions constitue souvent un signal précoce de désengagement.

### Impact des performances académiques

Les étudiants obtenant des résultats faibles aux évaluations sont davantage exposés au risque d'abandon.

La moyenne des notes apparaît comme un indicateur fortement corrélé au décrochage.

### Importance de l'engagement

Le score d'engagement constitue l'un des indicateurs les plus discriminants.

Les étudiants les plus actifs et impliqués dans les activités pédagogiques présentent généralement une probabilité de réussite plus importante.

---

## 6. Variables les plus influentes

Les analyses réalisées montrent que les facteurs suivants jouent un rôle majeur dans la prédiction :

| Rang | Variable              |
| ---- | --------------------- |
| 1    | Engagement Score      |
| 2    | Moyenne des notes     |
| 3    | Nombre total de clics |
| 4    | Score faible          |
| 5    | Activité faible       |

Ces variables ont été retenues comme principales caractéristiques pour l'entraînement du modèle prédictif.

---

## 7. Enseignements clés

Les principaux enseignements issus de l'analyse sont :

* Une faible activité sur la plateforme est souvent associée à un risque accru de décrochage.
* Les performances académiques influencent fortement la probabilité de réussite.
* L'engagement étudiant constitue un indicateur précoce particulièrement pertinent.
* Les données comportementales permettent de détecter les étudiants en difficulté avant l'abandon effectif.

---

## 8. Conclusion

L'analyse exploratoire confirme que les données collectées contiennent des signaux pertinents permettant d'anticiper le décrochage étudiant.

Les variables construites au cours de cette phase constituent une base solide pour l'entraînement des modèles de Machine Learning développés dans la suite du projet.

Ces résultats justifient la mise en place d'un système de détection précoce capable d'aider les établissements à identifier rapidement les étudiants nécessitant un accompagnement pédagogique.
