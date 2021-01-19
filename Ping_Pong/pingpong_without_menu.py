import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("PING PONG")

ball = pygame.Rect(sw//2-15, sh//2-15, 30, 30)
player = pygame.Rect(sw-20, sh//2-60, 10, 120)
opponent = pygame.Rect(10, sh//2-60, 10, 120)

bg_color = pygame.Color('grey12')

ball_speed_x = 6*random.choice(((-1,1)))
ball_speed_y = 6*random.choice(((-1,1)))

player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

pong_sound = pygame.mixer.Sound('sound/pong.ogg')
score_sound = pygame.mixer.Sound('sound/score.ogg')

score_time = None

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time, sh, sw

    ball.center = (sw//2, sh//2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        ball_speed_x = 0
        ball_speed_y = 0
        number_three = game_font.render("3", False, (200,200,200))
        screen.blit(number_three, (sw//2-8, sh//2+50))

    elif current_time - score_time < 1400:
        ball_speed_x = 0
        ball_speed_y = 0
        number_two = game_font.render("2", False, (200,200,200))
        screen.blit(number_two, (sw//2-8, sh//2+50))

    elif current_time - score_time < 2100:
        ball_speed_x = 0
        ball_speed_y = 0
        number_one = game_font.render("1", False, (200, 200, 200))
        screen.blit(number_one, (sw // 2 - 8, sh // 2 + 50))
    else:
        ball_speed_x = 6 * random.choice(((-1, 1)))
        ball_speed_y = 6 * random.choice(((-1, 1)))
        score_time = None


running = True
while running:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -=7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= sh:
        pong_sound.play()
        ball_speed_y *= -1
        
    if ball.left <= 0:
        score_sound.play()
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= sw:
        score_sound.play()
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        pong_sound.play()
        ball_speed_x *= -1

    if score_time:
        ball_restart()

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= sh:
        player.bottom = sh

    if opponent.bottom < ball.y:
        opponent.bottom += opponent_speed
    if opponent.top > ball.y:
        opponent.top -= opponent_speed

    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opponent)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.aaline(screen, (200, 200, 200), (sw//2, 0), (sw//2, sh))

    player_text = game_font.render(str(player_score), True, (200, 200, 200))
    screen.blit(player_text, (sw//2+20, sh//2-16))

    opponent_text = game_font.render(str(opponent_score), True, (200, 200, 200))
    screen.blit(opponent_text, (sw//2-42, sh // 2 - 16))

    pygame.display.update()
    clock.tick(60)






