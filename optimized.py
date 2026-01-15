# On importe le module time uniquement si tu veux mesurer le temps d'exécution (optionnel)
import time


def knapsack_best_gain(actions, budget_max_eur):
    """
    Calcule le gain maximal possible (Knapsack 0/1) sans dépasser budget_max_eur.
    
    actions : liste d'objets ayant au minimum :
        - action.cost  (coût en euros)
        - action.rate  (taux en décimal, ex: 0.27)
        - action.name  (nom)
    
    Retour :
        - meilleur_gain_eur (float)
    """

    # Conversion du budget en centimes (entier) 
    # Exemple : 500€ -> 50000 centimes
    budget_max_cents = int(budget_max_eur * 100)

    # Création de la "mémoire" des meilleurs gains par budget 
    # meilleur_gain[b] = meilleur gain possible (en centimes) avec un budget <= b centimes
    # On crée une liste de taille budget_max_cents + 1, remplie de 0 (De à à 501 car le budget est de 500€ et on prend en compte le 0)
    meilleur_gain = [0] * (budget_max_cents + 1) # Une liste de 501 items

    # On traite chaque action une par une -----
    for action in actions:

        # Conversion du coût de l'action en centimes 
        # Exemple : 34€ = 3400 centimes
        cout_action_cents = int(round(action.cost * 100))

        # Calcul du gain de l'action en centimes 
        # gain = coût * taux
        # Exemple : 34€ * 0.27 = 9.18€ -> 918 centimes
        gain_action_cents = int(round(action.gain * 100))

        # Si une action coûte plus que le budget, elle est inutile ici 
        # (Elle ne pourra jamais être sélectionnée)
        if cout_action_cents > budget_max_cents:
            continue

        # Parcours des budgets du plus grand au plus petit 
        # On parcourt à l'envers pour ne PAS pouvoir prendre l'action plusieurs fois
        for budget_cents in range(budget_max_cents, cout_action_cents - 1, -1): # Cela signifie qu'on part du budget maximum jusqu'au coût de l'action auquel on retire 1

            # Gain sans prendre l'action 
            # "Sans action" = ce qu'on avait déjà de mieux pour ce budget
            gain_sans_action = meilleur_gain[budget_cents] # "budget_cents" représente 50000 puisqu'on part du "budget_max_cents"

            # Gain si on prend l'action
            # Si on prend l'action, il reste : budget_cents - cout_action_cents // On enlève le montant du coût de l'action au budget
            # On ajoute le gain de l'action au meilleur gain connu pour le budget restant
            budget_restant = budget_cents - cout_action_cents #  On enlève le montant du coût de l'action au budget
            gain_avec_action = gain_action_cents + meilleur_gain[budget_restant]

            # On garde le meilleur des deux
            if gain_avec_action > gain_sans_action:
                meilleur_gain[budget_cents] = gain_avec_action

    # Résultat final 
    # Le meilleur gain possible pour le budget max est dans meilleur_gain[budget_max_cents]
    meilleur_gain_cents = meilleur_gain[budget_max_cents]

    # On reconvertit en euros pour l'affichage / retour
    meilleur_gain_eur = meilleur_gain_cents / 100

    return meilleur_gain_eur


# -------------------------
# LANCEMENT DU PROGRAMME
# -------------------------
if __name__ == "__main__":
    # Imports selon ton projet (tu as déjà ça)
    from transformers.transform import Transformer

    CSV_PATH = "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"
    BUDGET_MAX = 500

    transformer = Transformer()
    lecteur = transformer.action_loader(CSV_PATH)
    actions = transformer.transform_data(lecteur)

    # (optionnel) mesurer le temps
    start = time.time()
    meilleur_gain = knapsack_best_gain(actions, BUDGET_MAX)
    end = time.time()

    print("Meilleur gain (en euros) :", meilleur_gain)
    print("Temps d'exécution (sec)  :", round(end - start, 6))
