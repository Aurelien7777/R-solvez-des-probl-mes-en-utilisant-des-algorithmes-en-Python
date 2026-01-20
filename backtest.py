import time
from transformers.transform import Transformer
from algorithms.knapsack import knapsack_meilleure_strategie_dataset

BUDGET_MAX = 500

DATASET1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset1_Python+P7.csv"
DATASET2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset2_Python+P7.csv"

def compter_raisons_rejets(rejected_action):
    compteur = {}
    for rejet in rejected_action:
        raison = rejet["reason"]
        compteur[raison] = compteur.get(raison, 0) + 1
    return compteur

def run_dataset(chemin_csv, nom_affichage):
    transformer = Transformer()
    lignes = transformer.action_loader_dataset(chemin_csv)
    actions_valides = transformer.transform_data_dataset(lignes)

    print(f"\n=== {nom_affichage} ===")
    print("Actions valides :", len(actions_valides))
    print("Actions rejetées :", len(transformer.rejected_action))
    print("Détail rejets :", compter_raisons_rejets(transformer.rejected_action))

    start = time.time()
    actions_choisies, cout_total, gain_total = knapsack_meilleure_strategie_dataset(actions_valides, BUDGET_MAX)
    end = time.time()

    print("Coût total :", round(cout_total, 2), "€")
    print("Gain total :", round(gain_total, 2), "€")
    print("Nombre d'actions choisies :", len(actions_choisies))
    print("Temps d'exécution (sec) :", round(end - start, 6))

if __name__ == "__main__":
    run_dataset(DATASET1, "DATASET 1")
    run_dataset(DATASET2, "DATASET 2")
