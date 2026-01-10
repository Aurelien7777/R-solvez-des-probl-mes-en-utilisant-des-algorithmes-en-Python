from transformers.transform import Transformer
from transformers.transform import Action
from itertools import combinations

"""Chemin du fichier contenant les datas"""
CSV_PATH = "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"
BUDGET_MAX = 500

transformer = Transformer()
lecteur = transformer.action_loader(CSV_PATH)
actions = transformer.transform_data(lecteur)
print()
print("TEST")
print(actions[0])
print(type(actions[0]))
print(dir(actions[0]))
print()
print("Le prx de l'action numéro 1 est : ",actions[0].cost)
print("Le prx de l'action numéro 2 est : ",actions[1].cost)

def brute_force_best(actions, budget):
    best_combo = []
    best_gain = 0.0
    best_cost = 0.0

    number_total_actions = len(actions)

    #Boucle sur le nombre d'actions contenu dans la liste "actions"
    for size_combination in range(1, number_total_actions + 1): 
        for combo in combinations(actions, size_combination):
            
            #coût = la somme des prix de chaque action présent dans la combinaison
            cost = sum(action.cost for action in combo) 
            
            #Si le côut de la combinaison est inférieur ou égal à 500€
            if cost <= budget:
                
                #Gain est égal à la somme des gains que génère chaque action
                gain = sum(action.rate for action in combo)  
                
                #Si le gain est supérieur au meilleur gain enregistré
                if gain > best_gain:
                    # Le meilleur gain devient celui de la combinaison enregistrée
                    best_gain = gain
                    best_cost = cost
                    best_combo = combo
    return best_combo #, best_cost, best_gain


print()
best_invest = brute_force_best(actions, BUDGET_MAX)
print("Le meilleur investissement est :", best_invest)
print()
print(type(best_invest))


"""
i = 0
for invest in best_invest:
    print(f"Investissement {i} : {invest}")
    print()"""