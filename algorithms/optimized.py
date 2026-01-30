def knapsack_meilleure_strategie(actions, budget_max_euros):
    """
    OBJECTIF
    --------
    Trouver la meilleure combinaison d'actions qui maximise le gain total,
    sans dépasser un budget maximum (500€), et en respectant ces règles :

    - On ne peut acheter chaque action qu'une seule fois (problème du sac à dos 0/1)
    - On ne peut pas acheter une fraction d'action
    - On ne peut pas dépasser le budget

    ENTRÉES
    -------
    actions : liste d'objets Action
        Chaque Action contient au minimum :
        - action.cost : coût en euros (float)
        - action.gain : gain en euros (float)
        - action.name : nom (str) (utile pour afficher)

    budget_max_euros : float ou int
        Exemple : 500

    SORTIES
    -------
    actions_selectionnees : list[Action]
        La liste des actions retenues (la meilleure combinaison)
    cout_total : float
        La somme des coûts des actions sélectionnées (en euros)
    gain_total : float
        La somme des gains des actions sélectionnées (en euros)

    PRINCIPE
    --------
    On utilise la programmation dynamique (Dynamic Programming, DP).

    Idée simple :
    - On imagine que chaque budget possible (0€ à 500€) est une "case".
    - Pour chaque case budget, on stocke le meilleur gain possible.
    - Ensuite, on reconstruit quelles actions ont permis ce meilleur gain.
    """

    # ============================================================
    # 1) CONVERSION DU BUDGET EN CENTIMES (POUR ÉVITER LES FLOATS)
    # ============================================================
    # Exemple : 500€ -> 50000 centimes
    # Pourquoi ?
    # - Les floats peuvent créer des erreurs d'arrondi (ex : 0.1 + 0.2 != 0.3)
    # - En centimes, on travaille en entiers => comparaisons fiables
    budget_max_centimes = int(round(budget_max_euros * 100))

    # ============================================================
    # 2) MÉMOIRE PRINCIPALE : MEILLEUR GAIN POSSIBLE POUR CHAQUE BUDGET
    # ============================================================
    # meilleur_gain_par_budget[b] = meilleur gain possible (en centimes)
    # avec un budget maximum de b centimes.
    #
    # Exemple :
    # meilleur_gain_par_budget[50000] contient le gain max possible avec 500€
    #
    # On initialise à 0 car au départ, sans action, gain = 0.
    meilleur_gain_par_budget = [0] * (budget_max_centimes + 1)

    # ============================================================
    # 3) MÉMOIRE DE "DÉCISION" POUR RECONSTRUIRE LES ACTIONS CHOISIES
    # ============================================================
    # On veut pouvoir répondre à la question :
    # "OK, j'ai le gain max, mais quelles actions EXACTES ont été choisies ?"
    #
    # Pour ça, on mémorise les choix sous forme binaire (0 ou 1).
    #
    # choix_action[i][b] == 1 signifie :
    # "Pour l'action i, au budget b, on a pris cette action car ça améliorait le gain."
    #
    # On construit donc une "grille" :
    # - lignes = actions
    # - colonnes = budgets (0 à budget_max)
    #
    # bytearray :
    # - très compact en mémoire
    # - stocke des valeurs 0/1 (en réalité 0..255 mais ici on n'utilise que 0/1)
    choix_action = []

    index_action = 0
    while index_action < len(actions):
        # Une ligne par action, contenant un 0/1 pour chaque budget possible
        choix_action.append(bytearray(budget_max_centimes + 1))
        index_action += 1

    # ============================================================
    # 4) PROGRAMMATION DYNAMIQUE : TRAITEMENT ACTION PAR ACTION
    # ============================================================
    # On traite les actions une par une.
    # À chaque action, on met à jour meilleur_gain_par_budget.
    #
    # Point clé :
    # On parcourt le budget EN DESCENDANT (du plus grand au plus petit),
    # sinon on pourrait prendre plusieurs fois la même action.
    #
    # (C'est ce qui garantit la contrainte 0/1)
    index_action = 0
    while index_action < len(actions):
        action = actions[index_action]

        # Conversion du coût et du gain de l'action en centimes
        cout_action_centimes = int(round(action.cost * 100))
        gain_action_centimes = int(round(action.gain * 100))

        # --------------------------------------------
        # Filtrage des actions inutiles / invalides
        # --------------------------------------------
        # Si coût <= 0 ou gain <= 0 : ça n'a pas de sens ou ça ne rapporte rien
        if cout_action_centimes <= 0 or gain_action_centimes <= 0:
            index_action += 1
            continue

        # Si l'action coûte plus que le budget max, elle ne peut jamais être choisie
        if cout_action_centimes > budget_max_centimes:
            index_action += 1
            continue

        # --------------------------------------------
        # Parcours du budget en descendant (0/1 knapsack)
        # --------------------------------------------
        budget_en_cours = budget_max_centimes

        while budget_en_cours >= cout_action_centimes:
            # Option 1 : ne PAS prendre l'action
            gain_sans_action = meilleur_gain_par_budget[budget_en_cours]

            # Option 2 : prendre l'action
            # Si on prend l'action, il reste :
            budget_restant = budget_en_cours - cout_action_centimes

            # Gain total si on prend l'action =
            # gain de l'action + meilleur gain possible avec le budget restant
            gain_avec_action = gain_action_centimes + meilleur_gain_par_budget[budget_restant]

            # --------------------------------------------
            # On garde la meilleure option
            # --------------------------------------------
            if gain_avec_action > gain_sans_action:
                # On améliore le meilleur gain connu pour ce budget
                meilleur_gain_par_budget[budget_en_cours] = gain_avec_action

                # On mémorise que pour ce budget, cette action a été prise
                choix_action[index_action][budget_en_cours] = 1

            # On continue en diminuant le budget
            budget_en_cours -= 1

        index_action += 1

    # ============================================================
    # 5) RECONSTRUCTION : RETROUVER LA LISTE D'ACTIONS CHOISIES
    # ============================================================
    # À ce stade, on connaît le gain max.
    # Maintenant, on veut retrouver quelles actions ont mené à ce résultat.
    #
    # On part du budget max et on remonte action par action.
    actions_selectionnees = []
    budget_en_cours = budget_max_centimes

    # On repart de la dernière action vers la première
    index_action = len(actions) - 1
    while index_action >= 0:
        # Si pour ce budget, cette action a été marquée comme "prise"
        if choix_action[index_action][budget_en_cours] == 1:
            action = actions[index_action]
            actions_selectionnees.append(action)

            # On retire son coût du budget pour revenir au budget précédent
            budget_en_cours -= int(round(action.cost * 100))

        index_action -= 1

    # La reconstruction s'est faite à l'envers, donc on remet dans l'ordre
    actions_selectionnees.reverse()

    # ============================================================
    # 6) CALCUL DU COÛT TOTAL ET GAIN TOTAL EN EUROS
    # ============================================================
    cout_total = 0.0
    gain_total = 0.0

    for action in actions_selectionnees:
        cout_total += action.cost
        gain_total += action.gain

    return actions_selectionnees, cout_total, gain_total
