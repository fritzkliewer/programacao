import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import time

duracao=1
sample_rate = 44100

notas = {
    "la4": 440,
    "la#4":466.1638,
    "si4": 493.8833,
    "do5": 523.2511,
    "do#5":554.3653,
    "re5": 587.3295
    }

teclas={
    "a":"la4",
    "A":"la#4",
    "s":"si4",
    "d":"do5",
    "D":"do#5",
    "f":"re5"

}

print(notas["la4"])


pygame.mixer.pre_init(channels=1, allowedchanges=0)
pygame.init()
size = width, height = 740, 480
screen = pygame.display.set_mode(size)
img = pygame.image.load("char.png").convert()
x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sound=0
    if event.type == KEYDOWN :   
        if event.key == K_LEFT:  
            move_x = -0.3  # object moves -0.3 towards x axis
            print("pressed LEFT")
        elif event.key == K_RIGHT:  
            move_x = +0.3  # object moves 0.3 towards x axis
        elif event.key == K_UP: 
            move_y = -0.3  # object moves -0.3 towards y axis
            print("pressed UP")
        elif event.key == K_DOWN: 
            move_y = +0.3  # object moves 0.3 towards y axis
            print("pressed DOWN")
        elif event.key == K_LCTRL:
            img = pygame.image.load("char1.png")
            pygame.display.update()  # update image
        elif event.key == K_BACKSPACE:
            img = pygame.image.load("char.png")
            pygame.display.update()  # update image
    if event.type == KEYUP:
        pygame.mixer.stop()
        if event.key == K_LEFT:
            move_x = 0  # movement stops
        elif event.key == K_RIGHT:  
            move_x = 0  # movement stops
        elif event.key == K_a:  
            move_x = 0  # movement stops
            
        elif event.key == K_UP: 
            move_y = 0  # movement stops
        elif event.key == K_DOWN:  
            move_y = 0  # movement stops
            """KEYUP event will be triggered when the release the keys 
            and x,y coordinates will not change anymore"""

    x += move_x
    y += move_y
    screen.fill((255, 255, 255))
    screen.blit(img, (x, y))
    pygame.display.update()
