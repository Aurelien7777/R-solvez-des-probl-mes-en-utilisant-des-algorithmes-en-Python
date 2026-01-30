import time
from data_transformers.transform import Transformer
from algorithms.optimized_dataset import knapsack_meilleure_strategie

# ===============================
# CONFIGURATION
# ===============================
BUDGET_MAX = 500

CSV_INITIAL= "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"
DATASET1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset1_Python+P7.csv"
DATASET2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset2_Python+P7.csv"

# Choix du fichier à utiliser
FICHIER_SELECTIONNE = CSV_INITIAL   # change ici si besoin

# ===============================
# CHARGEMENT DES DONNÉES
# ===============================
transformer = Transformer()

if FICHIER_SELECTIONNE == CSV_INITIAL:
    lignes = transformer.action_loader(FICHIER_SELECTIONNE)
    actions = transformer.transform_data(lignes)
else:
    lignes = transformer.action_loader_dataset(FICHIER_SELECTIONNE)
    actions = transformer.transform_data_dataset(lignes)

# ===============================
# EXECUTION KNAPSACK
# ===============================
start = time.time()
#gain_total = knapsack_meilleure_strategie(actions, BUDGET_MAX)
actions_selectionnees, cout_total, gain_total = knapsack_meilleure_strategie(actions, BUDGET_MAX)

end = time.time()

# ===============================
# AFFICHAGE
# ===============================
print("Actions valides :", len(actions))
print("Actions rejetées :", len(transformer.rejected_action))
print("Gain total :", round(gain_total, 2), "€")
print("Temps d'exécution :", round(end - start, 4), "sec")
