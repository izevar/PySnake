#PySnake - Antonio Di Maria 2023
#this is a simple project i did use to learn pygame 
#Tested on python 3.9 with pygame 2.5
import pygame
import sys

DISPLAY_SIZE_X = 400
DISPLAY_SIZE_Y = 500
FPS_CAP = 60

#init pygame
pygame.init()

#create display survace
scree = pygame.display.set_mode((DISPLAY_SIZE_X,DISPLAY_SIZE_Y))
#create a clock to limit game speed to FPS_CAP

clock = pygame.time.Clock()

#game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS_CAP)