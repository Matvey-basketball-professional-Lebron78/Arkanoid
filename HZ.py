import pygame

def draw_game(screen, score_value, bg_file="background/-1.png", score_x=950, score_y=165):
    """
    Объединяет отрисовку фона и счета.
    
    Параметры:
    - screen: поверхность PyGame
    - score_value: текущий счет для отображения
    - bg_file: файл фона (по умолчанию "-1.png")
    - score_x, score_y: координаты счета
    """
    
    # Импортируем здесь, чтобы не было циклических импортов

    from Background import draw_background
    from Score import draw_score
    
    # 1. Рисуем фон
    draw_background(screen, bg_file)
    
    # 2. Рисуем счет
    draw_score(screen, score_value, score_x, score_y)