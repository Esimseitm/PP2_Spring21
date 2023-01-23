from datetime import datetime
import pygame
#активация всех модулей pygame
pygame.init()
#окно с разрешением "1280х960"
screen=pygame.display.set_mode((1280,960))
#время сейчас
a=datetime.now()
#маус
image=pygame.image.load("mickey.jpg")
#руки
llhand=pygame.image.load("llhand.png")
rrhand=pygame.image.load("rrhand.png")


#левая рука
def left_hand(surf, image, topleft, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)
#правая рука
def right_hand(surf, image, topleft, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)
#формулы нахождения позиции рук мауса
anglel=(51-a.second)*6
print(a.second)
angleh=(10-a.minute)*6
print(a.minute)
#координаты центра вращения стрелок
x=0
y=0
running = True
#для проверки условия вращения секундной стрелки
n=a.second
while running:
    #присвоил еще одной переменной метод "время сейчас",чтобы выполнялось условие b.second !=n во время вращения секундной стрелки
    b=datetime.now()
    # белый фон RGB 
    screen.fill((255,255,255))
    #вставил изображения мауса в окно
    screen.blit(image,(0,0))
    
    
    
    
    
    #при нажатии на крестик ,окно сворачивается и программа останавливает работу
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    #вызов функции левой и правой руки
    left_hand(screen, llhand, [x,y], anglel)
    right_hand(screen,rrhand,[x,y],angleh)
    #обновление окна 
    pygame.display.update()  
    #увеличиваем угол вращения стрелок
    
    if b.second>=0 and b.second !=n:
        n=b.second
        anglel-=6

    if b.second==0:
        angleh-=0.35
    print(b.second)