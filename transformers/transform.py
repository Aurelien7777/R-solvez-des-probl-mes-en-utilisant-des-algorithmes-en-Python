import csv

"""Chemin du fichier contenant les datas"""
CSV_PATH = "C:/OPENCLASSROOMS/PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python/CODE/liste_actions.csv"

class Action:
    def __init__(self, name, cost, rate, gain):
        self.name = name
        self.cost = cost 
        self.rate = rate
        self.gain = gain
        
    def calculate_gain(self):
        """Fonction permettant de calculer le gain généré par une action"""
        
        return self.cost * self.rate
        
    def __repr__(self):
        """Représentation textuelle de l'objet Action pour le débogage."""
        
        return (
            f"Action : \n"
            f"Nom = {self.name}\n" 
            f"Coût = {self.cost}\n" 
            f"Bénéfice = {self.rate}\n"
            f"Gain = {self.gain}")


class Transformer:
    def __init__(self):
        self.rejected_action = []

    def action_loader(self, csv_file):
        """Cette fonction charge le contenu du fichier à exploiter
            et retourne une liste de dictionnaire
        """
        
        # On ouvre le fichier CSV en lecture ("r")
        # encoding="cp1252" : utile car le fichier contient des caractères comme "Coût" et "Bénéfice"
        # newline="" : recommandé avec csv pour éviter des lignes vides sur certains systèmes
        actions_brut = []
        with open(csv_file, "r", encoding="cp1252", newline="") as fichier:
        # DictReader lit chaque ligne du CSV et la transforme en dictionnaire
        # delimiter=";" : car ton CSV est séparé par des points-virgules
            lecteur = csv.DictReader(fichier, delimiter=";")
            for ligne in lecteur:
                actions_brut.append(ligne)

        return actions_brut

    def transform_data(self, lecteur):
        """
        Cette fonction s'occupe de la transformation des données du CSV 
        pour exploitation dans le programme
        """
        
        #Initialisation de la liste qui va stocker les actions objets
        actions = []
            
        # On parcourt chaque ligne du fichier (chaque ligne = un dictionnaire)
        for ligne in lecteur:
        
            # On récupère le nom de l'action (ex: "Action-1")
            name = ligne["Actions #"].strip()  # strip() enlève les espaces inutiles
            
            # On récupère le coût et on le transforme en nombre (float)
            cout_texte = ligne["Coût par action (en euros)"].strip()
            cost = float(cout_texte)
            
            # On récupère le bénéfice (ex: "0,25") et on remplace la virgule par un point
            benefice_texte = ligne["Bénéfice (après 2 ans)"].strip()
            benefice_texte = benefice_texte.replace(",", ".")
            rate = float(benefice_texte)  # ex: 0.25
            
            #Création de l'instance action
            action = Action(name, cost, rate, gain=0)
            # On calcule le profit en euros pour UNE action
            gain = action.calculate_gain()
            action.gain = gain
            
            # On ajoute cette action dans la liste actions
            actions.append(action)
            
        #Vérification simple : on affiche combien d’actions on a chargées
        #print("Nombre d'actions chargées :", len(actions))
        
        return actions
    
    def action_loader_dataset(self, csv_file):
        """Charge dataset1_Python+P7 et dataset2_Python+P7
        et retourne une liste de dictionnaires
        """
        actions_brut = []
        with open(csv_file, "r", encoding="utf-8", newline="") as fichier:
            lecteur = csv.DictReader(fichier, delimiter=",")
            for ligne in lecteur:
                actions_brut.append(ligne)

        return actions_brut


    def transform_data_dataset(self, lecteur):
        actions = []
        self.rejected_action = []

        for ligne in lecteur:
            # 1) name
            #Récupère la partie "name" de la ligne
            name = (ligne.get("name") or "").strip()
            if not name:
                self.rejected_action.append({"name": None, "reason": "missing_name"})
                continue

            # 2) price
            #Récupère la partie "price" de la ligne
            price_str = (ligne.get("price") or "").strip()
            try:
                cost = float(price_str)
            except ValueError:
                self.rejected_action.append({"name": name, "reason": "invalid_price_format"})
                continue

            if cost <= 0:
                self.rejected_action.append({"name": name, "reason": "price_leq_0"})
                continue

            # 3) profit (en %)
            #Récupère la partie "profit" de la ligne
            profit_str = (ligne.get("profit") or "").strip()
            try:
                profit_percent = float(profit_str)
            except ValueError:
                self.rejected_action.append({"name": name, "reason": "invalid_profit_format"})
                continue

            if profit_percent <= 0:
                self.rejected_action.append({"name": name, "reason": "profit_leq_0"})
                continue

            # conversion % -> taux
            rate = profit_percent / 100

            # gain en euros
            gain = cost * rate

            actions.append(Action(name, cost, rate, gain))

        return actions



