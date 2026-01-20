import time

def knapsack_meilleure_strategie_2d(actions, budget_max_euros):
    budget_max_centimes = int(round(budget_max_euros * 100))
    nombre_actions = len(actions)

    # Préparer les coûts/gains en centimes (plus simple et plus rapide)
    couts_centimes = [int(round(a.cost * 100)) for a in actions]
    gains_centimes = [int(round(a.gain * 100)) for a in actions]

    # gain_max[i][b] : meilleur gain possible avec les i premières actions et budget b
    gain_max = [[0] * (budget_max_centimes + 1) for _ in range(nombre_actions + 1)]

    # Remplissage DP
    for i in range(1, nombre_actions + 1):
        cout_action = couts_centimes[i - 1]
        gain_action = gains_centimes[i - 1]

        for budget_en_cours in range(0, budget_max_centimes + 1):
            # Option 1 : ne pas prendre l'action
            gain_sans_action = gain_max[i - 1][budget_en_cours]

            # Option 2 : prendre l'action (si possible)
            if cout_action <= budget_en_cours:
                gain_avec_action = gain_action + gain_max[i - 1][budget_en_cours - cout_action]
                gain_max[i][budget_en_cours] = max(gain_sans_action, gain_avec_action)
            else:
                gain_max[i][budget_en_cours] = gain_sans_action

    # Reconstruction des actions choisies
    actions_selectionnees = []
    budget_en_cours = budget_max_centimes

    for i in range(nombre_actions, 0, -1):
        # Si la valeur a changé par rapport à la ligne précédente, l'action i-1 a été prise
        if gain_max[i][budget_en_cours] != gain_max[i - 1][budget_en_cours]:
            action = actions[i - 1]
            actions_selectionnees.append(action)
            budget_en_cours -= couts_centimes[i - 1]

    actions_selectionnees.reverse()

    cout_total = sum(a.cost for a in actions_selectionnees)
    gain_total = sum(a.gain for a in actions_selectionnees)

    return actions_selectionnees, cout_total, gain_total


def knapsack_meilleure_strategie_dataset(actions, budget_max_euros):
    budget_max_centimes = int(round(budget_max_euros * 100))
    nombre_actions = len(actions)

    couts_centimes = [int(round(a.cost * 100)) for a in actions]
    gains_centimes = [int(round(a.gain * 100)) for a in actions]

    meilleur_gain_par_budget = [0] * (budget_max_centimes + 1)

    # Mémoire compacte : 1 byte par budget et par action
    choix_action = [bytearray(budget_max_centimes + 1) for _ in range(nombre_actions)]

    for index_action in range(nombre_actions):
        cout_action = couts_centimes[index_action]
        gain_action = gains_centimes[index_action]

        if cout_action <= 0 or gain_action <= 0:
            continue
        if cout_action > budget_max_centimes:
            continue

        for budget_en_cours in range(budget_max_centimes, cout_action - 1, -1):
            gain_sans_action = meilleur_gain_par_budget[budget_en_cours]
            gain_avec_action = gain_action + meilleur_gain_par_budget[budget_en_cours - cout_action]

            if gain_avec_action > gain_sans_action:
                meilleur_gain_par_budget[budget_en_cours] = gain_avec_action
                choix_action[index_action][budget_en_cours] = 1

    # Reconstruction
    actions_selectionnees = []
    budget_en_cours = budget_max_centimes

    for index_action in range(nombre_actions - 1, -1, -1):
        if choix_action[index_action][budget_en_cours] == 1:
            actions_selectionnees.append(actions[index_action])
            budget_en_cours -= couts_centimes[index_action]

    actions_selectionnees.reverse()

    cout_total = sum(a.cost for a in actions_selectionnees)
    gain_total = sum(a.gain for a in actions_selectionnees)

    return actions_selectionnees, cout_total, gain_total


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
    actions_choisies, cout_total, gain_total = knapsack_meilleure_strategie_2d(actions, BUDGET_MAX)

    print("Coût total :", round(cout_total, 2), "€")
    print("Gain total :", round(gain_total, 2), "€")
    print("Actions choisies :", [a.name for a in actions_choisies])
    print("Doublons ?", len(set(a.name for a in actions_choisies)) != len(actions_choisies))

    end = time.time()

    #print("Meilleur gain (en euros) :", meilleur_gain)
    print("Temps d'exécution (sec)  :", round(end - start, 6))
