import os
import json
import pygame
import tkinter as tk
import boutique
from tkinter import filedialog
from datetime import datetime

# Initialisation discrète de tkinter
root = tk.Tk()
root.withdraw()

# Rectangles globaux pour les clics de la UI
rect_bouton_param = pygame.Rect(20, 0, 40, 40)
rect_btn_export = pygame.Rect(0, 0, 0, 0)
rect_btn_import = pygame.Rect(0, 0, 0, 0)
rect_btn_reset = pygame.Rect(0, 0, 0, 0)

# Variable globale pour l'image (chargement différé)
img_param = None


def exporter_sauvegarde(argent, total_pieces, nb_taches, quetes, temps_joue):
    """Exporte l'ensemble des données du jeu dans un fichier JSON avec horodatage."""
    nom_defaut = f"export_dungeon_cleaner_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    fichier_cible = filedialog.asksaveasfilename(
        initialfile=nom_defaut,
        defaultextension=".json",
        filetypes=[("Fichiers JSON", "*.json")],
        title="Exporter la sauvegarde"
    )
    if fichier_cible:
        data_save = {
            "argent": argent,
            "total_pieces_gagnees": total_pieces,
            "nb_taches_nettoyees": nb_taches,
            "temps_joue": temps_joue,
            "quetes": [
                {
                    "id": q["id"],
                    "progression": q["progression"],
                    "completee": q["completee"],
                    "reclamee": q["reclamee"]
                }
                for q in quetes
            ]
        }
        with open(fichier_cible, "w", encoding="utf-8") as f:
            json.dump(data_save, f, indent=2, ensure_ascii=False)


def importer_sauvegarde():
    """Importe un fichier JSON externe et l'écrase sur sauvegarde.json."""
    fichier_source = filedialog.askopenfilename(
        filetypes=[("Fichiers JSON", "*.json")],
        title="Importer une sauvegarde"
    )
    if fichier_source:
        try:
            with open(fichier_source, "r", encoding="utf-8") as source:
                data = json.load(source)
            with open("sauvegarde.json", "w", encoding="utf-8") as dest:
                json.dump(data, dest, indent=2, ensure_ascii=False)
            return data
        except json.JSONDecodeError:
            print("Erreur : Fichier JSON invalide.")
            return None
    return None


def reinitialiser_sauvegarde():
    """Supprime le fichier sauvegarde.json pour recommencer à zéro."""
    if os.path.exists("sauvegarde.json"):
        os.remove("sauvegarde.json")


def dessiner_bouton_parametres(surface, hauteur_ecran):
    """Dessine le bouton paramètres en bas à gauche avec l'image PNG."""
    global rect_bouton_param, img_param
    rect_bouton_param.y = hauteur_ecran - 60

    if img_param is None:
        img_param = pygame.transform.scale(
            pygame.image.load("./assets/parametre.png").convert_alpha(),
            (24, 24)
        )

    pygame.draw.rect(surface, (209, 209, 209, 220), rect_bouton_param, border_radius=8)
    pygame.draw.rect(surface, (255, 255, 255, 100), rect_bouton_param, 2, border_radius=8)

    x_img = rect_bouton_param.x + (rect_bouton_param.width - img_param.get_width()) // 2
    y_img = rect_bouton_param.y + (rect_bouton_param.height - img_param.get_height()) // 2
    surface.blit(img_param, (x_img, y_img))


def dessiner_menu_parametres(surface, largeur_ecran, hauteur_ecran, police_titre, police_texte):
    """Affiche la fenêtre de paramètres avec ses 3 boutons."""
    global rect_btn_export, rect_btn_import, rect_btn_reset

    largeur_win, hauteur_win = 280, 220
    x_win = (largeur_ecran - largeur_win) // 2
    y_win = (hauteur_ecran - hauteur_win) // 2

    rect_btn_export = pygame.Rect(x_win + 20, y_win + 50, 240, 38)
    rect_btn_import = pygame.Rect(x_win + 20, y_win + 100, 240, 38)
    rect_btn_reset  = pygame.Rect(x_win + 20, y_win + 155, 240, 38)

    surf = pygame.Surface((largeur_win, hauteur_win), pygame.SRCALPHA)
    pygame.draw.rect(surf, (20, 24, 30, 245), (0, 0, largeur_win, hauteur_win), border_radius=12)
    pygame.draw.rect(surf, (255, 255, 255, 80), (0, 0, largeur_win, hauteur_win), 2, border_radius=12)

    titre = police_titre.render("PARAMÈTRES", True, (255, 255, 255))
    surf.blit(titre, (15, 15))

    pygame.draw.rect(surface, (40, 100, 170), rect_btn_export, border_radius=6)
    pygame.draw.rect(surface, (40, 150, 90), rect_btn_import, border_radius=6)
    pygame.draw.rect(surface, (190, 50, 50), rect_btn_reset, border_radius=6)

    txt_export = police_texte.render("Exporter la sauvegarde", True, (255, 255, 255))
    txt_import = police_texte.render("Importer une sauvegarde", True, (255, 255, 255))
    txt_reset  = police_texte.render("Recommencer la partie", True, (255, 255, 255))

    surface.blit(surf, (x_win, y_win))
    surface.blit(txt_export, (rect_btn_export.x + (240 - txt_export.get_width()) // 2, rect_btn_export.y + 9))
    surface.blit(txt_import, (rect_btn_import.x + (240 - txt_import.get_width()) // 2, rect_btn_import.y + 9))
    surface.blit(txt_reset,  (rect_btn_reset.x + (240 - txt_reset.get_width()) // 2, rect_btn_reset.y + 9))


def dessiner_argent(surface, argent, police, largeur_ecran):
    txt = police.render(f"Pièces : {argent}", True, (255, 215, 0))
    largeur_boite = txt.get_width() + 20
    hauteur_boite = 35
    x = largeur_ecran - largeur_boite - 20
    y = 20
    surf = pygame.Surface((largeur_boite, hauteur_boite), pygame.SRCALPHA)
    pygame.draw.rect(surf, (20, 24, 30, 200), (0, 0, largeur_boite, hauteur_boite), border_radius=8)
    pygame.draw.rect(surf, (255, 215, 0, 180), (0, 0, largeur_boite, hauteur_boite), 2, border_radius=8)
    surface.blit(surf, (x, y))
    surface.blit(txt, (x + 10, y + (hauteur_boite - txt.get_height()) // 2))


def dessiner_stats(surface, nb_taches, total_pieces, temps_total, police_titre, police_texte, largeur_ecran, hauteur_ecran):
    largeur_win, hauteur_win = 300, 200
    x_win = (largeur_ecran - largeur_win) // 2
    y_win = (hauteur_ecran - hauteur_win) // 2
    
    minutes = temps_total // 60
    secondes = temps_total % 60
    str_temps = f"{minutes:02d}:{secondes:02d}"
    
    surf_stats = pygame.Surface((largeur_win, hauteur_win), pygame.SRCALPHA)
    pygame.draw.rect(surf_stats, (20, 24, 30, 235), (0, 0, largeur_win, hauteur_win), border_radius=12)
    pygame.draw.rect(surf_stats, (0, 180, 216, 180), (0, 0, largeur_win, hauteur_win), 2, border_radius=12)
    
    titre = police_titre.render("STATISTIQUES", True, (0, 180, 216))
    surf_stats.blit(titre, (15, 15))

    txt_temps = police_texte.render(f"Temps joué : {str_temps}", True, (255, 255, 255))
    txt_taches = police_texte.render(f"Tâches nettoyées : {nb_taches}", True, (255, 255, 255))
    txt_pieces = police_texte.render(f"Total pièces gagnées : {total_pieces}", True, (255, 255, 255))

    surf_stats.blit(txt_temps, (15, 60))
    surf_stats.blit(txt_taches, (15, 95))
    surf_stats.blit(txt_pieces, (15, 130))

    surface.blit(surf_stats, (x_win, y_win))


def dessiner_inventaire(surface, inventaire, police_titre, police_texte, largeur_ecran, hauteur_ecran):
    nb_cases, taille_case, marge_case, padding = 5, 60, 10, 15
    largeur_inv = (nb_cases * taille_case) + ((nb_cases - 1) * marge_case) + (padding * 2)
    hauteur_inv = taille_case + padding * 2 + 30
    x_inv = (largeur_ecran - largeur_inv) // 2
    y_inv = (hauteur_ecran - hauteur_inv) // 2
    surface_inv = pygame.Surface((largeur_inv, hauteur_inv), pygame.SRCALPHA)
    pygame.draw.rect(surface_inv, (20, 24, 30, 230), (0, 0, largeur_inv, hauteur_inv), border_radius=12)
    pygame.draw.rect(surface_inv, (255, 255, 255, 60), (0, 0, largeur_inv, hauteur_inv), 2, border_radius=12)
    texte_titre = police_titre.render("INVENTAIRE", True, (255, 255, 255))
    surface_inv.blit(texte_titre, (padding, padding))
    y_cases = padding + 30
    for i in range(nb_cases):
        x_case = padding + i * (taille_case + marge_case)
        pygame.draw.rect(surface_inv, (45, 50, 60), (x_case, y_cases, taille_case, taille_case), border_radius=8)
        pygame.draw.rect(surface_inv, (100, 110, 130), (x_case, y_cases, taille_case, taille_case), 2, border_radius=8)
        objet = inventaire[i]
        if objet is not None:
            texte_obj = police_texte.render(objet, True, (255, 255, 255))
            obj_x = x_case + (taille_case - texte_obj.get_width()) // 2
            obj_y = y_cases + (taille_case - texte_obj.get_height()) // 2
            surface_inv.blit(texte_obj, (obj_x, obj_y))
    surface.blit(surface_inv, (x_inv, y_inv))


def dessiner_popup_action(surface, tache_rect, surface_cle, surface_action, largeur_ecran):
    padding, espace_entre = 8, 10
    taille_touche = max(surface_cle.get_width(), surface_cle.get_height()) + 8
    largeur_totale = padding * 2 + taille_touche + espace_entre + surface_action.get_width()
    hauteur_totale = padding * 2 + max(taille_touche, surface_action.get_height())
    x_popup = max(10, min(tache_rect.centerx - (largeur_totale // 2), largeur_ecran - largeur_totale - 10))
    y_popup = tache_rect.top - hauteur_totale - 12
    if y_popup < 0:
        y_popup = tache_rect.bottom + 12
    surface_popup = pygame.Surface((largeur_totale, hauteur_totale), pygame.SRCALPHA)
    pygame.draw.rect(surface_popup, (20, 24, 30, 220), (0, 0, largeur_totale, hauteur_totale), border_radius=12)
    pygame.draw.rect(surface_popup, (255, 255, 255, 60), (0, 0, largeur_totale, hauteur_totale), 2, border_radius=12)
    pos_touche_x = padding
    pos_touche_y = (hauteur_totale - taille_touche) // 2
    pygame.draw.rect(surface_popup, (45, 50, 60), (pos_touche_x, pos_touche_y, taille_touche, taille_touche), border_radius=6)
    pygame.draw.rect(surface_popup, (100, 110, 130), (pos_touche_x, pos_touche_y, taille_touche, taille_touche), 1, border_radius=6)
    surface_popup.blit(surface_cle, (pos_touche_x + (taille_touche - surface_cle.get_width()) // 2, pos_touche_y + (taille_touche - surface_cle.get_height()) // 2))
    surface_popup.blit(surface_action, (pos_touche_x + taille_touche + espace_entre, (hauteur_totale - surface_action.get_height()) // 2))
    surface.blit(surface_popup, (x_popup, y_popup))

def dessiner_fenetre_boutique(surface, articles, police_titre, police_texte, largeur_ecran, hauteur_ecran):
    largeur_win, hauteur_win = 600, 400
    x_win = (largeur_ecran - largeur_win) // 2
    y_win = (hauteur_ecran - hauteur_win) // 2

    # Surface principale de la fenêtre
    surf_fenetre = pygame.Surface((largeur_win, hauteur_win), pygame.SRCALPHA)
    pygame.draw.rect(surf_fenetre, (20, 24, 30, 245), (0, 0, largeur_win, hauteur_win), border_radius=12)
    pygame.draw.rect(surf_fenetre, (255, 215, 0, 150), (0, 0, largeur_win, hauteur_win), 2, border_radius=12)

    titre = police_titre.render("BOUTIQUE", True, (255, 215, 0))
    surf_fenetre.blit(titre, (20, 15))

    # Zone découpée (Viewport) pour contenir les cartes d'articles
    hauteur_zone = 310
    largeur_zone = largeur_win - 50
    zone_articles = pygame.Surface((largeur_zone, hauteur_zone), pygame.SRCALPHA)

    # Dessin des articles dans la zone défilante
    y_item = -boutique.defilement_y
    hauteur_totale_contenu = len(articles) * 88

    for item in articles:
        if not isinstance(item, dict):
            continue

        # Dessine uniquement si l'élément est visible à l'écran
        if -80 <= y_item <= hauteur_zone:
            pygame.draw.rect(zone_articles, (35, 40, 50), (0, y_item, largeur_zone - 15, 80), border_radius=8)
            pygame.draw.rect(zone_articles, (70, 80, 95), (0, y_item, largeur_zone - 15, 80), 1, border_radius=8)

            nom = item.get("titre", "Objet inconnu")
            desc = item.get("description", "")
            prix = item.get("prix", 0)
            temps = item.get("temps", 0)

            txt_nom = police_titre.render(nom, True, (255, 255, 255))
            txt_desc = police_texte.render(desc, True, (180, 190, 205))
            txt_prix = police_texte.render(f"{prix} pièces | Temps : {temps}s", True, (255, 215, 0))

            zone_articles.blit(txt_nom, (15, y_item + 8))
            zone_articles.blit(txt_desc, (15, y_item + 32))
            zone_articles.blit(txt_prix, (15, y_item + 54))

        y_item += 88

    # Blit de la zone d'articles sur la fenêtre
    surf_fenetre.blit(zone_articles, (20, 55))

    # --- BARRE DE DÉFILEMENT (SCROLLBAR) ---
    if hauteur_totale_contenu > hauteur_zone:
        x_barre = largeur_win - 20
        y_barre = 55
        hauteur_rail = hauteur_zone

        # Rail de la scrollbar
        pygame.draw.rect(surf_fenetre, (40, 45, 55), (x_barre, y_barre, 8, hauteur_rail), border_radius=4)

        # Curseur mobile
        taille_curseur = max(20, int((hauteur_zone / hauteur_totale_contenu) * hauteur_rail))
        ratio_scroll = boutique.defilement_y / (hauteur_totale_contenu - hauteur_zone)
        pos_curseur = y_barre + int(ratio_scroll * (hauteur_rail - taille_curseur))

        pygame.draw.rect(surf_fenetre, (255, 215, 0), (x_barre, pos_curseur, 8, taille_curseur), border_radius=4)

    surface.blit(surf_fenetre, (x_win, y_win))