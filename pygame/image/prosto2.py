import pygame
import sys
 
FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
# радиус будущего круга
r = 30
# координаты круга
# скрываем за левой границей
x = r
# выравнивание по центру по вертикали
y = WIN_HEIGHT // 2
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x +=1
    if keys[pygame.K_LEFT]:
        x -=1
    if keys[pygame.K_UP]:
        y -=1
    if keys[pygame.K_DOWN]:
        y +=1
 
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE, (x, y), r)
    # обновляем окно
    pygame.display.update()
    if x == WIN_WIDTH or x==WIN_HEIGHT:
        # перемещаем его за левую
        x = (WIN_WIDTH,WIN_HEIGHT//2)
        y = WIN_HEIGHT