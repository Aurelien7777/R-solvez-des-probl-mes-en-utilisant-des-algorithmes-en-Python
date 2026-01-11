from transformers.transform import Transformer
from transformers.transform import Action
from itertools import combinations

"""Chemin du fichier contenant les datas"""
CSV_PATH = "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"
BUDGET_MAX = 500

transformer = Transformer()
lecteur = transformer.action_loader(CSV_PATH)
actions = transformer.transform_data(lecteur)

def brute_force_best(actions, budget):
    """Cette fonction permet de sélectionner la combinaison
    permettant de réaliser un maximum de gain avec un investissement limité
    """
    
    best_combo = []
    best_gain = 0.0
    best_cost = 0.0

    number_total_actions = len(actions)

    # Boucle sur le nombre d'action(20) contenu dans la liste "actions"
    # "size_combination" = taille de la combinaison (Détermine si "ACTION" va être testé avec 1, 2, 3 etc éléments)
    for size_combination in range(1, number_total_actions + 1): #Nous allons boucler "number_total_actions" + 1 SOIT 20 fois
        
        # Dans la boucle ci-dessous, la liste "actions" est l'itérable, c'est à dire, l'objet contenant les éléments à combiner
        # "size_combination" = taille de la combinaison (Détermine si "ACTION" va être testé avec 1, 2, 3 etc éléments)
        # "combo" contient une combinaison d'action de taille "size_combination" (Exemple : action-1, action-2, action-4)
        # Pour chaque action provenant de "actions", tu vas tester des combinaisons d'actions de taille "size_combinations" 
        # En fonction de la taille de la combinaison "size_combination", il va y avoir plus ou moins d'actions dans "combo"
        # Comment les actions sont ajoutées dans "combo"? "combo" vient puiser les actions dans la liste "actions" placée en paramètre de "combinations"
        
        for combo in combinations(actions, size_combination): 
            # "combo"est un tuple contenant les actions présentes dans une combinaison
            # Par exemple "action-1" est testé avec toutes les tailles de combinaisons possible allant de 1 à 20, si les conditions sont réunies (BUDGET_MAX)
            
            # coût = la somme des prix de chaque action présent dans la combinaison
            cost = sum(action.cost for action in combo) 
            # "combo"est un tuple contenant les actions présentes dans une combinaison
            # Création d'une une expression génératrice nommée "cost", dans laquelle pour chaque action présente dans combo, on récupère son coût (On additionne les coûts)
            # La valeur action.cost est récupérée à partir de "combo" qui représente une combinaison testée
            
            # Si le côut de la combinaison est inférieur ou égal à 500€ soit le BUDGET_MAX
            if cost <= budget:
                
                # Gain est égal à la somme des gains que génère chaque action
                gain = sum(action.gain for action in combo)  
                # Création d'une compréhension de liste nommée "gain", dans laquelle pour chaque action présente dans "combo", on récupère son gain générable
                # La valeur action.rate est récupérée à partir de "combo" qui représente une combinaison testée
                
                # Si le gain est supérieur au meilleur gain enregistré
                if gain > best_gain:
                    best_gain = gain
                    best_cost = cost
                    best_combo = combo
    return best_combo, best_cost, best_gain

best_invest = brute_force_best(actions, BUDGET_MAX)
print(type(best_invest))

for invest in best_invest:
    print("DEBUG",invest)