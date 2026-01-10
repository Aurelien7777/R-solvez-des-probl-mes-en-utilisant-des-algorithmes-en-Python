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
    # On ouvre le fichier CSV en lecture ("r")
    # encoding="cp1252" : utile car le fichier contient des caractères comme "Coût" et "Bénéfice"
    # newline="" : recommandé avec csv pour éviter des lignes vides sur certains systèmes
    def action_loader(self, csv_file):
        """Cette fonction charge le contenu du fichier à exploiter
            et retourne une liste de dictionnaire
        """
        
        actions_brut = []
        with open(csv_file, "r", encoding="cp1252", newline="") as fichier:
        # DictReader lit chaque ligne du CSV et la transforme en dictionnaire
        # delimiter=";" : car ton CSV est séparé par des points-virgules
            lecteur = csv.DictReader(fichier, delimiter=";")
            for ligne in lecteur:
                #print(ligne)
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
            
        # Vérification simple : on affiche combien d’actions on a chargées
        #print("Nombre d'actions chargées :", len(actions))
        
        return actions



