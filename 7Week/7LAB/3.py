
import pygame

pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)

size = width, height = (1100, 680)

screen = pygame.display.set_mode(size)


pygame.display.set_caption('PyGAME 7 LABS 3 Project')

clock = pygame.time.Clock()

color = WHITE

x = 100
y = 100
dx = 1
dy = 1

speed = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP or y > 650:
            dx = 0
            dy = -1 * speed
            y += dy
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 1 * speed
            y += dy
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -1 * speed
            dy = 0
            x += dx
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = 1 * speed
            dy = 0
            x += dx
        if x >= 1075:
            x = 1075
        if x <= 25:
            x = 25
        if y <= 25:
            y =25
        if y >= 680:
            y = 680


    screen.fill(WHITE)
    
    pygame.draw.circle(screen, RED, (x, y), 25)
    clock.tick(30)
    pygame.display.update()