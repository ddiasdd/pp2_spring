import pygame
from color_palette import *
from pygame.locals import *
import random,time,sys
pygame.init()

import psycopg2
#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "1223",
    port =5433
    )
#create a cursor to work with the database
cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute("""create table if not exists students_data(
            name varchar(255),
            score varchar(20)
        
);
""")
conn.commit()
# колем
san = 0
WIDTH = 600
HEIGHT = 600
SCORE = 0
CELL = 30
SAN = 1
bos =0
tiu = 0
# фон
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, colorBLACK)
leveling = font.render("next level",True,colorBLACK)
FPS = 7
clock = pygame.time.Clock()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False

        pygame.display.flip()
        clock.tick(15)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        

# онынды кайттан бастау
def reset_game():
    global snake, food, SCORE, bos,FPS
    snake = Snake()  # Пересоздаем змейку
    food = Food()    # Пересоздаем еду
    SCORE = 0   
    FPS =7
    bos =0
    print(FPS)
# экранды шахмат етип сызу
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))
# позиция
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
# жылан
class Snake:
    def __init__(self):
        global body
        # денеси
        self.body = [Point(9, 11), Point(9, 12), Point(9, 13)]
        self.dx = 0
        self.dy = -1
        self.stolknovenie = 0
        body = self.body[1:]
        self.walls = []
    # козгалыс
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    # тамакка тиуи
    def check_collision(self,food):
        global head
        global SCORE
        global tiu
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            global FPS
            SCORE += food.foods['score']
            self.stolknovenie+=1
            self.body.append(Point(head.x, head.y))
            food.update_position()
            if self.stolknovenie%2==0 and self.stolknovenie!=0:
                tiu +=1  
                global wals
                self.walls.append(walls()) 
                screen.blit(leveling,(150,150))
                FPS+=1.5
    def check_wall_collision(self):
        # Check if the snake's head hits any wall
        for wall in self.walls:
            if head.x == wall.pos.x and head.y == wall.pos.y:
                return True
            print("fes")
        return False
    def drawing(self):
        for wall in self.walls:
            wall.draw()

    # озине тимеуи
    def check(self):
        for segment in self.body[1:]:
            global bos
            if head.x == segment.x and head.y == segment.y:
                return True
            return False
# тамак
class Food():
    def __init__(self):

        self.pos=Point(random.randint(0,19),random.randint(0,19))
        self.timer = 10
        self.food_types = [
            {'color': colorYELLOW, 'score': 1},
            {'color': colorRED, 'score': 2},
            {'color': colorBLUE, 'score': 3}
        ]
        self.foods = random.choice(self.food_types)
    def update_position(self):
        while True:
            new_pos = Point(random.randint(0, 19), random.randint(0, 19))
            self.foods = random.choice(self.food_types)
            # Проверка на совпадение с позициями змеи
            collision = False
            for segment in snake.body:
                if new_pos.x == segment.x and new_pos.y == segment.y:
                    collision = True
                    break
            if not collision:
                self.pos = new_pos
                break
    def draw(self):
        pygame.draw.rect(screen, self.foods['color'],(self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    # уакыт азайуы
    def update_timer(self,dt):
        self.timer -= dt
        if self.timer<=0:
            self.update_position()
            self.timer = 10
class walls():
    def __init__(self):
         self.pos=Point(random.randint(0,19),random.randint(0,19))
    def update_position(self):
        while True:
            new_pos = Point(random.randint(0, 19), random.randint(0, 19))
            self.foods = random.choice(self.food_types)
            # Проверка на совпадение с позициями змеи
            collision = False
            for segment in snake.body:
                if new_pos.x == segment.x and new_pos.y == segment.y:
                    collision = True
                    break
            if not collision:
                self.pos = new_pos
                break
    def draw(self):
        pygame.draw.rect(screen,colorGREEN,(self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
def get_player_name():
    return input("Please enter your name: ")
player_name = get_player_name()
wals = walls()
snake = Snake()
food = Food()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if bos<1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()  
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
        if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    reset_game() 
    scores = font_small.render(str(SCORE), True, colorBLACK)
    level = font_small.render(str(tiu),True,colorBLACK)
    draw_grid_chess()

    snake.move()
    if snake.check_wall_collision():
        screen.fill(colorRED)
        screen.blit(game_over, (150, 150))
        pygame.display.flip()
        bos+=1
    snake.check_collision(food)
    snake.drawing()
    snake.draw()
    food.draw()
    dt = clock.tick(FPS)/1000
    food.update_timer(dt)
    # озине тисе
    if snake.check():
        screen.fill(colorRED)
        screen.blit(game_over,(150,150))
        bos+=1
        pygame.display.flip()
    
    # экраннан шыгып кетсе       
    if head.x < 0 or head.y<0 or head.x>19 or head.y>19:
        screen.fill(colorRED)
        screen.blit(game_over,(150,150))
        bos+=1
        pygame.display.flip() 
    if tiu>san:
        
        san = tiu
        
    screen.blit(scores, (10,10))
    screen.blit(level,(570,10))
    pygame.display.update()
#create new students
cur.execute(f"""insert into students_data (name, score) VALUES
            ('{player_name}','{SCORE}')
""")
conn.commit()
cur.execute(f"""update students_data
            set score = {SCORE}
            where name= '{player_name}'
""")
conn.commit()
pygame.quit()
sys.exit()