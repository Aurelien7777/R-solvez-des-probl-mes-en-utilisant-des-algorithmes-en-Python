import re


def load_sienna_decisions_txt(txt_file_path):
    """
    Lit un fichier texte (solution1/solution2) et récupère :
    - la liste des actions que Sienna a achetées
    - le coût total indiqué dans le fichier
    - le profit/retour total indiqué dans le fichier

    Exemple de fichier :
    Sienna bought:
    Share-XXXX
    Share-YYYY
    Total cost: 489.24€
    Profit: 193.78€
    """

    # On ouvre le fichier en lecture.
    # encoding="utf-8" : format le plus courant.
    # errors="replace" : si le fichier contient des caractères bizarres, Python ne plante pas,
    # il remplace juste les caractères invalides.
    with open(txt_file_path, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()

    # Dans tes fichiers, le symbole € est mal encodé (â‚¬).
    # On le remplace pour avoir un affichage propre.
    text = text.replace("â‚¬", "€")

    # On transforme le texte en liste de lignes (une ligne = un élément)
    # strip() enlève les espaces inutiles.
    lines = [line.strip() for line in text.splitlines()]

    # actions : contiendra les noms des actions achetées (ex: "Share-GRUT")
    actions = set()

    # total_cost / total_profit : ce que le fichier annonce
    total_cost = None
    total_profit = None

    # in_list sert à savoir si on est dans la partie "Sienna bought:" (la liste des actions)
    in_list = False

    # On lit chaque ligne une par une
    for line in lines:
        # Si la ligne est vide, on passe à la suivante
        if not line:
            continue

        # Version en minuscules pour comparer plus facilement
        low = line.lower()

        # Début de la liste des achats
        if low.startswith("sienna bought"):
            in_list = True
            continue

        # Dès qu'on arrive à "Total cost:", on arrête de lire la liste d'actions
        if low.startswith("total cost:"):
            in_list = False
            total_cost = _extract_float(line)
            continue

        # Le fichier peut écrire "Total return:" ou "Profit:"
        if low.startswith("total return:") or low.startswith("profit:"):
            in_list = False
            total_profit = _extract_float(line)
            continue

        # Si on est dans la liste, chaque ligne correspond à une action achetée
        if in_list:
            actions.add(line)

    return actions, total_cost, total_profit


def _extract_float(line):
    """
    Récupère le nombre dans une ligne comme :
    "Total cost: 498.76€"  -> 498.76

    On utilise une expression régulière (regex) pour trouver un nombre.
    """
    match = re.search(r"(\d+(?:\.\d+)?)", line)

    # Si aucun nombre trouvé, on retourne None (vide)
    if not match:
        return None

    # On convertit le texte trouvé en float
    return float(match.group(1))
