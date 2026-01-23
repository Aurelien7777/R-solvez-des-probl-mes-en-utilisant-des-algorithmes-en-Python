import time

def knapsack_best_gain(actions, budget_max_eur):
    """
    Calcule le gain maximal possible avec la méthode KNAPSACK sans dépasser le budget maximum
    """

    # Conversion du budget en centimes (entier) 
    # Exemple : 500€ -> 50000 centimes
    budget_max_cents = int(budget_max_eur * 100)

    # Création de la "mémoire" des meilleurs gains par budget 
    # meilleur_gain[b] = meilleur gain possible (en centimes) avec un budget <= b centimes
    # On crée une liste de taille budget_max_cents + 1, remplie de 0 (De à à 501 car le budget est de 500€ et on prend en compte le 0)
    meilleur_gain = [0] * (budget_max_cents + 1) # Une liste de 501 items

    # On traite chaque action une par une 
    for action in actions:
        print(f"----- TRAITEMENT DE L'ACTION {action.name} -----")
        
        # Conversion du coût de l'action en centimes 
        # Exemple : 34€ = 3400 centimes
        cout_action_cents = int(round(action.cost * 100))
        print(f"----- COÛT DE L'ACTION : {cout_action_cents} -----")
        
        # Calcul du gain de l'action en centimes 
        # gain = coût * taux
        # Exemple : 34€ * 0.27 = 9.18€ -> 918 centimes
        gain_action_cents = int(round(action.gain * 100))
        print(f"----- GAIN DE L'ACTION : {gain_action_cents} -----\n")
        
        # Si une action coûte plus que le budget, elle est inutile ici 
        if cout_action_cents > budget_max_cents:
            continue

        # Parcours des budgets du plus grand au plus petit 
        # On parcourt à l'envers pour ne PAS pouvoir prendre l'action plusieurs fois
        # cout_action_cents - 1 sert juste à inclure le budget égal au coût de l’action.
        # Cela signifie qu'on part du budget maximum jusqu'au coût de l'action auquel on retire 1
        for budget_cents in range(budget_max_cents, cout_action_cents - 1, -1): 
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

    print(f"AFFICHAGE DE LA LISTE : {meilleur_gain}")
    print(len(meilleur_gain))
    print()
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
    from transformers.transform import Transformer

    CSV_PATH = "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"
    DATASET1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset1_Python+P7.csv"
    DATASET2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset2_Python+P7.csv"
    BUDGET_MAX = 500

    transformer = Transformer()
    lecteur = transformer.action_loader(CSV_PATH)
    actions = transformer.transform_data(lecteur)

    # (optionnel) mesurer le temps
    start = time.time()
    print("-----LANCEMENT DU PROGRAMME-----\n")
    meilleur_gain = knapsack_best_gain(actions, BUDGET_MAX)
    end = time.time()

    print("Meilleur gain (en euros) :", meilleur_gain)
    print("Temps d'exécution (sec)  :", round(end - start, 6))