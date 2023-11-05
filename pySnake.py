#PySnake - Antonio Di Maria 2023
#this is a simple project i did use to learn pygame 
#Tested on python 3.9 with pygame 2.5
import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        #x and y pos
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

    #draw fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*CELL_SIZE), int(self.pos.y*CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)
        
#init pygame
pygame.init()

#globals 
FPS_CAP = 60

#RGB touples
BACKGROUND_COLOR = (175,215,70)
SURFACE_COLOR = (0,0,255)
FRUIT_COLOR = (126,166,144)

#virtual grid
CELL_SIZE = 40
CELL_NUMBER = 20

#OBJECTS Positions
surface_pos_x = 200
surface_pos_y = 250

#create screen and surace
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))

#create a clock to limit game speed to FPS_CAP
clock = pygame.time.Clock()

#game objects
fruit = FRUIT()

#game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(FPS_CAP)