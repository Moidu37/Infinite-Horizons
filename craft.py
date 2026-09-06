import pygame
import os
import json
import personnage

FICHIER_CRAFT = "./data/crafts.json"

def charger_craft():
    """Charge les crafts depuis le fichier JSON."""
    if not os.path.exists(FICHIER_CRAFT):
        return {}

    with open(FICHIER_CRAFT, "r", encoding="utf-8") as f:
        return json.load(f)


def dessiner_craft():
    pass


def ouvrir_craft():
    dictionnaire_crafts = charger_craft()
    reponse = input("Que voulez vous crafter (r = réacteur, ré = réservoir, n =nez)? ")
    
    if reponse == "r":
        print(f"Vous avez choisi de crafter un réacteur. Niveau : {personnage.level}")
        if "reacteurs" in dictionnaire_crafts:
            reacteur = dictionnaire_crafts["reacteurs"][0]  # Premier réacteur de la liste
            if personnage.level < reacteur["niveau_requis"]:
                print("Vous n'avez pas le niveau requis pour crafter cet objet.")
            else:
                print(f"Succès ! Craft disponible : {reacteur['nom']}")
        else:
            print("Aucun réacteur trouvé.")
            
    elif reponse == "ré":
        print(f"Vous avez choisi de crafter un réservoir. Niveau : {personnage.level}")
        if "reservoirs" in dictionnaire_crafts:
            reservoir = dictionnaire_crafts["reservoirs"][0]
            if personnage.level < reservoir["niveau_requis"]:
                print("Vous n'avez pas le niveau requis pour crafter cet objet.")
            else:
                print(f"Succès ! Craft disponible : {reservoir['nom']}")
        else:
            print("Aucun réservoir trouvé.")
                
    elif reponse == "n":
        print(f"Vous avez choisi de crafter un nez. Niveau : {personnage.level}")
        if "nez" in dictionnaire_crafts:
            nez = dictionnaire_crafts["nez"][0]
            if personnage.level < nez["niveau_requis"]:
                print("Vous n'avez pas le niveau requis pour crafter cet objet.")
            else:
                print(f"Succès ! Craft disponible : {nez['nom']}")
        else:
            print("Aucun nez trouvé.")