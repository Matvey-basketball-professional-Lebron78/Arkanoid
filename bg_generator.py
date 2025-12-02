import pygame
import os

screen = pygame.display.set_mode((1280, 800))


c = pygame.color.Color(123,23,15)
print(c.hsla)
N = 360
step = 360 // N
for i in range(0, 360, step):
    c.hsla = (i, 50, 50, 100)
    screen.fill(c)
    pygame.image.save(screen, os.path.join('images', 'background',f'{i//step}.png'))
    
