import sys
import pygame
import pygame_textinput

textinput = pygame_textinput.TextInput()

def check_events(set,scr):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    events = pygame.event.get()
    textinput.update(events)
    scr.blit(textinput.get_surface(),(10,10))
    pygame.display.update()
