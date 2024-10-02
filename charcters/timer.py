












































import pygame
from time import *
from pygame.locals import *
import time

pygame.init()
WIDTH = 1500
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
start = pygame.image.load("images/start.png")
start = pygame.transform.scale(start,(1200,300))
clock = pygame.image.load("images/time.png")
clock = pygame.transform.scale(clock,(500,200))
c_time = 60

while True:
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Times New Roman",100)
    start_1 = font.render("start",True,(0,0,0))
    c_time_surface = font.render(str(c_time), True, (255, 255, 255))
    screen.blit(start,(200,100))
    screen.blit(clock,(500,400))
    timer = font.render("c_time",True,(0,0,0))
    screen.blit(c_time_surface,(650,420))
    font = pygame.font.SysFont("Times New Roman",200)
    screen.blit(timer,(700,170))
 
    for i in range(60):
        c_time = c_time - 1
        
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit(0)  


    pygame.display.update()



