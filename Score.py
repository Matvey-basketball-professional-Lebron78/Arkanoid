import pygame
import sys
import os

pygame.init()

# Настройки
WIDTH, HEIGHT = 240, 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def load_digit_images(folder="digits", width=80, height=80):
    """Загружает все цифры из папки"""
    images = {}
    print(f"Загружаю цифры из папки: {folder}")
    print(f"Текущая директория: {os.getcwd()}")
    print(f"Содержимое папки '{folder}':")
    
    # Проверяем, существует ли папка
    if os.path.exists(folder):
        files = os.listdir(folder)
        print(files)
    else:
        print(f"Папка '{folder}' не найдена!")
    
    for i in range(10):
        file_path = os.path.join(folder, f"{i}.png")
        print(f"Пробую загрузить: {file_path}")
        
        if os.path.exists(file_path):
            try:
                img = pygame.image.load(file_path)
                # Измените width и height на реальный размер ваших картинок
                images[str(i)] = pygame.transform.scale(img, (width, height))
                print(f"✓ Загружена цифра {i}")
            except Exception as e:
                print(f"✗ Ошибка загрузки {i}.png: {e}")
                # Создаем простую заглушку
                surf = pygame.Surface((width, height))
                surf.fill((50, 50, 50))
                font = pygame.font.SysFont(None, 80)
                text = font.render(str(i), True, (255, 255, 255))
                text_rect = text.get_rect(center=(width//2, height//2))
                surf.blit(text, text_rect)
                images[str(i)] = surf
        else:
            print(f"✗ Файл {i}.png не найден")
            # Создаем простую заглушку
            surf = pygame.Surface((width, height))
            surf.fill((50, 50, 50))
            font = pygame.font.SysFont(None, 80)
            text = font.render(str(i), True, (255, 255, 255))
            text_rect = text.get_rect(center=(width//2, height//2))
            surf.blit(text, text_rect)
            images[str(i)] = surf
    
    print(f"Загружено {len(images)} цифр")
    return images

def draw_score(surface, score, images, x, y, spacing=5, digits=6):
    """Рисует счет на указанных координатах"""
    if not images:
        print("Нет изображений цифр для отображения!")
        return
    
    score_str = str(score).zfill(digits)
    
    # Используем первую цифру для определения ширины
    if "0" in images:
        digit_width = images["0"].get_width()
    elif images:
        # Берем первую доступную цифру
        first_key = list(images.keys())[0]
        digit_width = images[first_key].get_width()
    else:
        digit_width = 80  # Значение по умолчанию
    
    for i, digit in enumerate(score_str):
        if digit in images:
            img = images[digit]
            x_pos = x + i * (digit_width + spacing)
            surface.blit(img, (x_pos, y))
        else:
            print(f"Нет изображения для цифры: {digit}")


folder_name = folder_name = "images\digits"
digit_width = 80
digit_height = 80
display_x = 0
display_y = 0 
digit_spacing = 0
num_digits = 3

# Загрузка изображений
digit_images = load_digit_images(folder_name, digit_width, digit_height)

# Начальные значения
current_score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    # Отрисовка
    screen.fill((0, 0, 0))
    
    # Рисуем счет
    draw_score(screen, current_score, digit_images, 
               display_x, display_y, digit_spacing, num_digits)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()