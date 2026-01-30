import time

from data_transformers.transform import Transformer
from algorithms.optimized import knapsack_meilleure_strategie


# ===============================
# CONFIGURATION
# ===============================

BUDGET_MAX = 500

CSV_INITIAL = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\CODE\liste_actions.csv"
DATASET1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset1_Python+P7.csv"
DATASET2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset2_Python+P7.csv"

# Choisis le fichier à analyser ici :
FICHIER_SELECTIONNE = DATASET2  # CSV_INITIAL / DATASET1 / DATASET2


# ===============================
# CHARGEMENT + TRANSFORMATION
# ===============================

transformer = Transformer()

# On charge les lignes brutes + on transforme en objets Action
# - CSV_INITIAL : séparateur ; et champs différents
# - DATASET1/2  : séparateur , et champs name/price/profit
if FICHIER_SELECTIONNE == CSV_INITIAL:
    lignes = transformer.action_loader(FICHIER_SELECTIONNE)
    actions = transformer.transform_data(lignes)
else:
    lignes = transformer.action_loader_dataset(FICHIER_SELECTIONNE)
    actions = transformer.transform_data_dataset(lignes)


# ===============================
# RAPPORT D'EXPLORATION
# ===============================

print("\n===== EXPLORATION DES DONNÉES =====")
print("Fichier :", FICHIER_SELECTIONNE)
print("Nombre total de lignes CSV :", len(lignes))
print("Actions valides :", len(actions))

# rejected_action est surtout alimenté pour dataset1/dataset2
nb_rejets = len(getattr(transformer, "rejected_action", []))
print("Actions rejetées :", nb_rejets)

# Détail des rejets par raison (si dispo)
reasons = {}
for rejet in getattr(transformer, "rejected_action", []):
    reason = rejet.get("reason", "unknown_reason")
    reasons[reason] = reasons.get(reason, 0) + 1

if reasons:
    print("Détails des rejets :", reasons)


# ===============================
# EXECUTION KNAPSACK
# ===============================

start = time.time()
actions_selectionnees, cout_total, gain_total = knapsack_meilleure_strategie(actions, BUDGET_MAX)
end = time.time()


# ===============================
# RESULTATS
# ===============================

print("\n===== RÉSULTATS DE L’ALGORITHME =====")
print("Nombre d’actions choisies :", len(actions_selectionnees))
print("Coût total :", round(cout_total, 2), "€")
print("Gain total :", round(gain_total, 2), "€")
print("Temps d’exécution :", round(end - start, 4), "sec")
