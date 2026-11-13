import numpy as np
import pygame
import time

sample_rate = 44100
duracao=0.5
pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)

la4=440
si4=493.8833
do4=523.2511
re4=587.3295

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
 play_tone(la4, duration=duracao)
 play_tone(si4, duration=duracao)
 play_tone(do4, duration=duracao)
 play_tone(re4, duration=duracao)
 play_tone(la4, duration=duracao)
