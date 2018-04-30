import pygame

def daylight(time):
    '''Takes an input of military time e.g. 800 = 8am, 1400 = 2pm
    and uses that number to select a blue value that varies between
    0 (midnight) and 255 (noon). Returns a RGB tuple.'''
    blue_value = 255 * (1200 - abs(time - 1200)) // 1200
    return (0, 0, blue_value)
    
screen = pygame.display.set_mode((640, 480))

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    screen.fill(daylight(500))
    pygame.display.flip()
