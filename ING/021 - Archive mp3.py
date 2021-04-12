#Play an mp3 file.

import pygame

pygame.mixer.init()

pygame.mixer.music.load('nts.mp3')

pygame.mixer.music.play()

while(pygame.mixer.music.get_busy()): pass