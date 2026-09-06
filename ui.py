import pygame
import personnage

is_running = True

background = pygame.Surface((1280, 720))

# Charger les images
logo_piece = pygame.image.load("./assets/piece.png").convert_alpha()

# Redimensionner l'image
logo_piece = pygame.transform.smoothscale(logo_piece, (40, 40))



#Affichage de l'écriture
font=pygame.font.Font(None, 24)
text_pieces = font.render("Pièce(s)",1,(255, 255, 255))


def afficher_menu(window_surface):
    pygame.draw.rect(window_surface, (107, 3, 128), (20, 35, 70, 650), width=0, border_radius=7)