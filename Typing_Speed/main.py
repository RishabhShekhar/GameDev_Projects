import pygame, random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TYPING SPEED CALCULATOR")
text_font = pygame.font.Font("freesansbold.ttf", 20)

statements = [
    "Please take your dog, Cali, out for a walk – he really needs some exercise!",
    "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
    "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
    "Do you know why all those chemicals are so hazardous to the environment?",
    "You never did tell me how many copper pennies where in that jar; how come?",
    "Max Joykner sneakily drove his car around every corner looking for his dog.",
    "The two boys collected twigs outside, for over an hour, in the freezing cold!",
    "When do you think they will get back from their adventure in Cairo, Egypt?",
    "Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.",
    "We climbed to the top of the mountain in just under two hours; isn’t that great?",
]

statements = random.choice(statements)
inp = ''
enter = 0
start = 0

MainRun = True
while MainRun:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(50, 100, 900,40), 3)
    sentence = text_font.render(statements, True, (255, 255, 255))
    screen.blit(sentence,(60,110))

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50, 200, 900, 40), 3)
    if start == 0:
        inp_sentence = text_font.render("(PRESS 1 TO START)", True, (120,120,120))
    else:
        inp_sentence = text_font.render(inp, True, (255, 255, 255))

    screen.blit(inp_sentence,(60, 210))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                start = 1
                start_time = pygame.time.get_ticks()
            elif event.key == pygame.K_RETURN:
                enter = 1
                end_time = pygame.time.get_ticks()
            elif event.key == pygame.K_BACKSPACE:
                inp = inp[:-1]
            else:
                inp += event.unicode

    if enter = 1:
        Accuracy_msg =
    print(inp)
    pygame.display.update()