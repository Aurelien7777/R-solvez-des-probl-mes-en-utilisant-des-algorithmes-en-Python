import time

# Chargement des outils de transformation des données
from data_transformers.transform import Transformer

# Algorithme optimisé (sac à dos / knapsack)
from algorithms.optimized_dataset import knapsack_meilleure_strategie



# ===============================
# PARAMÈTRES GÉNÉRAUX
# ===============================

BUDGET_MAX = 500  # Budget maximal autorisé (en euros)

DATASET1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset1_Python+P7.csv"
DATASET2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset2_Python+P7.csv"

DECISION1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\solution1_Python+P7.txt"
DECISION2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\solution2_Python+P7.txt"

# 👉 Choix du dataset et de la décision à tester
DATASET_SELECTIONNE = DATASET2
DECISION_SELECTIONNE = DECISION1


# ===============================
# 1️⃣ CHARGEMENT DES DONNÉES
# ===============================

# Création de l'objet Transformer
transformer = Transformer()

# Chargement brut du CSV
lignes = transformer.action_loader_dataset(DATASET_SELECTIONNE)

# Transformation :
# - suppression des données invalides
# - calcul des gains
# - création des objets Action
actions = transformer.transform_data_dataset(lignes)


# ===============================
# 2️⃣ EXÉCUTION DE L’ALGORITHME OPTIMISÉ
# ===============================

start = time.time()

# L’algorithme choisit les meilleures actions possibles
actions_algo, cout_algo, gain_algo = knapsack_meilleure_strategie(actions, BUDGET_MAX)

end = time.time()



# ===============================
# 5️⃣ AFFICHAGE DU RAPPORT (BACKTEST)
# ===============================

print("\n===== EXPLORATION DES DONNÉES =====")
print("Nombre total de lignes CSV :", len(lignes))
print("Actions valides :", len(actions))
print("Actions rejetées :", len(transformer.rejected_action))

# Comptage des raisons de rejet (données manquantes / incorrectes)
reasons = {}
for rejet in transformer.rejected_action:
    reason = rejet["reason"]
    reasons[reason] = reasons.get(reason, 0) + 1

print("Détails des rejets :", reasons)


print("\n===== RÉSULTATS DE L’ALGORITHME =====")
print("Nombre d’actions choisies :", len(actions_algo))
print("Coût total :", round(cout_algo, 2), "€")
print("Gain total :", round(gain_algo, 2), "€")
print("Temps d’exécution :", round(end - start, 4), "sec")


