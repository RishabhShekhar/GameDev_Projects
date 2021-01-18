import pygame
import random
import sys

pygame.init()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("PING PONG")

ball = pygame.Rect(sw//2-15, sh//2-15, 30, 30)
player = pygame.Rect(sw-20, sh//2-60, 10, 30)
opponent = pygame.Rect(10, sh//2-60, 10, 30)

bg_color = pygame.Color('grey12')

ball_speed_x = 6
ball_speed_y = 6

player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold', 32)

pong_sound = pygame.mixer.Sound('sound/pong.ogg')
score_sound = pygame.mixer.Sound('sound/score.ogg')

running = True





