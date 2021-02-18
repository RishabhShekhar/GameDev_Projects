import pygame

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow():
    screen.fill((255, 255, 255))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()