import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import time

duracao=3
sample_rate = 44100

la4=440
si4=493.8833
do4=523.2511
re4=587.3295

def play_tone(frequency, duration=0.5, volume=0.5):  
  t = np.linspace(0, duration, int(sample_rate * duration), True)
  wave = np.sin(2 * np.pi * frequency * t) * np.exp(-3 * t)
  audio = (wave * (2.15**15 - 1) * volume).astype(np.int16)
  sound = pygame.sndarray.make_sound(audio)
  sound.play()
  return sound
  #time.sleep(duration)

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
    if event.type == TEXTINPUT :        
        if event.text == K_LEFT:  
            move_x = -0.3  # object moves -0.3 towards x axis
            play_tone(re4, duration=duracao)
            print("pressed LEFT")
        elif event.text == "a":  
            move_x = +0.3  # object moves 0.3 towards x axis
            sound=play_tone(la4, duration=duracao)
            print(ord(event.text ))
        elif event.text == K_UP: 
            move_y = -0.3  # object moves -0.3 towards y axis
            print("pressed UP")
        elif event.text == K_DOWN: 
            move_y = +0.3  # object moves 0.3 towards y axis
            print("pressed DOWN")
        elif event.text == K_LCTRL:
            img = pygame.image.load("char1.png")
            pygame.display.update()  # update image
        elif event.text == K_BACKSPACE:
            img = pygame.image.load("char.png")
            pygame.display.update()  # update image
    if event.type == KEYUP:
        if event.key == K_LEFT:
            move_x = 0  # movement stops
        elif event.key == K_RIGHT:  
            move_x = 0  # movement stops
        elif event.key == K_a:  
            move_x = 0  # movement stops
            pygame.mixer.stop()
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
