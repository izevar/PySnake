#PySnake - Antonio Di Maria 2023
#this is a simple project i did use to learn pygame 
#Tested on python 3.9 with pygame 2.5
import pygame
import sys

DISPLAY_SIZE_X = 400
DISPLAY_SIZE_Y = 500
SURFACE_SIZE_X = 100
SURFACE_SIZE_Y = 200
FPS_CAP = 60

#RGB touples
BACKGROUND_COLOR = (175,215,70)
SURFACE_COLOR = (0,0,255)

#OBJECTS Positions
surface_pos_x = 200
surface_pos_y = 250

#init pygame
pygame.init()

#create screen and surace
screen = pygame.display.set_mode((DISPLAY_SIZE_X, DISPLAY_SIZE_Y))

#create a clock to limit game speed to FPS_CAP
clock = pygame.time.Clock()

#game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    pygame.display.update()
    clock.tick(FPS_CAP)