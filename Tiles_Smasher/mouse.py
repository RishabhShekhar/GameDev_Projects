import pygame

pygame.init()

clock = pygame.time.Clock()

sw = 200
sh = 100

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("TILES")
game_font = pygame.font.Font("freesansbold.ttf", 60)

running = True
while running:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # LEFT CLICK
                print("LEFT CLICK")
            elif event.button == 2:  # MIDDLE CLICK
                print("MIDDLE CLICK")
            elif event.button == 3:  # RIGHT CLICK
                print("RIGHT CLICK")
            elif event.button == 4:  # WHEEL UP
                print("WHEEL UP")
            elif event.button == 5:  # WHEEL DOWN
                print("WHEEL DOWN")

    clock.tick(30)
    pygame.display.update()
