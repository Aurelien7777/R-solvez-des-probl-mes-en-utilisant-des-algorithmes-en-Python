def compare_selections(all_actions, algo_actions_selectionnees, sienna_action_names):
    """
    Compare les choix de l'algorithme avec ceux de Sienna.

    all_actions :
        Liste complète des actions valides du dataset.

    algo_actions_selectionnees :
        Liste des objets Action choisis par l'algorithme.

    sienna_action_names :
        Ensemble (set) des noms d'actions achetées par Sienna.

    Retourne un dictionnaire contenant :
    - coûts et gains comparés
    - actions communes
    - actions uniquement choisies par l'algorithme
    - actions uniquement choisies par Sienna
    - actions de Sienna inconnues du dataset
    """

    # -------------------------------
    # Création d'un dictionnaire :
    # nom_action -> objet Action
    # Utile pour retrouver rapidement une action à partir de son nom
    # -------------------------------
    action_map = {}
    for action in all_actions:
        action_map[action.name] = action

    # -------------------------------
    # Noms des actions choisies par l'algorithme
    # -------------------------------
    algo_names = set()
    for action in algo_actions_selectionnees:
        algo_names.add(action.name)

    # -------------------------------
    # Calcul du coût et du gain de l'algorithme
    # -------------------------------
    algo_cost = 0.0
    algo_gain = 0.0

    for action in algo_actions_selectionnees:
        algo_cost += action.cost
        algo_gain += action.gain

    # -------------------------------
    # Calcul du coût et du gain de Sienna
    # (uniquement pour les actions présentes dans le dataset)
    # -------------------------------
    sienna_cost = 0.0
    sienna_gain = 0.0

    for name in sienna_action_names:
        action = action_map.get(name)

        # Si l'action n'existe pas dans le dataset, on l'ignore ici
        if action is None:
            continue

        sienna_cost += action.cost
        sienna_gain += action.gain

    # -------------------------------
    # Comparaison des ensembles d'actions
    # -------------------------------
    commun = algo_names.intersection(sienna_action_names)
    seulement_algo = algo_names.difference(sienna_action_names)
    seulement_sienna = sienna_action_names.difference(algo_names)

    # -------------------------------
    # Actions citées par Sienna mais absentes du dataset
    # -------------------------------
    sienna_inconnues = set()
    for name in sienna_action_names:
        if name not in action_map:
            sienna_inconnues.add(name)

    # -------------------------------
    # Résultat final
    # -------------------------------
    return {
        "algo_cost": algo_cost,
        "algo_gain": algo_gain,
        "sienna_cost": sienna_cost,
        "sienna_gain": sienna_gain,
        "commun": sorted(list(commun)),
        "seulement_algo": sorted(list(seulement_algo)),
        "seulement_sienna": sorted(list(seulement_sienna)),
        "sienna_inconnues": sorted(list(sienna_inconnues)),
    }
