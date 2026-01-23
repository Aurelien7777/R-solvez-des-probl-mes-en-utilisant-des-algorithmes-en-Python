import time

def knapsack_meilleure_strategie(actions, budget_max_euros):
    """
    Version optimisée (DP 1D) qui retourne :
    - la liste des actions choisies
    - le coût total
    - le gain total

    Cette version respecte la contrainte 0/1 (une action max une fois).
    """

    # 1) Conversion du budget max en centimes pour travailler en entiers (évite les erreurs float)
    budget_max_centimes = int(round(budget_max_euros * 100))

    # 2) Mémoire principale :
    # meilleur_gain_par_budget[b] = meilleur gain possible (en centimes) pour un budget max de b centimes
    meilleur_gain_par_budget = [0] * (budget_max_centimes + 1)

    # 3) Mémoire de reconstruction :
    # Pour chaque action, on garde une ligne de "choix" :
    # choix_action[index_action][budget] = 1 si on a pris cette action pour améliorer ce budget
    choix_action = []
    index_action = 0
    while index_action < len(actions):
        choix_action.append(bytearray(budget_max_centimes + 1))
        index_action += 1

    # 4) Traitement action par action
    index_action = 0
    while index_action < len(actions):
        action = actions[index_action]

        # Conversion du coût et du gain en centimes
        cout_action_centimes = int(round(action.cost * 100))
        gain_action_centimes = int(round(action.gain * 100))

        # Si l'action est trop chère ou inutile, on l'ignore
        if cout_action_centimes <= 0 or gain_action_centimes <= 0:
            index_action += 1
            continue

        if cout_action_centimes > budget_max_centimes:
            index_action += 1
            continue

        # Parcours du budget du plus grand vers le plus petit (IMPORTANT pour 0/1)
        budget_en_cours = budget_max_centimes
        while budget_en_cours >= cout_action_centimes:

            # Gain actuel (sans prendre l'action)
            gain_sans_action = meilleur_gain_par_budget[budget_en_cours]

            # Gain si on prend l'action
            budget_restant = budget_en_cours - cout_action_centimes
            gain_avec_action = gain_action_centimes + meilleur_gain_par_budget[budget_restant]

            # Si prendre l'action améliore le résultat, on met à jour
            if gain_avec_action > gain_sans_action:
                meilleur_gain_par_budget[budget_en_cours] = gain_avec_action
                choix_action[index_action][budget_en_cours] = 1

            budget_en_cours -= 1

        index_action += 1

    # 5) Reconstruction de la liste des actions choisies
    actions_selectionnees = []
    budget_en_cours = budget_max_centimes

    index_action = len(actions) - 1
    while index_action >= 0:

        # Si on a choisi cette action pour ce budget, on la prend
        if choix_action[index_action][budget_en_cours] == 1:
            action = actions[index_action]
            actions_selectionnees.append(action)

            # On retire le coût de l'action du budget pour continuer la reconstruction
            budget_en_cours -= int(round(action.cost * 100))

        index_action -= 1

    # La reconstruction récupère la liste à l'envers
    actions_selectionnees.reverse()

    # 6) Calcul coût total et gain total en euros
    cout_total = 0.0
    gain_total = 0.0

    for action in actions_selectionnees:
        cout_total += action.cost
        gain_total += action.gain

    return actions_selectionnees, cout_total, gain_total
