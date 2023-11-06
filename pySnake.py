#PySnake - Antonio Di Maria 2023
#this is a simple project i did use to learn pygame 
#Tested on python 3.9 with pygame 2.5
#Crdit to Clear Code tutorial on https://www.youtube.com/watch?v=QFvqStqPCRU

import pygame, sys, random
from pygame.math import Vector2

#init pygame
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

#timers 
FPS_CAP = 60
GAME_SPEED = 200 #timer in milliseconds
SCREEN_UPDATE = pygame.USEREVENT

#RGB touples
WALL_COLOR = (77,13,0)
BACKGROUND_COLOR = (0,34,51)
GRASS_COLOR = (0,77,64)
FRUIT_COLOR = (56,199,15)
SNAKE_COLOR = (150,123,0)
SCORE_COLOR = (250,0,0)
SCORE_BG = (90,90,90)
SCORE_FRAME = (0,0,0)

#virtual grid
CELL_SIZE = 20
CELL_NUMBER = 30

#fonts
FONT_SIZE = 28
score_font = pygame.font.Font('SourceAssets/SevenSegment.ttf', FONT_SIZE)

class FRUIT:
    def __init__(self):
        #Load PNG Assets
        self.food = pygame.image.load('Graphics/food.png').convert_alpha()
        #Randomize fruit position
        self.randomize()
    #draw fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*CELL_SIZE,
                                 self.pos.y*CELL_SIZE,
                                 CELL_SIZE, 
                                 CELL_SIZE)
        #pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)
        screen.blit(self.food, fruit_rect)
    def randomize(self):
        self.x = random.randint(1, CELL_NUMBER-2)
        self.y = random.randint(1, CELL_NUMBER-2)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        #Load PNG Assets
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_l.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_r.png').convert_alpha()
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_l.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_r.png').convert_alpha()
        #Load Sound Assets
        self.crunch_sound = pygame.mixer.Sound('Sound/eating.mp3')
        #starting position
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0) #right
        self.new_block = False
    def draw_snake(self):
        for index,block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * CELL_SIZE,
                                     block.y * CELL_SIZE,
                                     CELL_SIZE,
                                     CELL_SIZE)
            if index == 0: #head
                #calculate head direction
                direction = self.body[1] - self.body[0]
                #dwaw correct asset
                if direction == Vector2(1,0): screen.blit(self.head_left,block_rect)
                elif direction == Vector2(-1,0): screen.blit(self.head_right,block_rect)
                elif direction == Vector2(0,1): screen.blit(self.head_up,block_rect)
                elif direction == Vector2(0,-1): screen.blit(self.head_down,block_rect)
            elif index == len(self.body) -1: #tail
                #calculate tail direction
                direction = self.body[len(self.body) -2] - self.body[len(self.body) -1]
                #dwaw correct asset
                if direction == Vector2(1,0): screen.blit(self.tail_left,block_rect)
                elif direction == Vector2(-1,0): screen.blit(self.tail_right,block_rect)
                elif direction == Vector2(0,1): screen.blit(self.tail_up,block_rect)
                elif direction == Vector2(0,-1): screen.blit(self.tail_down,block_rect)
            else:   
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
    def play_crunch_sound (self):
        self.crunch_sound.play()
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0) #right
        self.new_block = False
        pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED - len(self.body)) 

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def increase_speed(self):
        pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED - len(self.snake.body)) 
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    def check_collision(self):
        # snake got the fruit
        if self.fruit.pos == self.snake.body[0]:
            self.snake.play_crunch_sound()
            self.fruit.randomize()
            self.snake.add_block()
            self.increase_speed()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        # control borders
        if not 1 <= self.snake.body[0].x < CELL_NUMBER+1:
            self.game_over()   
        elif not 1 <= self.snake.body[0].y < CELL_NUMBER+1:  
            self.game_over()   
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()   
    def draw_grass(sef):
        for row in range(1,CELL_NUMBER+1):     
            if row % 2 == 0:
                for col in range(1,CELL_NUMBER+1):
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    if col % 2 == 0:
                        pygame.draw.rect(screen, GRASS_COLOR, grass_rect)
                    else:
                        pygame.draw.rect(screen, BACKGROUND_COLOR, grass_rect)
            else:
                for col in range(1,CELL_NUMBER+1):
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    if col % 2 == 1:
                        pygame.draw.rect(screen, GRASS_COLOR, grass_rect)
                    else:
                        pygame.draw.rect(screen, BACKGROUND_COLOR, grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body) -3)
        score_surface = score_font.render(score_text,True,SCORE_COLOR)
        score_x = int(CELL_SIZE * CELL_NUMBER -60)
        score_y = int(CELL_SIZE * CELL_NUMBER -40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        bg_rect = pygame.Rect(score_rect.left -6 , score_rect.top -6 , score_rect.width +12, score_rect.height +12)
        pygame.draw.rect(screen, SCORE_BG, bg_rect)
        screen.blit(score_surface, score_rect)
        pygame.draw.rect(screen, SCORE_FRAME, bg_rect, 2)
    
    def game_over(self):
        if (len(self.snake.body) > 3):
            print ("Score: " + str(len(self.snake.body) -3))
        self.snake.reset()

#create screen and surace
screen = pygame.display.set_mode((CELL_SIZE*(CELL_NUMBER+2), CELL_SIZE*(CELL_NUMBER+2)))

#create a clock to limit game speed to FPS_CAP
clock = pygame.time.Clock()
pygame.time.set_timer(SCREEN_UPDATE, GAME_SPEED) 

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

    screen.fill(WALL_COLOR)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FPS_CAP)