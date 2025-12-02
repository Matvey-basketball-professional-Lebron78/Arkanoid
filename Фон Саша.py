import pygame
from pygame.draw import *
import sys
import os

pygame.init()

#collors 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211) 

class gif:
    def __init__(self, path, *args, **kwargs):

        # self.IMAGES = {filename: pygame.image.load(os.path.join('images', path, filename)) for fil/name in os.listdir('images') }
        self.IMAGES = [
            pygame.image.load(os.path.join('images', path, f'{i}.png'))
            for i in range(len(os.listdir(os.path.join('images', path))))
        ]
        self.currimage = 0

    def blit(self, screen, pos):
        self.currimage = (self.currimage + 1)  % (3 * len(self.IMAGES))
        screen.blit(self.IMAGES[self.currimage//3], pos)

BG = gif('background')

# screen.blit(IMAGES['one'], (0,0))


#window 
screen = pygame.display.set_mode((1280, 800))
FPS=30
clock = pygame.time.Clock()
pygame.display.update()
running = True

#background
# screen.fill((BLACK))

rect(screen,GRAY, (0, 0, 1280, 800), 8 )
#gamewindow
rect(screen,GRAY, (47, 50, 843, 700), 5 )
#score_Number
digit_data = {
    0: {'file': 'zero.png', 'pos': (100, 50)},
    1: {'file': 'one.png', 'pos': (100, 50)},
    2: {'file': 'two.png', 'pos': (80, 80)}, 
    3: {'file': 'three.png', 'pos': (100, 50)},
    4: {'file': 'four.png', 'pos': (100, 50)},
    5: {'file': 'five.png', 'pos': (100, 50)},
    6: {'file': 'six.png', 'pos': (100, 50)},
    7: {'file': 'seven.png', 'pos': (100, 50)},
    8: {'file': 'eight.png', 'pos': (100, 50)},
    9: {'file': 'nine.png', 'pos': (100, 50)}
}
#HS
rect(screen,BLUE, (920, 160, 320, 180), 2 )
#S
rect(screen,BLUE, (920, 240, 320, 60), 2 )
while running:
    BG.blit(screen, (0,0))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    
    pygame.display.flip()
    
#end program
pygame.quit()
sys.exit()