#Всякие импорты
import pygame
from Plitki_Matvey import *
from Functions import *

#Здесь всякие штуки, которые нужны для pygame и кода
score = 0
FPS = 30
screen = pygame.display.set_mode((1280, 800))
finished = False

#Запуск главного экрана

#Начало игры(Большая надпись "Начало", затем мячик появляется на верхней части платформы и летит вертикально вверх, но с небольшим углом)

#Здесь будет обновление данных для каждого кадра(1. проверка на столкновение 2. рисуются все объекты)
#while not finished:
    
    
    
#Здесь будет проверка того, что еще остались плитки
while score < 78:
    #clock.tick(FPS)
    for PLI in vse_plitki: #Проверяем на столкновение
        #Цикл проверяет, не столкнулись ли шарик и плитка. Если столкнулись, он добавляет очко к общему счёту, а еще функция уничтожает эту плитку
        score_change = destroy(PLI, Ball) #FIXME: Ball
        score += score_change
    for PLI in vse_plitki: #Обновляем экран
        place_plitku(screen, PLI)
        #FIXME: здесь должна быть функция, рисующая шарик
    for event in pygame.event.get(): #Проверяем, не нажали ли на крестик справа сверху
        if event.type == pygame.QUIT:
            finished = True
#Здесь будет финальный экран с затраченным временем 1