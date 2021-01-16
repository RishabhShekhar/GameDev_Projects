import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FLAPPY BIRDS")


running = True
while running:
    screen.fill((120, 120, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
