import pygame
from pygame.draw import *
def place_pl(screen, Plitka):
    """Функция, рисующая плитки.
    Принимает на вход координаты плитки, размеры плитки, цвет плитки, статус жизни плитки"""
    
    x = Plitka.x
    y = Plitka.y
    l = Plitka.l
    d = Plitka.d
    color = Plitka.color
    zhizn = Plitka.zhizn
    if zhizn == True:
        rect(screen, color, (x - l/2, y - d/2, l, d))
        rect(screen, 'WHITE', (x - l/2, y - d/2, l, d), 1)

def destroy(Plitka, Ball): #FIXME: Ball
    """Функция, определяющая, столкнулся ли шарик с какой-либо плиткой
    Принимает на вход координаты определённой плитки и координаты шарика в данный момент
    Если шарик задевает плитку, статус плитки меняется на 'разрушена', шарик отбивается от плитки и летит в другую сторону"""
    if Plitka.zhizn == True:
        #Ищем ближайшую к шарику точку на плитке
        closest_x = max(Plitka.x - Plitka.l/2, min(Ball.x, Plitka.x + Plitka.l/2))
        closest_y = max(Plitka.y - Plitka.d/2, min(Ball.y, Plitka.y + Plitka.d/2))
        
        if  (closest_x - Ball.x)^2 + (closest_y - Ball.y)^2 <= Ball.r:
            Plitka.zhizn = False
            return 1
            #FIXME: добавить увеличение количества очков после столкновения
            
            #FIXME: добавить смену направления движения шарика после столкновения 
        else:
            return 0
        
