'''
Docstring for Plitki
This file was writed by matvey goddamn LEBRON denisov (aka Matvey Denisov B06-506)
it contains class plitki and some functions for it
'''

import pygame
from pygame.draw import *
from func import *

COLORS = ['GREY','RED','BLUE','ORANGE','PINK','GREEN']
#FIXME: Это убрать потом
FPS = 30
screen = pygame.display.set_mode((1280, 800))
#^^

"""def place_plitku(screen, Plitka):
    
    x = Plitka.x
    y = Plitka.y
    l = Plitka.l
    d = Plitka.d
    color = Plitka.color
    zhizn = Plitka.zhizn
    if zhizn == True:
        rect(screen, color, (x - l/2, y - d/2, l, d))
        rect(screen, 'WHITE', (x - l/2, y - d/2, l, d), 1)"""

class Plitka:
    """Класс, содержащий плитки/кирпичики, которые уничтожаются, когда в них попадает шарик
    Содержит положение плитки(x, y - центр плитки), размер плитки(l - длина, d - ширина), цвет плитки, статус жизни(уничтожена или нет), ряд и столбец плитки"""
    
    x = 0
    
    y = 0
    
    l = 62
    
    d = 26
    
    ryad = 0
    
    stolb = 0
    
    color = 'GREY'
    
    zhizn = True
    

#Здесь функция, которая задает всем плиткам положение и цвет


vse_plitki = []


for i in range (78):
    """Создаем 78 плиток (13 * 6)"""
    pl = Plitka()
    vse_plitki.append(pl)
i = 0
j = 0

for plit in vse_plitki:
    """Каждой плитке присваиваем координаты и цвет"""
    #Каждой плитке присваивается номер ряда и столбца
    plit.stolb = i
    plit.ryad = j
    #Каждой плитке присваиваются координаты
    plit.x = 86 + plit.l * i 
    plit.y = 73 + plit.d * j
    #Каждой плитке присваивается цвет
    plit.color = COLORS[j]
    i += 1
    if i > 12:
        i = 0
        j += 1
    place_pl(screen, plit)
    pygame.display.update()
    
#FIXME: это убрать(это в мейне будет)

finished = False
print(1)
while not finished:
    #clock.tick(FPS)
    for PLI in vse_plitki:
        place_pl(screen, PLI)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

