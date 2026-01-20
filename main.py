import time
from transformers.transform import Transformer
from algorithms.knapsack import (
    knapsack_meilleure_strategie,
    knapsack_meilleure_strategie_dataset
)

BUDGET_MAX = 500

def run_csv_initial():
    print("\n=== CSV INITIAL (20 actions) ===")
    transformer = Transformer()
    raw_actions = transformer.action_loader("data/liste_actions.csv")
    actions = transformer.transform_data(raw_actions)

    start = time.time()
    actions_choisies, cout, gain = knapsack_meilleure_strategie(actions, BUDGET_MAX)
    end = time.time()

    print("Coût total :", round(cout, 2), "€")
    print("Gain total :", round(gain, 2), "€")
    print("Actions :", [a.name for a in actions_choisies])
    print("Temps :", round(end - start, 4), "s")


def run_dataset(path, label):
    print(f"\n=== {label} ===")
    transformer = Transformer()
    raw = transformer.action_loader_dataset(path)
    actions = transformer.transform_data_dataset(raw)

    start = time.time()
    actions_choisies, cout, gain = knapsack_meilleure_strategie_dataset(actions, BUDGET_MAX)
    end = time.time()

    print("Coût total :", round(cout, 2), "€")
    print("Gain total :", round(gain, 2), "€")
    print("Nombre d'actions :", len(actions_choisies))
    print("Temps :", round(end - start, 4), "s")


if __name__ == "__main__":
    run_csv_initial()
    run_dataset("data/dataset1_Python+P7.csv", "DATASET 1")
    run_dataset("data/dataset2_Python+P7.csv", "DATASET 2")
