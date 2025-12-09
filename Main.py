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
from Score_Background import load_background

#Здесь всякие штуки, которые нужны для pygame и кода в целом
clock = pygame.time.Clock()
score = 0
t = 0
FPS = 30
screen = pygame.display.set_mode((1280, 800))
finished = False
font = pygame.font.SysFont('impact', 80, bold=False)
font_big = pygame.font.SysFont('arial', 72, bold=True)
score_title = font.render('SCORE:', True, (255, 255, 255))

#Создание плиток, шарика, платформы
create_pl() #Это работает!
platform, ball = start(screen, clock) #Здесь создаются платформа и шарик(всё нормально, они в классах)

#Запуск вступительного экрана
knopka_x, knopka_y, knopka_len, knopka_wid = 340, 400, 600, 200
start_txt = font_big.render('START', True, (0, 0, 0))
txt_rect  = start_txt.get_rect(center=(knopka_x + knopka_len//2, knopka_y + knopka_wid//2))
mainmenu = True
while mainmenu == True:
    screen.fill('BLACK')
    pygame.draw.rect(screen, (255, 255, 255), (knopka_x, knopka_y, knopka_len, knopka_wid))
    screen.blit(start_txt, txt_rect)
    mouse_button = pygame.mouse.get_pressed()
    clock.tick(50)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            if knopka_x <= mx <= knopka_x + knopka_len and knopka_y <= my <= knopka_y + knopka_wid:
                mainmenu = False
#Начало игры(Большая надпись "Начало", затем мячик появляется на верхней части платформы и летит вертикально вверх, но с небольшим углом)
clock.tick(5)
#1) проверка, что еще остались плитки 2) изменение параметров шарика, платформы и плиток 3) отрисовка объектов
while finished == False and score < 78:
    screen.fill('BLACK')
    screen.blit(score_title, (920, 50))
    pygame.draw.rect(screen, (255, 255, 255), (47, 50, 816, 695), 5)
    #screen.blit(background, (0, 0))
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
    score_value = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_value, (920, 150))
    pygame.display.update()
    
    for event in pygame.event.get(): #Проверяем, не нажали ли на крестик справа сверху
        if event.type == pygame.QUIT:
            finished = True
    clock.tick(50)
        
#УРА ПОБЕДА
clock.tick(10)
screen.fill('BLACK')
ura_pobeda = font.render('УРА-УРА ПОЗДРАВЛЯЕМ!!', True, (255, 255, 255))
uraura_pobeda  = ura_pobeda.get_rect(center=(640, 400))
screen.blit(ura_pobeda, uraura_pobeda)
pygame.display.update()
clock.tick(0.5)
pygame.quit()