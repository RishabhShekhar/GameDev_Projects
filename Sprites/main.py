import pygame
import random

clock = pygame.time.Clock()

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


pygame.init()

sw = 700
sh = 400

screen = pygame.display.set_mode((sw, sh))
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(10):
    block = Block(black, 30, 30)

    block.rect.x = random.randrange(sw)
    block.rect.y = random.randrange(sh)

    block_list.add(block)
    all_sprites_list.add(block)

running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(20)
    pygame.display.update()
