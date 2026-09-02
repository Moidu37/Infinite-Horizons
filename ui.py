import pygame


pygame.init()

pygame.display.set_caption('Infinite Horizons')
window_surface = pygame.display.set_mode((1280, 720))

background = pygame.Surface((1280, 720))
background.fill(pygame.Color('#000000'))

is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))


    pygame.display.update()