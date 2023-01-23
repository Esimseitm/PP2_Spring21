import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400,300))

image_library = {}

def get_image(path):
    global image_library
    image = image_library.get(path)
    if image is None:
        _path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(_path)
        image_library = image
    return image 

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    screen.fill(get_image('ball.jpeg'), (0, 0, 0) , (20,20))
    pygame.display.flip()

pygame.quit()