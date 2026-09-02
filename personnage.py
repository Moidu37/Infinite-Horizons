import pygame

perso_x = 0
perso_y = 0

level = 1
minerais = []
planete_actuelle = "Terre"

def mettre_a_jour_personnage(ecran):
    global perso_x, perso_y, index_frame, compteur_animation, regarde_a_gauche, personnage_final
    
    largeur_actuelle, hauteur_actuelle = ecran.get_size()
    
    # Calcul basé sur le ratio de surface pour l'UWQHD
    surface_base = 800 * 500
    surface_actuelle = largeur_actuelle * hauteur_actuelle
    ratio_surface = surface_actuelle / surface_base
    
    # La racine carrée adoucit la montée en vitesse sur les très grands écrans
    echelle = math.sqrt(ratio_surface)
    
    # On limite l'échelle à x2 maximum pour éviter l'effet "Flash" en UWQHD
    echelle = min(echelle, 2.0)
    
    vitesse = VITESSE_BASE * echelle

    touches = pygame.key.get_pressed()
    en_deplacement = False

    if touches[pygame.K_RIGHT] or touches[pygame.K_d]:
        perso_x += vitesse
        en_deplacement = True
        regarde_a_gauche = False
    if touches[pygame.K_LEFT] or touches[pygame.K_q]:
        perso_x -= vitesse
        en_deplacement = True
        regarde_a_gauche = True
    if touches[pygame.K_UP] or touches[pygame.K_z]:
        perso_y -= vitesse
        en_deplacement = True
    if touches[pygame.K_DOWN] or touches[pygame.K_s]:
        perso_y += vitesse
        en_deplacement = True

    frames_actuelles = frames_gauche if regarde_a_gauche else frames_droite

    if en_deplacement:
        compteur_animation += 1
        if compteur_animation >= vitesse_animation:
            compteur_animation = 0
            index_frame = (index_frame + 1) % len(frames_actuelles)
            personnage_final = frames_actuelles[index_frame]
    else:
        compteur_animation = 0
        index_frame = 0
        personnage_final = frames_actuelles[0]

    hitbox_personnage.topleft = (int(perso_x), int(perso_y))
    hitbox_personnage.clamp_ip(ecran.get_rect())
    perso_x, perso_y = hitbox_personnage.topleft

    return personnage_final, hitbox_personnage