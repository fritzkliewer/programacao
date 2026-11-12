import numpy
import pygame
import time

pygame.mixer.init(frequency=44100, size=-16, channels=1)


def play_tone(frequency, duration=0.5, volume=0.5):
  sample_rate = 44100
  t = numpy.linspace(0, duration, int(sample_rate * duration), False)
  # Onda senoidal com envelope simples (fade-out)
  wave = numpy.sin(2 * np.pi * frequency * t) * np.exp(-3 * t)
  audio = (wave * (2.15**15 - 1) * volume).astype(np.int16)
  sound = pygame.sndarray.make_sound(audio)
  sound.play()
  time.sleep(duration)


# Toca uma nota Lá (A4 = 440 Hz)
play_tone(440, duration=1.0)
