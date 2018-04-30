import pygame

width = int(input("width? "))
height = int(input("height? "))

screen = pygame.display.set_mode((width, height))

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    screen.fill((255, 255, 255))
    pygame.display.flip()
