import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import time

duracao=1
sample_rate = 44100

notasW = {
    "A": {"oitava":4,"freq":440},
    "B": {"oitava":4,"freq":493.8833},
    "C": {"oitava":5,"freq":523.2511},
    "D": {"oitava":5,"freq":587.3295}
    }

notasB = {
    "A#": {"oitava":4,"freq":466.1638},
    "C#": {"oitava":5,"freq":554.3653},
}

teclas={
    "a":"A",
    "A":"A#",
    "s":"B",
    "d":"C",
    "D":"C#",
    "f":"D"
}

def load_img(name):
    fullname = name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print("Error: couldn't load image: ", fullname)
        raise SystemExit(message)
    return (image, image.get_rect())

def play_tone(nota,notadados, duration=0.5, volume=0.5):  
  octave_offset = (notadados["oitava"]- LOWEST) * width
  if nota in WHITE_KEYS:
    w = WHITE_KEYS.index(nota) * white_key_width
    w = w + octave_offset
    playing_w.append([w, tick, nota])
  else:
    i = BLACK_KEYS.index(nota)
    if i == 0:
        w = 18
    elif i == 1:
        w = 58
    elif i == 2:
        w = 115
    elif i == 3:
        w = 151
    else:
        w = 187
    w = w + octave_offset
    playing_b.append([w, tick, nota])
    
  notes = playing_w + playing_b
  notes.sort()
  notenames = []
  for n in notes:
    notenames.append(n[2])

  t = np.linspace(0, duration, int(sample_rate * duration), True)
  wave = np.sin(2 * np.pi * notadados["freq"]* t) * np.exp(-3 * t)
  audio = (wave * (2.15**15 - 1) * volume).astype(np.int16)
  sound = pygame.sndarray.make_sound(audio)
  sound.play()
  return sound
  #time.sleep(duration)

OCTAVES = 5  # number of octaves to show
LOWEST = 2  # lowest octave to show
FADEOUT = 0.25  # coloration fadeout time (1 tick = 0.001)
WHITE_KEY = 0
BLACK_KEY = 1
WHITE_KEYS = ["C","D","E","F","G","A","B",]
BLACK_KEYS = ["C#", "D#", "F#", "G#", "A#"]


pygame.mixer.pre_init(channels=1, allowedchanges=0)
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("monospace", 12)

x, y = 0, 0
move_x, move_y = 0, 0

screen = pygame.display.set_mode((640, 480))
(key_graphic, kgrect) = load_img("keys.png")
(width, height) = (kgrect.width, kgrect.height)
white_key_width = width / 7
pygame.display.set_mode((OCTAVES * width, height + 20))
pygame.display.set_caption("mingus piano")
octave = 4
channel = 8
pressed = pygame.Surface((white_key_width, height))
pressed.fill((0, 230, 0))
text = pygame.Surface((width * OCTAVES, 20))
text.fill((255, 255, 255))
playing_w = []  # white keys being played right now
playing_b = []  # black keys being played right now
quit = False
tick = 0.0

while True:
    for x in range(OCTAVES):
        screen.blit(key_graphic, (x * width, 0))
    for note in playing_w:
      diff = tick - note[1]
      if diff > FADEOUT:
          playing_w.remove(note)
      else:
         pressed.fill((0, ((FADEOUT - diff) / FADEOUT) * 255, 124))
         screen.blit(pressed, (note[0], 0), None, pygame.BLEND_SUB)
    for note in playing_b:
        diff = tick - note[1]
        if diff > FADEOUT:
            playing_b.remove(note)
        else:
            pressed.fill((((FADEOUT - diff) / FADEOUT) * 125, 0, 125))
            screen.blit(pressed, (note[0], 1), (0, 0, 19, 68), pygame.BLEND_ADD)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sound=0
    if event.type == TEXTINPUT :   
        if event.text in teclas:
         nota=teclas[event.text]
         notadados=0
         if nota in notasW:
             notadados=notasW[nota]
         elif nota in notasB:
             notadados=notasB[nota]
         if notadados!=0:
          sound=play_tone(nota,notadados ,duration=duracao)     
    if event.type == KEYUP:
        pygame.mixer.stop()
    pygame.display.update()
    tick += 0.001
