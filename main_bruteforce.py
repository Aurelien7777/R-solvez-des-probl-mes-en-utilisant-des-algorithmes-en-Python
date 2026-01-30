from data_transformers.transform import Transformer
from algorithms.bruteforce import brute_force_best

CSV_PATH = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\CODE\liste_actions.csv"
BUDGET_MAX = 500

def main():
    transformer = Transformer()
    lecteur = transformer.action_loader(CSV_PATH)
    actions = transformer.transform_data(lecteur)

    best_combo, best_cost, best_gain = brute_force_best(actions, BUDGET_MAX)

    print("Coût total :", round(best_cost, 2), "€")
    print("Gain total :", round(best_gain, 2), "€")
    print("Actions sélectionnées :", best_combo)

if __name__ == "__main__":
    main()
