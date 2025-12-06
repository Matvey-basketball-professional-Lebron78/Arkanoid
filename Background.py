
import pygame
import sys

# Инициализация PyGame
pygame.init()

# Установка размеров окна (1280x800)
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Отображение картинки")

# Загрузка картинки из папки background
try:
    # Если картинка в папке background
    image = pygame.image.load('images/background/-1.png')
    # Если картинка в той же папке, что и код
    # image = pygame.image.load('-1.png')
except FileNotFoundError:
    print("Ошибка: файл -1.png не найден в папке background!")
    print("Проверьте правильность пути к файлу.")
    sys.exit()

# Преобразование изображения для лучшей производительности
image = image.convert()

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Очистка экрана
    screen.fill((0, 0, 0))
    
    # Отображение картинки на весь экран
    # Автоматическое масштабирование под размер окна
    scaled_image = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(scaled_image, (0, 0))
    
    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
sys.exit()