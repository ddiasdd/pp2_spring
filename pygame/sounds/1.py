import pygame
pygame.init()
done = False
is_red = True
sound = pygame.mixer.Sound("/Users/apple/Desktop/pp2_spring/test2/pygame/sounds/muz.mp3")
sound.play()
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    is_red = False
while is_red:
    continue

pygame.mixer.music.stop()