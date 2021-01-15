import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SNAKE GAME")

running = True

snake_pos = [[300, 300], [340, 300], [380, 300], [420, 300]]

step = 30
up = (0, -step)
left = (-step, 0)
right = (step, 0)
down = (0, step)
direction = left

timer = 0

while running:
    pygame.time.Clock().tick(30)
    screen.fill((20, 100, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                direction = down
            elif event.key == pygame.K_UP:
                direction = up
            elif event.key == pygame.K_LEFT:
                direction = left
            elif event.key == pygame.K_RIGHT:
                direction = right

    timer += 1
    if timer == 5:
        snake_pos = [[snake_pos[0][0] + direction[0], snake_pos[0][1] + direction[1]]] + snake_pos[:-1]
        timer = 0

    for x, y in snake_pos:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)

    pygame.display.update()


