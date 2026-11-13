import numpy as np
import pygame
import time
import sys



sample_rate = 44100
duracao=0.5
pygame.mixer.pre_init(channels=1, allowedchanges=0)
pygame.init()

pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)

la4=440
si4=493.8833
do4=523.2511
re4=587.3295

def collect_input():
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()         
            if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
              return event.key 
        
        return "0"

def play_tone(frequency, duration=0.5, volume=0.5):
  
  t = np.linspace(0, duration, int(sample_rate * duration), False)
  # Onda senoidal com envelope simples (fade-out)
  wave = np.sin(2 * np.pi * frequency * t) * np.exp(-3 * t)
  audio = (wave * (2.15**15 - 1) * volume).astype(np.int16)
  sound = pygame.sndarray.make_sound(audio)
  sound.play()
  time.sleep(duration)


# Toca uma nota Lá (A4 = 440 Hz)
while 1: 
 #tecla = input("Digite a nota desejada: ") 
 #print(chr(ord(tecla)+2))
 #if pygame.key.get_pressed():
 #for event in pygame.event.get():
  #  if event.type == pygame.KEYDOWN:
  keys = collect_input()
  print(keys)
  if keys!="0":
    print(keys)
    play_tone(la4, duration=duracao)


