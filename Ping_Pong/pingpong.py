import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("PING PONG")
bg_color = pygame.Color('grey12')
game_font = pygame.font.Font('freesansbold.ttf', 60)

level = 1
opponent = 6

screen_time = None

def Start_Game(05):
    pass

WelcomeScreen = True
while WelcomeScreen:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WelcomeScreen = False

        if event.type == pygame.K_DOWN:
            if event.key == pygame.K_SPACE:
                WelcomeScreen = False
                Start_Game(opponent_speed)
            if event.key == pygame.K_1:
                opponent_speed = 6
                level = 1
            if event.key == pygame.K_2:
                opponent_speed = 10
                level = 2
            if event.key == pygame.K_3:
                opponent_speed = 15
                level = 3

    if level == 1:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(sw // 2 - 190, sh - 410, 350, 70), 2)
    if level == 2:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(sw // 2 - 190, sh - 310, 350, 70), 2)
    if level == 3:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(sw // 2 - 190, sh - 210, 350, 70), 2)

    Welcome_Message = game_font.render("PING PONG", True, (200, 200, 200))
    screen.blit(Welcome_Message, (sw // 2 - 170, 20))

    Select_level = game_font.render("Select_level", True, (200, 200, 200))
    screen.blit(Select_level, (sw // 2 - 200, sh - 500))

    Easy = game_font.render("Easy", True, (200, 200, 200))
    screen.blit(Easy, (sw // 2 - 90, sh - 400))

    Medium = game_font.render("Medium", True, (200, 200, 200))
    screen.blit(Medium, (sw // 2 - 130, sh - 300))

    Hard = game_font.render("Hard", True, (200, 200, 200))
    screen.blit(Hard, (sw // 2 - 90, sh - 200))

    Start = game_font.render("PRESS SPACE TO START", True, (200, 200, 200))
    screen.blit(Start, (sw // 2 - 360, sh - 100))

    clock.tick(60)
    pygame.display.update()
