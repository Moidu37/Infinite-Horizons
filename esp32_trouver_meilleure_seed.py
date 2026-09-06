import hashlib
import random
import json

MINERAIS_DB = [
  {
    "id": 1,
    "prix": 1.0,
    "nom": "Ferraillite"
  },
  {
    "id": 2,
    "prix": 2.5,
    "nom": "Alunite Grise"
  },
  {
    "id": 3,
    "prix": 4.0,
    "nom": "Zincite Terne"
  },
  {
    "id": 4,
    "prix": 6.0,
    "nom": "Étainite Molle"
  },
  {
    "id": 5,
    "prix": 8.5,
    "nom": "Plombite Sombre"
  },
  {
    "id": 6,
    "prix": 11.0,
    "nom": "Cuivrite Rouge"
  },
  {
    "id": 7,
    "prix": 14.0,
    "nom": "Nickélite Brute"
  },
  {
    "id": 8,
    "prix": 18.0,
    "nom": "Manganite Rugueuse"
  },
  {
    "id": 9,
    "prix": 22.0,
    "nom": "Chromite Terreuse"
  },
  {
    "id": 10,
    "prix": 27.0,
    "nom": "Magnésite Poudreuse"
  },
  {
    "id": 11,
    "prix": 33.0,
    "nom": "Titanite Grise"
  },
  {
    "id": 12,
    "prix": 40.0,
    "nom": "Argentite Pâle"
  },
  {
    "id": 13,
    "prix": 48.0,
    "nom": "Cobaltite Bleutée"
  },
  {
    "id": 14,
    "prix": 57.0,
    "nom": "Antimoinite Noire"
  },
  {
    "id": 15,
    "prix": 67.0,
    "nom": "Bismuthite Violette"
  },
  {
    "id": 16,
    "prix": 78.0,
    "nom": "Molybdénite Sombre"
  },
  {
    "id": 17,
    "prix": 90.0,
    "nom": "Tungstite Dense"
  },
  {
    "id": 18,
    "prix": 103.0,
    "nom": "Béryllite Claire"
  },
  {
    "id": 19,
    "prix": 117.0,
    "nom": "Cadmite Jaune"
  },
  {
    "id": 20,
    "prix": 132.0,
    "nom": "Zircite Fumée"
  },
  {
    "id": 21,
    "prix": 148.0,
    "nom": "Niobite Brillante"
  },
  {
    "id": 22,
    "prix": 165.0,
    "nom": "Tantalite Dorée"
  },
  {
    "id": 23,
    "prix": 183.0,
    "nom": "Hafnite Cristalline"
  },
  {
    "id": 24,
    "prix": 202.0,
    "nom": "Germanite Grise"
  },
  {
    "id": 25,
    "prix": 222.0,
    "nom": "Galite Métallique"
  },
  {
    "id": 26,
    "prix": 243.0,
    "nom": "Sélénite Rouge"
  },
  {
    "id": 27,
    "prix": 265.0,
    "nom": "Tellurite Blanche"
  },
  {
    "id": 28,
    "prix": 288.0,
    "nom": "Orite Brute"
  },
  {
    "id": 29,
    "prix": 312.0,
    "nom": "Platinite Lourde"
  },
  {
    "id": 30,
    "prix": 337.0,
    "nom": "Palladite Grise"
  },
  {
    "id": 31,
    "prix": 363.0,
    "nom": "Rhodite Rosée"
  },
  {
    "id": 32,
    "prix": 390.0,
    "nom": "Ruthénite Bleue"
  },
  {
    "id": 33,
    "prix": 418.0,
    "nom": "Iridite Sombre"
  },
  {
    "id": 34,
    "prix": 447.0,
    "nom": "Osmite Noire"
  },
  {
    "id": 35,
    "prix": 477.0,
    "nom": "Rhénite Dense"
  },
  {
    "id": 36,
    "prix": 508.0,
    "nom": "Scandite Claire"
  },
  {
    "id": 37,
    "prix": 540.0,
    "nom": "Yttrite Blanche"
  },
  {
    "id": 38,
    "prix": 573.0,
    "nom": "Cérite Orangée"
  },
  {
    "id": 39,
    "prix": 607.0,
    "nom": "Néodymite Violette"
  },
  {
    "id": 40,
    "prix": 642.0,
    "nom": "Samarite Grise"
  },
  {
    "id": 41,
    "prix": 678.0,
    "nom": "Gadolinite Brillante"
  },
  {
    "id": 42,
    "prix": 715.0,
    "nom": "Dysprosite Dorée"
  },
  {
    "id": 43,
    "prix": 753.0,
    "nom": "Erbite Rose"
  },
  {
    "id": 44,
    "prix": 792.0,
    "nom": "Ytterbite Claire"
  },
  {
    "id": 45,
    "prix": 832.0,
    "nom": "Lutécite Dense"
  },
  {
    "id": 46,
    "prix": 873.0,
    "nom": "Uranite Verte"
  },
  {
    "id": 47,
    "prix": 915.0,
    "nom": "Thorite Sombre"
  },
  {
    "id": 48,
    "prix": 958.0,
    "nom": "Radite Lumineuse"
  },
  {
    "id": 49,
    "prix": 1002.0,
    "nom": "Poloniite Grise"
  },
  {
    "id": 50,
    "prix": 1047.0,
    "nom": "Francite Ancienne"
  },
  {
    "id": 51,
    "prix": 1093.0,
    "nom": "Erbium"
  },
  {
    "id": 52,
    "prix": 1140.0,
    "nom": "Thulium"
  },
  {
    "id": 53,
    "prix": 1188.0,
    "nom": "Ytterbium"
  },
  {
    "id": 54,
    "prix": 1237.0,
    "nom": "Lutécium"
  },
  {
    "id": 55,
    "prix": 1287.0,
    "nom": "Uranium"
  },
  {
    "id": 56,
    "prix": 1338.0,
    "nom": "Thorium"
  },
  {
    "id": 57,
    "prix": 1390.0,
    "nom": "Radium"
  },
  {
    "id": 58,
    "prix": 1443.0,
    "nom": "Polonium"
  },
  {
    "id": 59,
    "prix": 1497.0,
    "nom": "Francium"
  },
  {
    "id": 60,
    "prix": 1552.0,
    "nom": "Actinium"
  },
  {
    "id": 61,
    "prix": 1608.0,
    "nom": "Protactinium"
  },
  {
    "id": 62,
    "prix": 1665.0,
    "nom": "Neptunium"
  },
  {
    "id": 63,
    "prix": 1723.0,
    "nom": "Plutonium"
  },
  {
    "id": 64,
    "prix": 1782.0,
    "nom": "Américium"
  },
  {
    "id": 65,
    "prix": 1842.0,
    "nom": "Curium"
  },
  {
    "id": 66,
    "prix": 1903.0,
    "nom": "Berkélium"
  },
  {
    "id": 67,
    "prix": 1965.0,
    "nom": "Californium"
  },
  {
    "id": 68,
    "prix": 2028.0,
    "nom": "Einsteinium"
  },
  {
    "id": 69,
    "prix": 2092.0,
    "nom": "Fermium"
  },
  {
    "id": 70,
    "prix": 2157.0,
    "nom": "Mendélévium"
  },
  {
    "id": 71,
    "prix": 2223.0,
    "nom": "Nobélium"
  },
  {
    "id": 72,
    "prix": 2290.0,
    "nom": "Lawrencium"
  },
  {
    "id": 73,
    "prix": 2358.0,
    "nom": "Rutherfordium"
  },
  {
    "id": 74,
    "prix": 2427.0,
    "nom": "Dubnium"
  },
  {
    "id": 75,
    "prix": 2497.0,
    "nom": "Seaborgium"
  },
  {
    "id": 76,
    "prix": 2568.0,
    "nom": "Bohrium"
  },
  {
    "id": 77,
    "prix": 2640.0,
    "nom": "Hassium"
  },
  {
    "id": 78,
    "prix": 2713.0,
    "nom": "Meitnérium"
  },
  {
    "id": 79,
    "prix": 2787.0,
    "nom": "Darmstadtium"
  },
  {
    "id": 80,
    "prix": 2862.0,
    "nom": "Roentgenium"
  },
  {
    "id": 81,
    "prix": 2938.0,
    "nom": "Copernicium"
  },
  {
    "id": 82,
    "prix": 3015.0,
    "nom": "Nihonium"
  },
  {
    "id": 83,
    "prix": 3093.0,
    "nom": "Flérovium"
  },
  {
    "id": 84,
    "prix": 3172.0,
    "nom": "Moscovium"
  },
  {
    "id": 85,
    "prix": 3252.0,
    "nom": "Livermorium"
  },
  {
    "id": 86,
    "prix": 3333.0,
    "nom": "Tennesse"
  },
  {
    "id": 87,
    "prix": 3415.0,
    "nom": "Oganesson"
  },
  {
    "id": 88,
    "prix": 3498.0,
    "nom": "Rhodium stellaire"
  },
  {
    "id": 89,
    "prix": 3582.0,
    "nom": "Osmium noir"
  },
  {
    "id": 90,
    "prix": 3667.0,
    "nom": "Iridium bleu"
  },
  {
    "id": 91,
    "prix": 3753.0,
    "nom": "Platine gris"
  },
  {
    "id": 92,
    "prix": 3840.0,
    "nom": "Or blanc rare"
  },
  {
    "id": 93,
    "prix": 3928.0,
    "nom": "Or rose ancien"
  },
  {
    "id": 94,
    "prix": 4017.0,
    "nom": "Argent météoritique"
  },
  {
    "id": 95,
    "prix": 4107.0,
    "nom": "Fer météoritique"
  },
  {
    "id": 96,
    "prix": 4198.0,
    "nom": "Nickel lunaire"
  },
  {
    "id": 97,
    "prix": 4290.0,
    "nom": "Titane spatial"
  },
  {
    "id": 98,
    "prix": 4383.0,
    "nom": "Palladium abyssal"
  },
  {
    "id": 99,
    "prix": 4477.0,
    "nom": "Rhénium volcanique"
  },
  {
    "id": 100,
    "prix": 4572.0,
    "nom": "Osmium abyssal"
  },
  {
    "id": 101,
    "prix": 4668.0,
    "nom": "Iridium cosmique"
  },
  {
    "id": 102,
    "prix": 4765.0,
    "nom": "Uranium enrichi"
  },
  {
    "id": 103,
    "prix": 4863.0,
    "nom": "Plutonium pur"
  },
  {
    "id": 104,
    "prix": 4962.0,
    "nom": "Neptunium stable"
  },
  {
    "id": 105,
    "prix": 5062.0,
    "nom": "Américium cristallin"
  },
  {
    "id": 106,
    "prix": 5163.0,
    "nom": "Curium rare"
  },
  {
    "id": 107,
    "prix": 5265.0,
    "nom": "Californium pur"
  },
  {
    "id": 108,
    "prix": 5368.0,
    "nom": "Einsteinium stable"
  },
  {
    "id": 109,
    "prix": 5472.0,
    "nom": "Adamantium"
  },
  {
    "id": 110,
    "prix": 5577.0,
    "nom": "Orichalque pur"
  },
  {
    "id": 111,
    "prix": 5683.0,
    "nom": "Mithril forgé"
  },
  {
    "id": 112,
    "prix": 5790.0,
    "nom": "Vibranium"
  },
  {
    "id": 113,
    "prix": 5898.0,
    "nom": "Naquadah"
  },
  {
    "id": 114,
    "prix": 6007.0,
    "nom": "Dilithium"
  },
  {
    "id": 115,
    "prix": 6117.0,
    "nom": "Kryptonite"
  },
  {
    "id": 116,
    "prix": 6228.0,
    "nom": "Unobtanium"
  },
  {
    "id": 117,
    "prix": 6340.0,
    "nom": "Éthérium"
  },
  {
    "id": 118,
    "prix": 6453.0,
    "nom": "Astatium"
  },
  {
    "id": 119,
    "prix": 6567.0,
    "nom": "Chronium"
  },
  {
    "id": 120,
    "prix": 6682.0,
    "nom": "Voidmétal"
  },
  {
    "id": 121,
    "prix": 6798.0,
    "nom": "Starmetal"
  },
  {
    "id": 122,
    "prix": 6915.0,
    "nom": "Umbrite"
  },
  {
    "id": 123,
    "prix": 7033.0,
    "nom": "Prismium"
  },
  {
    "id": 124,
    "prix": 7152.0,
    "nom": "Solarium"
  },
  {
    "id": 125,
    "prix": 7272.0,
    "nom": "Lunarium"
  },
  {
    "id": 126,
    "prix": 7393.0,
    "nom": "Nébulite"
  },
  {
    "id": 127,
    "prix": 7515.0,
    "nom": "Astralium"
  },
  {
    "id": 128,
    "prix": 7638.0,
    "nom": "Célestium"
  },
  {
    "id": 129,
    "prix": 7762.0,
    "nom": "Zénithium"
  },
  {
    "id": 130,
    "prix": 7887.0,
    "nom": "Éclipsium"
  },
  {
    "id": 131,
    "prix": 8013.0,
    "nom": "Novacier"
  },
  {
    "id": 132,
    "prix": 8140.0,
    "nom": "Pulsarite"
  },
  {
    "id": 133,
    "prix": 8268.0,
    "nom": "Quasarium"
  },
  {
    "id": 134,
    "prix": 8397.0,
    "nom": "Galaxite"
  },
  {
    "id": 135,
    "prix": 8527.0,
    "nom": "Cosmium"
  },
  {
    "id": 136,
    "prix": 8658.0,
    "nom": "Infinitium"
  },
  {
    "id": 137,
    "prix": 8790.0,
    "nom": "Éternium"
  },
  {
    "id": 138,
    "prix": 8923.0,
    "nom": "Primordium"
  },
  {
    "id": 139,
    "prix": 9057.0,
    "nom": "Génésium"
  },
  {
    "id": 140,
    "prix": 9192.0,
    "nom": "Apexium"
  },
  {
    "id": 141,
    "prix": 9328.0,
    "nom": "Zénith noir"
  },
  {
    "id": 142,
    "prix": 9465.0,
    "nom": "Argent stellaire"
  },
  {
    "id": 143,
    "prix": 9603.0,
    "nom": "Or cosmique"
  },
  {
    "id": 144,
    "prix": 9742.0,
    "nom": "Platine astral"
  },
  {
    "id": 145,
    "prix": 9882.0,
    "nom": "Diamantium"
  },
  {
    "id": 146,
    "prix": 10023.0,
    "nom": "Cristal métallique"
  },
  {
    "id": 147,
    "prix": 10165.0,
    "nom": "Alliage royal"
  },
  {
    "id": 148,
    "prix": 10308.0,
    "nom": "Métal antique"
  },
  {
    "id": 149,
    "prix": 10452.0,
    "nom": "Acier céleste"
  },
  {
    "id": 150,
    "prix": 10597.0,
    "nom": "Métal ultime"
  }
]

def decoder_nom_planete(texte_saisi):
    h = hashlib.sha256(texte_saisi.encode())
    digest_bytes = h.digest()
    hex_str = "".join(["{:02x}".format(b) for b in digest_bytes])
    seed_num = int(hex_str, 16)
    
    random.seed(seed_num)
    
    consonnes = ["V", "K", "T", "R", "L", "M", "N", "Z", "X", "B", "D", "P"]
    voyelles = ["a", "e", "i", "o", "u", "y"]
    
    nom_genere = random.choice(consonnes) + random.choice(voyelles) + random.choice(consonnes) + random.choice(voyelles)
    nom_genere = nom_genere[0].upper() + nom_genere[1:]
    
    taille = random.randint(400, 1200)
    couleur_rgb = (random.randint(20, 250), random.randint(20, 250), random.randint(20, 250))
    pos_y = random.randint(100, 1000)
    
    minerais_choisis = []
    copie_db = list(MINERAIS_DB)
    for _ in range(min(5, len(copie_db))):
        index = random.randrange(len(copie_db))
        minerais_choisis.append(copie_db.pop(index))
        
    pourcentages = [0.02, 0.05, 0.10, 0.20, 0.35]
    for i in range(len(pourcentages) - 1, 0, -1):
        j = random.randrange(i + 1)
        pourcentages[i], pourcentages[j] = pourcentages[j], pourcentages[i]
    
    minerais_avec_stats = []
    for i in range(len(minerais_choisis)):
        minerais_avec_stats.append({
            "id": minerais_choisis[i]["id"],
            "nom": minerais_choisis[i]["nom"],
            "prix": minerais_choisis[i]["prix"],
            "pourcentage": int(pourcentages[i] * 100)
        })
        
    return {
        "nom_officiel": nom_genere,
        "seed": seed_num,
        "taille": taille,
        "couleur": couleur_rgb,
        "pos_y": pos_y,
        "minerais": minerais_avec_stats
    }

print("Recherche en continu... Appuyez sur Ctrl+C (ou Stop) pour arrêter et afficher le JSON.")

meilleure_note = 0
meilleure_infos = None
compteur = 0

try:
    while True:
        compteur += 1
        texte_test = f"seed_{compteur}"
        infos = decoder_nom_planete(texte_test)
        
        score_actuel = 0
        for m in infos['minerais']:
            prix = m.get("prix", 1.0)
            pourcentage = m['pourcentage'] / 100.0
            score_actuel += pourcentage * prix

        if score_actuel > meilleure_note:
            meilleure_note = score_actuel
            meilleure_infos = infos
            print(f"Record (Essai {compteur}) -> {infos['nom_officiel']} (Score: {score_actuel:.2f})")

except KeyboardInterrupt:
    print("\nArrêt utilisateur détecté.")

if meilleure_infos:
    rapport = {
        "total_essais": compteur,
        "meilleure_planete": meilleure_infos,
        "score_rentabilite": round(meilleure_note, 2)
    }
    print("\n--- RAPPORT JSON FINAL ---")
    print(json.dumps(rapport))
else:
    print("Aucune planète évaluée.")