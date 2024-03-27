import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_red = True

red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)


x = 30
y = 30
# image = pygame.image.load("/Users/apple/Desktop/pp2_spring/test2/pygame/image/ball.jpg").convert()
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        print(event)
        if(event.type == pygame.QUIT):
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
            
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x +=1
    if keys[pygame.K_LEFT]:
        x -=1
    if keys[pygame.K_UP]:
        y -=1
    if keys[pygame.K_DOWN]:
        y +=1

screen.fill((white))
pygame.draw.rect(screen,red,pygame.rect(x,y,100,60))
    # screen.blit(image,(x,y))
pygame.display.flip()
clock.tick(60)