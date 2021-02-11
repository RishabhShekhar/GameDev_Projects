import pygame
import random

clock = pygame.time.Clock()

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()  # Initialize Sprite Class

        self.image = pygame.Surface([width, height])  # Surface--> small screen
        self.image.fill(color)

        self.rect = self.image.get_rect()


pygame.init()

sw = 700
sh = 400

screen = pygame.display.set_mode((sw, sh))
block_list = pygame.sprite.Group()  # Not have to handle every square individually which we will eat
all_sprites_list = pygame.sprite.Group()

for i in range(30):  # Insert blocks in blocks list
    block = Block(black, 30, 30)

    block.rect.x = random.randrange(sw)
    block.rect.y = random.randrange(sh)

    block_list.add(block)
    # all_sprites_list.add(block)

player = Block(red, 30, 30)
all_sprites_list.add(player)

score = 0

running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pos = pygame.mouse.get_pos()
    # print(pos)

    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in block_hit_list:
        score += 1
        print(score)

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    block_list.draw(screen)
    all_sprites_list.draw(screen)


    clock.tick(20)
    pygame.display.update()
