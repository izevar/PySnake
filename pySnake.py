#PySnake - Antonio Di Maria 2023
#this is a simple project i did use to learn pygame 
#Tested on python 3.9 with pygame 2.5
import pygame, sys, random
from pygame.math import Vector2

#init pygame
pygame.init()

#timers 
FPS_CAP = 60
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #timer in milliseconds

#RGB touples
BACKGROUND_COLOR = (175,215,70)
SURFACE_COLOR = (0,0,255)
FRUIT_COLOR = (56,199,15)
SNAKE_COLOR = (203,111,111)

#virtual grid
CELL_SIZE = 40
CELL_NUMBER = 20

class FRUIT:
    def __init__(self):
        #x and y pos
        self.randomize()
    #draw fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*CELL_SIZE,
                                 self.pos.y*CELL_SIZE,
                                 CELL_SIZE, 
                                 CELL_SIZE)
        pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        #starting position
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0) #right
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * CELL_SIZE,
                                     block.y * CELL_SIZE,
                                     CELL_SIZE,
                                     CELL_SIZE)
            pygame.draw.rect(screen, SNAKE_COLOR, block_rect)
    def move_snake(self):
        #create a copy of the snake, discard the last block.
        #add a new blok at the beginning of the list in the directon of movement
        if self.new_block == True:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
    def add_block(self):
        self.new_block = True

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        # snake got the fruit
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    def check_fail(self):
        # control borders
        if not 0 <= self.snake.body[0].x < CELL_NUMBER:
            self.game_over()   
        elif not 0 <= self.snake.body[0].y < CELL_NUMBER:  
            self.game_over()   
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()        

#create screen and surace
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))

#create a clock to limit game speed to FPS_CAP
clock = pygame.time.Clock()

main_game = MAIN()

#game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1) #up
            elif event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1) #down
            elif event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0) #left
            elif event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:    
                    main_game.snake.direction = Vector2(1,0) #right

    screen.fill(BACKGROUND_COLOR)
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(FPS_CAP)