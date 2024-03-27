import pygame
pygame.init()
done = False
black = (0,0,0)
screen = pygame.display.set_mode((800, 600))
sound = pygame.mixer.Sound("/Users/apple/Desktop/pp2_spring/test2/pygame/sounds/muz.mp3")
sound2 = pygame.mixer.Sound("/Users/apple/Desktop/pp2_spring/test2/pygame/sounds/muz2.mp3")


while not done:
    for event in pygame.event.get():
        print(event)
        if(event.type == pygame.QUIT):
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sound.play()
    if keys[pygame.K_LEFT]:
        sound.stop()
    if keys[pygame.K_UP]:
        sound2.play
    if keys[pygame.K_DOWN]:
     sound.play()
screen.fill((black))
pygame.display.flip()
