import time

def knapsack_best_gain(actions, budget_max_eur):
    """
    Calcule le gain maximal possible avec la méthode KNAPSACK sans dépasser le budget maximum
    """
    meilleur_gain = [0] * (budget_max_eur + 1) 

    # On traite chaque action une par une 
    for action in actions:
        print(f"----- TRAITEMENT DE L'ACTION {action.name} -----")
        
        # Conversion du coût de l'action en centimes 
        # Exemple : 34€ = 3400 centimes
        cout_action = int(action.cost)
        print(f"----- COÛT DE L'ACTION : {cout_action} -----")
        
        # Calcul du gain de l'action en centimes 
        # gain = coût * taux
        # Exemple : 34€ * 0.27 = 9.18€ -> 918 centimes
        gain_action = action.gain
        print(f"----- GAIN DE L'ACTION : {gain_action} -----\n")
        
        # Si une action coûte plus que le budget, elle est inutile ici 
        if cout_action > budget_max_eur:
            continue
        
        for budget in range(budget_max_eur, cout_action - 1, -1): 
            
            print(f"Le budget actuel est : {budget}")
            
            # Gain sans prendre l'action 
            gain_sans_action = meilleur_gain[budget] 
            print(f"GAIN SANS ACTION : {gain_sans_action}")
            
            # Gain si on prend l'action
            budget_restant = budget - cout_action
            print(f"-----BUDGET RESTANT : {budget_restant}-----")
            
            gain_avec_action = gain_action + meilleur_gain[budget_restant]
            print(f"GAIN AVEC ACTION : {gain_avec_action}\n")
            
            # On garde le meilleur des deux
            if gain_avec_action > gain_sans_action:
                meilleur_gain[budget] = gain_avec_action

    #print(f"AFFICHAGE DE LA LISTE : {meilleur_gain}")
    print()
    # Résultat final 
    # Le meilleur gain possible pour le budget max est dans meilleur_gain[budget_max_cents]
    meilleur_gain = meilleur_gain[BUDGET_MAX]

    return meilleur_gain


# -------------------------
# LANCEMENT DU PROGRAMME
# -------------------------
if __name__ == "__main__":
    from transformers.transform import Transformer

    CSV_PATH = "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"
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
