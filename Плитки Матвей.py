import pygame
from pygame import *


#FIXME: Это убрать потом
FPS = 30
screen = pygame.display.set_mode((1280, 800))
#^^
class Plitka:
    """Класс, содержащий плитки/кирпичики, которые уничтожаются, когда в них попадает шарик
    Содержит положение плитки(x, y - центр плитки), размер плитки(l - длина, d - ширина), цвет плитки, статус жизни(уничтожена или нет), ряд и столбец плитки"""
    
    x = 0
    
    y = 0
    
    l = 0
    
    d = 0
    
    ryad = 0
    
    stolb = 0
    
    color = ' '
    
    zhizn = True

#Здесь функция, которая задает всем плиткам положение и цвет

pl = 0
vse_plitki = []

#FIXME: это убрать(это в мейне будет)
finished = False
while not finished:
    #clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


def unique_plitka(Plitka):
    """Функция, которая присваивает каждой плитке номер ряда и столбца, цвет, координаты, размер"""
    pl = 0
    for i in range (78):
        pl = Plitka()
        vse_plitki.append(pl)
    i = 0
    j = 0
    for plit in vse_plitki:
        #
        plit.stolb = i
        plit.ryad = j
        i += 1
        if i > 11:
            i = 0
            j += 1
        #plit.color = 
        plit.x = 