'''
Docstring for Main
This file was writed by our sweat and blood
it contains all the information for our functions and runs these functions
'''
#Всякие импорты
import pygame
from plitki import *
from func import *
from ballandplatform import *

#Здесь всякие штуки, которые нужны для pygame и кода в целом
clock = pygame.time.Clock()
score = 0
t = 0
FPS = 30
screen = pygame.display.set_mode((1280, 800))
finished = False

#Создание плиток, шарика, платформы
create_pl() #Это работает!
platform, ball = start(screen, clock) #Здесь создаются платформа и шарик(всё нормально, они в классах)

#Запуск главного экрана

#Начало игры(Большая надпись "Начало", затем мячик появляется на верхней части платформы и летит вертикально вверх, но с небольшим углом)

#1) проверка, что еще остались плитки 2) изменение параметров шарика, платформы и плиток 3) отрисовка объектов
while finished == False:
    if score < 78:
        screen.fill('BLACK')
        mouse_button = pygame.mouse.get_pressed()
        if mouse_button[0]:
            platform.move_left(window_x = WINDOW_X)
        if mouse_button[2]:
            platform.move_right()
        #неактивный мяч - на платформе + обновление координат активного мяча
        if mouse_button[1]:
            ball.activate(platform.rect)
        
        if not ball.active:
            ball.rect.midbottom = platform.rect.midtop
        ball.update(platform)
        #инактивация мяча в случае вылета за нижнюю границу
        if ball.rect.top > WINDOW_Y + WINDOW_HEIGHT:
            ball.active = False
            
            
        #clock.tick(FPS)
        for PLI in Plitka.vse_plitki: #Проверяем на столкновение
            #Цикл проверяет, не столкнулись ли шарик и плитка. Если столкнулись, он добавляет очко к общему счёту, а еще функция уничтожает эту плитку
            score_change = 0
            if destroy(PLI, ball) == True:
                score_change = 1
            score += score_change
        for PLI in Plitka.vse_plitki: #Обновляем экран. Эта функция
            place_pl(screen, PLI)
        platform.draw(screen)
        ball.draw(screen)
        #ball.draw(screen)
        pygame.display.update()
            #FIXME: здесь должна быть функция, рисующая шарик
        for event in pygame.event.get(): #Проверяем, не нажали ли на крестик справа сверху
            if event.type == pygame.QUIT:
                finished = True
        clock.tick(30)
#Здесь будет финальный экран с затраченным временем 1