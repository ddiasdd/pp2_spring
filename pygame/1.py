import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_red = True

red = (255,0,0)
blue = (0,0,255)

x = 30
y = 20
while not done:
    for event in pygame.event.get():
        print(event)
        if(event.type == pygame.QUIT):
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
    if is_red:
        pygame.draw.rect(screen,red,pygame.Rect(30,30,100,60))
    else:
        pygame.draw.rect(screen,blue,pygame.Rect(30,30,100,60))
    pygame.display.flip()