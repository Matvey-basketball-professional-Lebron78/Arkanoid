# ============================================================================
# DEBUG_MAIN.PY - ВЕРСИЯ С ОТЛАДКОЙ
# ============================================================================
# Здесь мы выведем все координаты и проверим что творится

import pygame
import sys

from ballandplatform import Platform, Ball, start, WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT
from Plitki import Plitka, create_pl, place_pl
from func import destroy
from Score_Background import load_background, load_digit_images, draw_score

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (100, 100, 100)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Арканоид - Полная версия (ОТЛАДКА)")
clock = pygame.time.Clock()

print("=" * 80)
print("ОТЛАДКА - проверяем координаты")
print("=" * 80)

# ============================================================================
# КОНСТАНТЫ
# ============================================================================
print(f"\nКонстанты игрового поля:")
print(f"  WINDOW_X = {WINDOW_X}")
print(f"  WINDOW_Y = {WINDOW_Y}")
print(f"  WINDOW_WIDTH = {WINDOW_WIDTH}")
print(f"  WINDOW_HEIGHT = {WINDOW_HEIGHT}")
print(f"  Нижняя граница поля Y: {WINDOW_Y + WINDOW_HEIGHT}")

# ============================================================================
# СОЗДАНИЕ ПЛИТОК
# ============================================================================
print(f"\nСоздание плиток...")
create_pl()

print(f"Всего плиток: {len(Plitka.vse_plitki)}")

if len(Plitka.vse_plitki) > 0:
    print(f"\nПервая плитка:")
    p = Plitka.vse_plitki[0]
    print(f"  X = {p.x}, Y = {p.y}")
    print(f"  Ширина = {p.l}, Высота = {p.d}")
    print(f"  Левый край = {p.x - p.l/2}, Правый край = {p.x + p.l/2}")
    print(f"  Верхний край = {p.y - p.d/2}, Нижний край = {p.y + p.d/2}")
    print(f"  Цвет = {p.color}, Живая = {p.zhizn}")
    
    print(f"\nПоследняя плитка:")
    p = Plitka.vse_plitki[-1]
    print(f"  X = {p.x}, Y = {p.y}")
    print(f"  Левый край = {p.x - p.l/2}, Правый край = {p.x + p.l/2}")
    print(f"  Верхний край = {p.y - p.d/2}, Нижний край = {p.y + p.d/2}")
    print(f"  Цвет = {p.color}, Живая = {p.zhizn}")

# ============================================================================
# ЗАГРУЗКА ФОНА
# ============================================================================
background = load_background('images/background/-1.png')
digit_images = load_digit_images("images/digits", 80, 80)

# ============================================================================
# СОЗДАНИЕ ПЛАТФОРМЫ И МЯЧА
# ============================================================================
print(f"\nСоздание платформы и мяча...")
platform, ball = start(screen, clock)

print(f"\nПлатформа:")
print(f"  X = {platform.rect.x}, Y = {platform.rect.y}")
print(f"  Ширина = {platform.rect.width}, Высота = {platform.rect.height}")
print(f"  Центр X = {platform.rect.centerx}, Центр Y = {platform.rect.centery}")
print(f"  Левый край = {platform.rect.left}, Правый край = {platform.rect.right}")
print(f"  Верхний край = {platform.rect.top}, Нижний край = {platform.rect.bottom}")

print(f"\nМяч:")
print(f"  X = {ball.rect.x}, Y = {ball.rect.y}")
print(f"  Ширина = {ball.rect.width}, Высота = {ball.rect.height}")
print(f"  Центр X = {ball.rect.centerx}, Центр Y = {ball.rect.centery}")
print(f"  Радиус = {ball.radius}")
print(f"  Активен = {ball.active}")

# ============================================================================
# ПЕРЕМЕННЫЕ ИГРЫ
# ============================================================================
current_score = 0
display_x = 920
display_y = 157
digit_spacing = 0
num_digits = 4
finished = False
FPS = 30

print("\n" + "=" * 80)
print("РЕЖИМ ОТЛАДКИ - видишь ли объекты?")
print("=" * 80)
print(f"Белый прямоугольник = граница игрового поля")
print(f"Серые прямоугольники = плитки")
print(f"Синий прямоугольник = платформа")
print(f"Красный круг = мяч")
print("\nНажми левую/правую кнопку мыши для движения платформы")
print("=" * 80 + "\n")

# ============================================================================
# ГЛАВНЫЙ ЦИКЛ ОТЛАДКИ
# ============================================================================

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    if current_score < 78:
        # ОЧИСТКА И ФОН
        screen.blit(background, (0, 0))
        
        # РИСУЕМ ГРАНИЦУ ИГРОВОГО ПОЛЯ (белый прямоугольник)
        pygame.draw.rect(screen, WHITE, 
                        (WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT), 
                        2)
        
        # РИСУЕМ ВСЕ ПЛИТКИ
        for plitka in Plitka.vse_plitki:
            place_pl(screen, plitka)
        
        # РИСУЕМ ПЛАТФОРМУ
        platform.draw(screen)
        
        # РИСУЕМ МЯЧ
        ball.draw(screen)
        
        # РИСУЕМ СЧЕТ
        draw_score(screen, current_score, digit_images, 
                   display_x, display_y, digit_spacing, num_digits)
        
        # УПРАВЛЕНИЕ
        mouse_button = pygame.mouse.get_pressed()
        
        if mouse_button[0]:
            platform.move_left(window_x=WINDOW_X)
        
        if mouse_button[2]:
            platform.move_right()
        
        if mouse_button[1]:
            ball.activate(platform.rect)
        
        if not ball.active:
            ball.rect.midbottom = platform.rect.midtop
        
        ball.update(platform)
        
        if ball.rect.top > WINDOW_Y + WINDOW_HEIGHT:
            ball.active = False
        
        # ПРОВЕРКА СТОЛКНОВЕНИЙ
        for plitka in Plitka.vse_plitki:
            if destroy(plitka, ball):
                current_score += 1
    
    else:
        screen.blit(background, (0, 0))
        font = pygame.font.SysFont(None, 100)
        text = font.render("ПОБЕДА!", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        
        font_small = pygame.font.SysFont(None, 60)
        score_text = font_small.render(f"Счет: {current_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(score_text, score_rect)
    
    pygame.display.update()
    clock.tick(FPS)

print("=" * 80)
print("Спасибо за игру! Финальный счет:", current_score)
print("=" * 80)

pygame.quit()
sys.exit()
