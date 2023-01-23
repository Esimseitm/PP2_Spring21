import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
osnova = 400, 400

clock = pygame.time.Clock()

Mickey = pygame.transform.scale(pygame.image.load('Main.png'), (1280*5//8, 1280*5//8))
Minhand = pygame.transform.scale(pygame.image.load('MinHand.png'), (770//2, 230//2))
Hour_Hand = pygame.transform.scale(pygame.image.load('hour.png'), (594//2, 322//2))

pygame.display.set_caption('7 LAB FIRST PROJECT - CLOCK')

def Rotate(serfaces, image, Coordinate, Position, angle):
    image11 = image.get_rect(topleft = (Coordinate[0]- Position[0], Coordinate[1] - Position[1]))
    rotated_1 = pygame.math.Vector2(Coordinate) - image11.center
    rotated_2 = rotated_1.rotate(angle)
    rotated_3 = (Coordinate[0] - rotated_2.x, Coordinate[1] - rotated_2.y)
    rotated_4 = pygame.transform.rotate(image, -angle)
    rotated_5 = rotated_4.get_rect(center = rotated_3)
    serfaces.blit(rotated_4, rotated_5)

done = False
while not done:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(Mickey, (0, 0))

    t = datetime.now()
    second = t.second
    minute = t.minute

    aa1 = minute + (second/60)
    alpha = aa1 * 6.0
    hh = Hour_Hand.get_width() / 2
    mm = Minhand.get_height() / 2
    Rotate(screen, Hour_Hand , osnova, (hh + 110, mm + 75), alpha + 75)
    alpha = second * 6.0
    Rotate(screen, Minhand, osnova, (hh - 145, mm), alpha - 87)

    pygame.display.flip()
    print(second)
pygame.quit()