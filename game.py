import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

py, sy = HEIGHT // 2, 0
player = pygame.Rect(WIDTH // 3, py, 50, 50)

state = 'start'
timer = 10

pipes = []

play = True
while play:
    just_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            just_clicked = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            just_clicked = True

    if timer > 0:
        timer -= 1

    for i in range(len(pipes) -1, -1, -1):
        pipe = pipes[i]
        pipe.x -= 3

        if pipe.right < 0:
            pipes.remove(pipe)

    if state == 'start':
        if just_clicked and timer == 0 and len(pipes) == 0:
            state = 'play'
            sy = -11

        py += (HEIGHT // 2 - py) * 0.1  
        player.y = py
    elif state == 'play':
        if just_clicked:
            sy = -11

        py += sy
        sy = (sy + 1) * 0.98
        player.y = py

        if len(pipes) == 0 or pipes[len(pipes)-1].x < WIDTH -200:
            pipes.append(pygame.Rect(WIDTH, 0, 50, 200))
            pipes.append(pygame.Rect(WIDTH, 400, 50, 200))

        if player.top < 0 or player.bottom > HEIGHT:
            state = 'fall'

        for pipe in pipes:
            if player.colliderect(pipe):
                state = 'fall'
    elif state == 'fall':
        sy = 0
        state = 'start'
        timer = 60
    else:
        pass

    window.fill(pygame.Color('black')) 
    for pipe in pipes:
        pygame.draw.rect(window, pygame.Color('green'), pipe)

    pygame.draw.rect(window, pygame.Color('yellow'), player)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()