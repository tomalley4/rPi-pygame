import pygame

pygame.init()

def daylight(time):
    '''Takes an input of military time e.g. 800 = 8am, 1400 = 2pm
    and uses that number to select a blue value that varies between
    0 (midnight) and 255 (noon). Returns a RGB tuple.'''
    blue_value = 255 * (1200 - abs(time - 1200)) // 1200
    return (0, 0, blue_value)
    
screen = pygame.display.set_mode((640, 480))

def get_rect_color():
    # TODO: instead of always returning red, make this function check the status
    # of the rpi's switch and return blue if the switch has been pressed
    return (255, 0, 0)

while True:
    event = pygame.event.poll()
    blat = 'afjweoiawefjoiaefw'
    if event.type == pygame.QUIT:
        break
    screen.fill(daylight(500))

    pygame.draw.rect(screen, get_rect_color(), (50, 50, 100, 100))

    pygame.display.flip()
