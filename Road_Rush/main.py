import pygame

pygame.init()

screen_width = 640
screen_height = 480
half_screen_height = screen_height//2
screen = pygame.display.set_mode((screen_width, screen_height))

light_road = pygame.image.load("imgs/light_road.png")
dark_road = pygame.image.load("imgs/dark_road.png")

texture_position = 0

ddz = 0.001
dz = 0
z = 0

road_pos = 0
road_acceleration = 80
texture_position_acceleration = 4
texture_position_threshold = 300
half_texture_position_threshold = texture_position_threshold//2

while True:
    pygame.time.Clock().tick(30)
    screen.fill((0, 0, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        road_pos += road_acceleration
        if road_pos >= texture_position_threshold:
            road_pos = 0

    elif keys[pygame.K_DOWN]:
        road_pos -= road_acceleration
        if road_pos <= 0:
            road_pos = texture_position_threshold


    texture_position = road_pos
    dz = 0
    z = 0

    for i in range(half_screen_height-1,-1,-1):
        if texture_position < half_texture_position_threshold:
            screen.blit(light_road, (0, i+half_screen_height), (0, i, screen_width, 1))
        else:
            screen.blit(dark_road, (0, i + half_screen_height), (0, i, screen_width, 1))

        dz += ddz
        z += dz

        texture_position += texture_position_acceleration + z
        if texture_position >= texture_position_threshold:
            texture_position = 0

    pygame.display.update()
