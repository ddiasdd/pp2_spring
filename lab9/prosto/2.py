import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
is_red = (255,0,0)
x = 400
y = 300
radius = 25
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen,is_red,pygame.Rect(20,20,100,100))
    pygame.draw.rect(screen,(255,255,120),pygame.Rect(10,10,100,100))
    pygame.display.flip()
    clock.tick(20)
