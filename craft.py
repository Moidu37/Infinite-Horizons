import pygame
import os
import json

FICHIER_CRAFT = "./data/crafts.json"

"""Fonction pour charger les crafts depuis un fichier JSON."""
def charger_craft():
    # Charge les crafts.
    if not os.path.exists(FICHIER_CRAFT):
        return []

    with open(FICHIER_CRAFT, "r", encoding="utf-8") as f:
        craft_base = json.load(f)

    # Dictionnaire temporaire pour fusionner facilement
    dictionnaire_crafts = {}

    for craft in craft_base:
        # On utilise l'ID comme clé unique pour retrouver facilement chaque craft
        dictionnaire_crafts[craft["id"]] = craft

    dictionnaire_crafts = list(dictionnaire_crafts.values())
    return dictionnaire_crafts


def dessiner_craft():
    pass


def ouvrir_craft():
    pass