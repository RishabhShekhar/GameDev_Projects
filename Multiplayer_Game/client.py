import pygame
from network import Network

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val
        if keys[pygame.K_RIGHT]:
            self.x += self.val
        if keys[pygame.K_UP]:
            self.y -= self.val
        if keys[pygame.K_DOWN]:
            self.y += self.val

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(screen, player):
    screen.fill((255, 255, 255))
    player.draw(screen)
    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True
    n = Network()
    startPos = n.getPos()
    p = Player(50, 50, 100, 100, (0, 255, 0))

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # pygame.quit()

        p.move()
        redrawWindow(screen, p)

main()