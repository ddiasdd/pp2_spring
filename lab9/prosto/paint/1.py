import pygame
import sys
import math
pygame.init()
#экран бетінің көлмі
WIDTH = 960
HEIGHT = 640
# керек түстер
colorBlack = (0,0,0)
colorWhite = (255,255,255)
colorRed = (255,0,0)
colorGreen = (0,255,0)
colorBlue = (0 ,0,255)
colorYellow = (255,255,0)
# төртбұрыш экран аштық
screen = pygame.display.set_mode((WIDTH,HEIGHT))
base_layer = pygame.Surface((WIDTH,HEIGHT))
done = False
lastik = False
LMBpressed = False
rectangle = False
circle = False
square = False
triangle = False
diamond = False
equal_triangle = False
romb = False
color = colorWhite
prevx = 0
prevy = 0
currx = 0
curry = 0
# төртбұрыш нүктелері
def calculate_rect(x1,y1,x2,y2):
    return pygame.Rect(min(x1,x2),min(y1,y2),abs(x1-x2),abs(y1-y2))
# дөңгелек радиус
def calculate_circle(x1,y1,x2,y2):
     radius =  int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
     return radius
# өшіргіш
def calculate_lastik(x1,y1,x2,y2):
      return pygame.Rect(min(x1,x2),min(y1,y2),abs(x1-x2),abs(y1-y2))
# квадрат
def calculate_square(x1, y1, x2, y2):
    size = max(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(min(x1,x2),min(y1,y2), size, size)
# тікбұрышты үшбұрыш
def calculate_right_triangle(x1,y1,x2,y2):
    sol_zhak = [x1,y1]
    on_zhak = [x2,y2]
    asty = [x1,y2]
    points = [sol_zhak,on_zhak,asty]
    return points
# дұрыс үшбұрыш
def calculate_equilateral_triangle(x1,y1,x2,y2):
    sol_zhak = [x1,y1]
    on_zhak = [x1-(x2-x1),y1+(x2-x1)*math.sqrt(3)]
    asty = [x2,y1+(x2-x1)*math.sqrt(3),]
    points = [sol_zhak,on_zhak,asty]
    return points
# ромб
def calculate_romb(x1, y1, x2, y2):
    sol_zhak = [x1,y1]
    on_zhak = [x2,y2]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    diagonal = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 2
    asty = [x -diagonal, y]
    en_asty = [x + diagonal, y]
    points = [sol_zhak, asty, on_zhak, en_asty]
    return points
# главный
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # мышканың алғашқы нүктесі
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevx = event.pos[0]
            prevy = event.pos[1]
        # мышканың соңғы нүктесі
        if LMBpressed:
                currx = event.pos[0]
                curry = event.pos[1]
        if event.type == pygame.KEYDOWN:
            # ластик
            if event.key == pygame.K_e:
                lastik = True
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # тортбурыш
            if event.key == pygame.K_r:
                rectangle = True
                lastik = False
                circle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # донгелек
            if event.key == pygame.K_c:
                circle = True
                lastik = False
                rectangle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # квадрат
            if event.key == pygame.K_s:
                square = True
                lastik = False
                rectangle = False
                circle = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # ушбурыш
            if event.key == pygame.K_t:
                triangle = True
                lastik = False
                rectangle = False
                circle = False
                square = False
                diamond = False
                equal_triangle = False
                romb = False
            # тен ушбырыш
            if event.key == pygame.K_u:
                equal_triangle=True
                lastik = False
                LMBpressed = False
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                romb = False
            # ромб
            if event.key ==pygame.K_1:
                romb= True
                lastik = False
                LMBpressed = False
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
            if event.key==pygame.K_b:
                color = colorBlack
            if event.key==pygame.K_y:
                color = colorYellow
            if event.key==pygame.K_q:
                color=colorRed
            if event.key==pygame.K_g:
                color = colorGreen
        # мышканы жібергенде
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if lastik:
                pygame.draw.rect(screen,colorBlack,calculate_lastik(prevx,prevy,currx,curry))
            if rectangle:
                pygame.draw.rect(screen,color,calculate_rect(prevx,prevy,currx,curry),2)
            if circle:
                radius = calculate_circle(prevx,prevy,currx,curry)
                pygame.draw.circle(screen,color,(prevx,prevy),radius,2)
            if square:
                pygame.draw.rect(screen,color,calculate_square(prevx,prevy,currx,curry),2)
            base_layer.blit(screen,(0,0))
            if triangle:
                points = calculate_right_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
            if equal_triangle:
                points = calculate_equilateral_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
            if romb:
                points = calculate_romb(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
            
    if LMBpressed:
        
        screen.blit(base_layer,(0,0))
        if lastik:
            pygame.draw.rect(screen,colorYellow,calculate_lastik(prevx,prevy,currx,curry),2)
        if rectangle:
            pygame.draw.rect(screen,color,calculate_rect(prevx,prevy,currx,curry),2)
        if circle:
            radius = calculate_circle(prevx,prevy,currx,curry)
            pygame.draw.circle(screen,color,(prevx,prevy),radius,2)
        if square:
            pygame.draw.rect(screen,color,calculate_square(prevx,prevy,currx,curry),2)
        if triangle:
                points = calculate_right_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
        if equal_triangle:
                points = calculate_equilateral_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
        if romb:
                points = calculate_romb(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
    pygame.display.flip()