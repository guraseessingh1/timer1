





















import pygame
from time import *
from pygame.locals import *

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
space = pygame.image.load("images/space.jpeg")
space = pygame.transform.scale(space,(WIDTH,HEIGHT))
player = pygame.image.load("images/ship.png")
player = pygame.transform.scale(player,(50,80))
player_x = 200
player_y = 200
keys = [False,False,False,False]

while player_y < HEIGHT :
    screen.blit(space,(0,0))

    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit(0)  

        #check if any keyboard is being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False

    if keys[0] == True:
        if player_y > 0:
            player_y -= 1
    elif keys[2] == True:
        if player_y < HEIGHT-80:
            player_y += 1
    elif keys[1] == True:
        if player_x > 0:
            player_x -= 1
    elif keys[3] == True:
        if player_x < WIDTH-80:
            player_x += 1