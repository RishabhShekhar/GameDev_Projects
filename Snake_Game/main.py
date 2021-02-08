import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SNAKE GAME")

score = 0

snake_pos = [[300, 300], [320, 300], [340, 300], [360, 300]]

# DIRECTIONS
step = 20
up = (0, -step)
left = (-step, 0)
right = (step, 0)
down = (0, step)
direction = left

apple_pos = [260, 300]

timer = 0

font = pygame.font.SysFont('Arial', 30)

game_over = False

running = True

while running:

    pygame.time.Clock().tick(50)
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

    if snake_pos[0] == apple_pos:
        x = (random.randint(20, 780) // 20) * 20
        y = (random.randint(20, 580) // 20) * 20
        apple_pos = [x, y]
        snake_pos.append(snake_pos[-1])
        score += 1

    for i in range(1, len(snake_pos)):
        if snake_pos[0] == snake_pos[i]:
            game_over = True

    if game_over:
        print(score)
        running = False

    for x, y in snake_pos:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)

    pygame.draw.circle(screen, (0, 0, 255), apple_pos, 10)

    text = font.render(("SCORE: " + str(score)), True, (255, 255, 255))
    screen.blit(text, (0, 0))

    pygame.display.update()
