import pygame
from pygame.locals import *
from sys import exit
import numpy as np

duracao=0.5
sample_rate = 44100
oitavas = 5  
menoroitava = 2  
FADEOUT = duracao  
teclasbrancas = ["C","D","E","F","G","A","B",]
teclaspretas = ["C#", "D#", "F#", "G#", "A#"]

notasW = {
    "A": [{"info":{"oitava":3,"freq":220}},{"info":{"oitava":4,"freq":440}},{"info":{"oitava":5,"freq":880}}],
    "B": [{"info":{"oitava":3,"freq":246.9417}},{"info":{"oitava":4,"freq":493.8833}},{"info":{"oitava":5,"freq":987.7666}}],
    "C": [{"info":{"oitava":4,"freq":130.8128}},{"info":{"oitava":5,"freq":523.2511}},{"info":{"oitava":6,"freq":1108.73}}],
    "D": [{"info":{"oitava":4,"freq":146.8324}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":587.3295}}],
    "E": [{"info":{"oitava":4,"freq":164.8138}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":659.2551}}],
    "F": [{"info":{"oitava":4,"freq":174.6141}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":698.4565}}],
    "G": [{"info":{"oitava":4,"freq":195.9977}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":783.9909}}]
    }

res = next((sub for sub in notasW["A"] if sub['info']["oitava"] == 3), None)
print(res["info"]["freq"])

notasB = {
    "A#":[ {"info":{"oitava":3,"freq":233.0819}},{"info":{"oitava":4,"freq":466.1638}},{"info":{"oitava":5,"freq":932.3275}}],
    "C#":[ {"info":{"oitava":4,"freq":277.1826}},{"info":{"oitava":5,"freq":554.3653}},{"info":{"oitava":6,"freq":1108.731}}],
}

teclas={
    "g":{"nota":"A","oitava":4},
    "y":{"nota":"A#","oitava":4},
    "h":{"nota":"B","oitava":4},
    "j":{"nota":"C","oitava":5},
    "i":{"nota":"C#","oitava":5},
    "l":{"nota":"D","oitava":5}
}

def load_img(name):
    nome = name
    try:
        imagem = pygame.image.load(nome)
        if imagem.get_alpha() is None:
            imagem = imagem.convert()
        else:
            imagem = imagem.convert_alpha()
    except pygame.error as mensagem:
        print("Error: couldn't load imagem: ", nome)
        raise SystemExit(mensagem)
    return (imagem, imagem.get_rect())

def play_tone(oitava,nota,notadados, duracao=0.5, volume=0.5):  
  res = next((sub for sub in notadados if sub['info']["oitava"] == oitava), None)
  offsetoitava = (res["info"]["oitava"]- menoroitava) * width
  if nota in teclasbrancas:
    w = teclasbrancas.index(nota) * largteclabranca
    w = w + offsetoitava
    playing_w.append([w, tick, nota])
  else:
    i = teclaspretas.index(nota)
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
    w = w + offsetoitava
    playing_b.append([w, tick, nota])    
  notas = playing_w + playing_b
  notas.sort()
  notenames = []
  for n in notas:
    notenames.append(n[2])
  t = np.linspace(0, duracao, int(sample_rate * duracao), True)
  wave = np.sin(2 * np.pi * res["info"]["freq"]* t) * np.exp(-3 * t)
  audio = (wave * (2.15**15 - 1) * volume).astype(np.int16)
  sound = pygame.sndarray.make_sound(audio)
  sound.play()
  return sound

pygame.mixer.pre_init(channels=1, allowedchanges=0)
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("monospace", 12)
screen = pygame.display.set_mode((640, 480))
(key_graphic, kgrect) = load_img("keys.png")
(width, height) = (kgrect.width, kgrect.height)
largteclabranca = width / 7
pygame.display.set_mode((oitavas * width, height + 20))
pygame.display.set_caption("piano")
octave = 4
pressed = pygame.Surface((largteclabranca, height))
pressed.fill((0, 230, 0))
text = pygame.Surface((width * oitavas, 20))
text.fill((255, 255, 255))
playing_w = []  # white keys being played right now
playing_b = []  # black keys being played right now
quit = False
tick = 0.0

while True:
    for x in range(oitavas):
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
         nota=teclas[event.text]["nota"]
         notadados=0
         if nota in notasW:
             notadados=notasW[nota]
         elif nota in notasB:
             notadados=notasB[nota]
         if notadados!=0:
          sound=play_tone(teclas[event.text]["oitava"],nota,notadados ,duracao=duracao)     
    if event.type == KEYUP:
        pygame.mixer.stop()
    pygame.display.update()
    tick += 0.001
