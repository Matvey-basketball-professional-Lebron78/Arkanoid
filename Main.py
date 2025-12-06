'''
Docstring for Main
This file was writed by our sweat and blood
it contains all the information for our functions and runs these functions
'''
#Всякие импорты
import pygame
from Plitki import *
from func import *
from ballandplatform import *
#Здесь всякие штуки, которые нужны для pygame и кода
clock = pygame.time.Clock()
score = 0
FPS = 30
screen = pygame.display.set_mode((1280, 800))
finished = False

#Запуск главного экрана

#Начало игры(Большая надпись "Начало", затем мячик появляется на верхней части платформы и летит вертикально вверх, но с небольшим углом)

#Здесь будет обновление данных для каждого кадра(1. проверка на столкновение 2. рисуются все объекты)
t = 0
create_pl() #Это работает!
platform, ball = start(screen, clock) #Здесь создаются платформа и шарик(всё нормально, они в классах)
print(10)
#Здесь будет проверка того, что еще остались плитки
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
            
            score_change = destroy(PLI, ball) #FIXME: Ball
            print(1)
            '''score += score_change'''
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
        clock.tick(60)
#Здесь будет финальный экран с затраченным временем 1