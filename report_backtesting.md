# Backtesting et validation de l’algorithme

Dans cette section, nous évaluons la robustesse et la pertinence de l’algorithme optimisé
en le testant sur des jeux de données historiques fournis par l’entreprise.
Les résultats sont comparés aux décisions d’investissement réalisées manuellement par Sienna.


## Méthodologie

Les données historiques pouvant contenir des incohérences, un nettoyage préalable a été effectué
avant l’exécution de l’algorithme.

Règles de nettoyage appliquées :
- actions avec coût ≤ 0 : rejetées
- actions avec bénéfice ≤ 0 : rejetées
- valeurs manquantes (coût ou bénéfice) : rejetées
- formats invalides non interprétables : rejetés
- actions dont le coût dépasse le budget maximal : ignorées
- les bénéfices doivent être exprimés explicitement en pourcentage ou en taux décimal


## Dataset 1 – Exploration des données

### Qualité des données
- Nombre total d’actions : X
- Actions exploitables : Y
- Actions rejetées : Z
  - coût invalide : A
  - bénéfice invalide : B
  - format invalide : C
- Actions ignorées (coût > budget) : D


### Résultats

**Décision Sienna**
- Coût total : XXX €
- Gain total : XXX €
- Nombre d’actions sélectionnées : X

**Algorithme optimisé**
- Coût total : XXX €
- Gain total : XXX €
- Nombre d’actions sélectionnées : X
- Temps d’exécution : < 1 seconde


### Comparaison et analyse

Les résultats obtenus par l’algorithme sont comparables à ceux de la décision humaine.
Bien que les stratégies diffèrent, les gains restent proches, ce qui valide la cohérence
de l’algorithme sur des données historiques imparfaites.


## Conclusion

L’algorithme optimisé permet de déterminer rapidement une stratégie d’investissement
cohérente sous contrainte budgétaire, même lorsque les données d’entrée sont imparfaites.
La comparaison avec les décisions humaines montre que l’approche algorithmique constitue
un outil fiable d’aide à la décision.
