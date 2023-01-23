import pygame

pygame.init()
pygame.display.set_caption('7 LAB SECOND PROJECT - MP3')
songs = ['song_1.mp3' , 'song_2.mp3', 'song_3.mp3']
screen = pygame.display.set_mode((400, 400))
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
max = len(songs) - 1
print(max)
playing_song = None
i = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            i += 1
            print(i)
            if i > max:
                i = 0
            pygame.mixer.music.load(songs[i])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            i -= 1
            if i < 0:
                i = max
            pygame.mixer.music.load(songs[i])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pygame.mixer.music.unpause()
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
