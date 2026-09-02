import hashlib
import uuid
import random
import pygame
import os
import json
import time

import personnage
import boutique
import craft

FICHIER_MINERAI = "./data/minerais.json"

argent = 0

temps_joue_sauvegarde = 0
temps_debut_session = pygame.time.get_ticks()

"""Fonction pour charger les minerais depuis un fichier JSON."""
def charger_minerai():
    # Charge les minerais.
    if not os.path.exists(FICHIER_MINERAI):
        return []

    with open(FICHIER_MINERAI, "r", encoding="utf-8") as f:
        minerai_base = json.load(f)

    # Dictionnaire temporaire pour fusionner facilement
    dictionnaire_minerai = {}
    for minerai in minerai_base:
        # On utilise l'ID comme clé unique pour retrouver facilement chaque minerai
        dictionnaire_minerai[minerai["id"]] = minerai

    dictionnaire_minerai = list(dictionnaire_minerai.values())
    return dictionnaire_minerai



"""Fonctions pour générer un nom de planète et ses caractéristiques à partir d'un texte saisi par l'utilisateur."""
def decoder_nom_planete(texte_saisi):
    seed_num = int(hashlib.sha256(texte_saisi.encode()).hexdigest(), 16)
    random.seed(seed_num)
    
    consonnes = ["V", "K", "T", "R", "L", "M", "N", "Z", "X", "B", "D", "P"]
    voyelles = ["a", "e", "i", "o", "u", "y"]
    
    nom_genere = random.choice(consonnes) + random.choice(voyelles) + random.choice(consonnes) + random.choice(voyelles)
    nom_genere = nom_genere.capitalize()
    
    couleur_rgb = (random.randint(20, 250), random.randint(20, 250), random.randint(20, 250))
    distance = random.randint(100, 1000)

    
    liste_minerai = charger_minerai()

     # On choisit 5 minerais à partir de la seed
    minerais_choisis = random.sample(liste_minerai, 5) 
    
    # Assigner des pourcentages uniques (ex: 2%, 5%, 10%, 20%, 30%)
    pourcentages = [0.02, 0.05, 0.10, 0.20, 0.35]
    random.shuffle(pourcentages)
    
    minerais_avec_stats = []
    for i in range(5):
        minerais_avec_stats.append({
            "type": minerais_choisis[i],
            "pourcentage": int(pourcentages[i] * 100) # En pourcentage (ex: 5%)
        })
    
    return {
        "nom_officiel": nom_genere,
        "seed": seed_num,
        "couleur": couleur_rgb,
        "distance": distance,
        "minerais": minerais_avec_stats
    }

"""Génère une planète aléatoire avec un nom unique et des caractéristiques basées sur un UUID."""
def generer_planete():
    seed_str = str(uuid.uuid4())[:8]
    seed_num = int(hashlib.sha256(seed_str.encode()).hexdigest(), 16)
    random.seed(seed_num)
    
    consonnes = ["V", "K", "T", "R", "L", "M", "N", "Z", "X", "B", "D", "P"]
    voyelles = ["a", "e", "i", "o", "u", "y"]
    
    nom_genere = random.choice(consonnes) + random.choice(voyelles) + random.choice(consonnes) + random.choice(voyelles)
    nom_genere = nom_genere.capitalize()
    
    couleur_rgb = (random.randint(20, 250), random.randint(20, 250), random.randint(20, 250))
    distance = random.randint(100, 1000) * personnage.level  

    liste_minerai = charger_minerai()

    # Filtre les minerais selon le niveau du personnage
    minerais_choisis = [m for m in liste_minerai if m['id'] <= (personnage.level * 10)] 

    # Sécurité si le niveau est très bas (on prend les 10 premiers par défaut)
    if len(minerais_choisis) < 5:
        minerais_choisis = liste_minerai[:10]
    
    # On sélectionne jusqu'à 5 minerais sans risquer le crash
    nombre_a_prendre = min(5, len(minerais_choisis))
    minerais_selectionnes = random.sample(minerais_choisis, nombre_a_prendre)
    
    pourcentages = [0.02, 0.05, 0.10, 0.20, 0.35][:nombre_a_prendre]
    random.shuffle(pourcentages)
    
    minerais_avec_stats = []
    for i in range(nombre_a_prendre):
        minerais_avec_stats.append({
            "type": minerais_selectionnes[i],
            "pourcentage": int(pourcentages[i] * 100)
        })
    
    return {
        "nom_officiel": nom_genere,
        "seed": seed_str,
        "couleur": couleur_rgb,
        "distance": distance,
        "minerais": minerais_avec_stats
    }


"""Fonction pour vérifier quel minerai se trouve à une position donnée (x, y) sur la planète."""
def verifier_minerai_a_position(seed_num, x, y, minerais_config):
    position_hash = seed_num + x * 73856093 ^ y * 19349663
    rnd = random.Random(position_hash)
    
    # On tire un nombre aléatoire entre 0 et 1 (0% à 100%)
    valeur_de_chance = rnd.random()
    
    # On teste chaque minerai selon son pourcentage de présence
    seuil_cumule = 0.0
    for minerai in minerais_config:
        seuil_cumule += minerai["pourcentage"] / 100.0
        if valeur_de_chance < seuil_cumule:
            return minerai["type"]
            
    return None # Aucun minerai (roche vide)

"""Fonction pour obtenir le temps total de jeu en secondes, incluant la session actuelle et les sessions précédentes sauvegardées."""
def obtenir_temps_total():
    return temps_joue_sauvegarde + ((pygame.time.get_ticks() - temps_debut_session) // 1000)

"""Fonction pour sauvegarder l'état actuel du jeu dans un fichier JSON."""
def sauvegarder_partie():
    if os.path.exists("sauvegarde.json"):
        try:
            with open("sauvegarde.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    data["argent"] = argent
    data["temps_joue"] = obtenir_temps_total()

    with open("sauvegarde.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


infos = decoder_nom_planete(input("Entrez un texte pour générer une planète : "))
print(f"Planète : {infos['nom_officiel']} (Distance: {infos['distance']}, RGB: {infos['couleur']})")
print("Minerais et leurs pourcentages de présence :")
for m in infos['minerais']:
    print(f"- Type {m['type']} : {m['pourcentage']}% de chance")

# Test d'une vérification à la volée pour des coordonnées (ex: x=42, y=128)
minerai_trouve = verifier_minerai_a_position(infos['seed'], personnage.perso_x, personnage.perso_y, infos['minerais'])
print(f"À la position ({personnage.perso_x}, {personnage.perso_y}), il y a le minerai : {minerai_trouve}")

suite = input("Lancer script? (Appuyez sur O pour continuer, B pour la boutique et N pour quitter) : ")

if suite.upper() == "O":
    infos_auto = generer_planete()
    print(f"Planète auto : {infos_auto['nom_officiel']} (Seed: {infos_auto['seed']}), Minerais: {infos_auto['minerais']}")
elif suite.upper() == "B":
    boutique.ouvrir_boutique()
    print("Ouverture de la boutique...")
elif suite.upper() == "C":
    craft.ouvrir_craft()
    print("Ouverture de l'atelier...")
elif suite.upper() == "N":
    print("Fin du programme.")
    exit()

"""jeu_en_cours = True
while jeu_en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                pass"""