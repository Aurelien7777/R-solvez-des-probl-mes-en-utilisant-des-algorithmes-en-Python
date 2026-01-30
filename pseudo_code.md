1) Charger les actions depuis le CSV
2) Nettoyer les données (coût > 0, bénéfice > 0, etc.)
3) Pour chaque action :
       gain = coût * taux

4) Convertir le budget en centimes (pour travailler en entiers)
       budget_max = 50000

5) Créer une liste "meilleur_gain" de taille budget_max + 1
       meilleur_gain[b] = meilleur gain possible avec un budget <= b
       Initialiser toutes les cases à 0

6) Pour chaque action (coût_c, gain_c) :
       Pour budget b allant de budget_max vers coût_c :
            gain_sans = meilleur_gain[b]
            gain_avec = gain_c + meilleur_gain[b - coût_c]
            meilleur_gain[b] = max(gain_sans, gain_avec)

7) Le meilleur gain final est :
       meilleur_gain[budget_max]



Parcours du budget à l’envers : garantit qu’une action n’est jamais prise deux fois (0/1)

## Complexité :

Temps : O(n × budget)
Mémoire : O(budget)
Conversion en centimes : évite les erreurs d’arrondi des floats et permet des index entiers



## Limites (slide dédiée ou bullet)

Si budget énorme ou précision très fine → DP plus coûteux
Données invalides (coût/bénéfice manquants) → doivent être nettoyées