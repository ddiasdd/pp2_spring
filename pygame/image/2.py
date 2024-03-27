import pygame
import os
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
image = pygame.image.load("ball.png")
_image_library =  dict()
def load_image(path):
    image = _image_library.get(path)
    global _image_library
    if image is None:
        canonicalized_path = path.replace('/',os.sep()).replace('\\',os.sep())
        image = pygame.image.load(path)
        _image_library[path] = image
        return image
    return image
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
    screen.blit(load_image(""),(x,y))
    pygame.display.flip()
    clock.tick(60)
