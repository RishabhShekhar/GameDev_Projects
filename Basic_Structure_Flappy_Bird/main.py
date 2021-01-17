import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FLAPPY BIRDS")

x = 200
y = 300
jump = False
speed = 0.5
def draw_circle(x,y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

pipe1 = [600, 0, 50, random.randint(50,250)]
pipe2 = [400, 0, 50, random.randint(50,250)]

Pipes = []
Pipes.append(pipe1)
Pipes.append(pipe2)

def draw_pipe(PIPE):
    pygame.draw.rect(screen, (0, 255, 0), (PIPE[0], PIPE[1], PIPE[2], PIPE[3]))
    pygame.draw.rect(screen, (0, 255, 0), (PIPE[0], 200+ PIPE[3], PIPE[2], PIPE[3]+400))

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
sCord = (10,10)

def print_score(scr):
    screen.blit(font.render("Score: "+str(scr), True, (255,255,255)), sCord)

running = True
while running:
    screen.fill((120, 120, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump = False

    draw_circle(x, y)

    if jump:
        y -= 2
    else:
        y += speed

    for i in Pipes:
        draw_pipe(i)
        i[0] -= 0.5
        if i[0] <= 0:
            i[0] = 600
            i[3] = random.randint(50, 250)

    for i in Pipes:
        if i[0] == 200:
            if y <= i[3] or y >= 200+i[3]:
                print("GAME OVER")
                running = False
            else:
                score += 1
                print(score)


    print_score(score)
    pygame.display.update()
