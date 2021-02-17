import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
half_screen_height = screen_height // 2
screen = pygame.display.set_mode((screen_width, screen_height))

light_road = pygame.image.load("imgs/light_road.png")
dark_road = pygame.image.load("imgs/dark_road.png")
car = pygame.image.load("imgs/car.png")
truck = pygame.image.load("imgs/truck.png")
rock = pygame.image.load("imgs/rock.png")
health = pygame.image.load("imgs/health.png")

health_sound = pygame.mixer.Sound("sounds/health.wav")
rock_sound = pygame.mixer.Sound("sounds/rock.wav")

# GRADIENT
texture_position = 0
ddz = 0.001
dz = 0
z = 0

road_pos = 0 # Our Position on the road
road_acceleration = 80 # Speed at which road moves
texture_position_acceleration = 4
texture_position_threshold = 300
half_texture_position_threshold = texture_position_threshold // 2

car_x = 260
car_y = 360
stone_x = random.randint(250, 350)
stone_y = 240
health_x = random.randint(250, 350)
health_y = 240

state = 0

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
sCoord = (10, 10)


def score_print(scr):
    screen.blit(font.render("Score: " + str(scr), True, (0, 0, 0)), sCoord)


def isCollided(Cx, Cy, Sx, Sy):
    if Cx + 20 < Sx + 15 < Cx + 110 and Cy + 20 < Sy + 11 < Cy + 110:
        return True
    return False


def draw_lives(l):
    pygame.draw.rect(screen, (200, 0, 0), (600 - 30 * 4, 10, 30 * 5, 15))
    for i in range(l):
        pygame.draw.rect(screen, (0, 200, 0), (600 - 30 * i, 10, 30, 15))


life = 5
game = 1
start_time = pygame.time.get_ticks()
life_time = pygame.time.get_ticks()
health_piece = 0

running = True
while running:
    pygame.time.Clock().tick(30)
    screen.fill((0, 0, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # pygame.quit()

    keys = pygame.key.get_pressed()

    '''
    if keys[pygame.K_UP]:
        # print("UP")
        road_pos += road_acceleration #(80)
        if road_pos >= texture_position_threshold: #(300)
            road_pos = 0
    if keys[pygame.K_DOWN]:
        # print("DOWN")
        road_pos -= road_acceleration #(80)
        if road_pos <= 0: #(300)
            road_pos = texture_position_threshold
    '''

    if keys[pygame.K_RIGHT]:
        car_x += 5
        if car_x >= 450:
            car_x -= 5

    if keys[pygame.K_LEFT]:
        car_x -= 5
        if car_x <= 50:
            car_x += 5

    if life > 0:
        road_pos += road_acceleration
        if road_pos >= texture_position_threshold:
            road_pos = 0

    texture_position = road_pos
    dz = 0
    z = 0

    for i in range(half_screen_height - 1, -1, -1):
        if texture_position < half_texture_position_threshold:
            screen.blit(light_road, (0, i + half_screen_height), (0, i, screen_width, 1))
        else:
            screen.blit(dark_road, (0, i + half_screen_height), (0, i, screen_width, 1))

        dz += ddz
        z += dz

        texture_position += texture_position_acceleration + z
        if texture_position >= texture_position_threshold:
            texture_position = 0

    game_time = pygame.time.get_ticks()
    if game_time - start_time > 1000 and state == 0 and game == 1 and health_piece == 0:
        state = 1
        stone_x = random.randint(250, 350)
        stone_y = 240
        chng = 0

    if state == 1 and life > 0:
        stone_y += 5
        if stone_x < 270:
            chng = -4
        elif stone_x > 330:
            chng = 4
        stone_x += chng
        screen.blit(rock, (stone_x, stone_y))

        collided = isCollided(car_x, car_y, stone_x, stone_y)
        if state == 1 and collided:
            rock_sound.play()
            state = 0
            life -= 1
            start_time = pygame.time.get_ticks()
        if stone_y >= 480:
            score += 1
            state = 0
            start_time = pygame.time.get_ticks()

    game_life_time = pygame.time.get_ticks()
    if game_life_time - life_time > 10000 or health_piece == 1:
        health_piece = 1
        game = 0
        health_y += 5
        if health_x < 270:
            chng = -4
        elif health_y > 330:
            chng = 4
        health_x += chng
        screen.blit(health, (health_x, health_y))
        collided_health = isCollided(car_x, car_y, health_x, health_y)
        if collided_health:
            score += 2
            health_sound.play()
            health_piece = 0
            game = 1
            life += 1
            if life > 5:
                life = 5
            health_x = random.randint(250, 350)
            health_y = 240

        if health_y >= 480:
            game = 1
            health_y = 240
            health_x = random.randint(250, 350)

        life_time = pygame.time.get_ticks()

    screen.blit(car, (car_x, car_y))
    screen.blit(truck, (270, 210))

    score_print(score)
    draw_lives(life)
    pygame.display.update()