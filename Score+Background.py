import pygame
import sys
import os

pygame.init()

screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Арканоид - Фон и Счет")
clock = pygame.time.Clock()

def load_background(image_path='images/background/-1.png'):
    try:
        image = pygame.image.load(image_path)
        image = image.convert()
        return pygame.transform.scale(image, (screen_width, screen_height))
    except:
        bg = pygame.Surface((screen_width, screen_height))
        bg.fill((0, 0, 0))
        return bg


def load_digit_images(folder="images/digits", width=80, height=80):
    images = {}
    for i in range(10):
        file_path = os.path.join(folder, f"{i}.png")
        if os.path.exists(file_path):
            try:
                img = pygame.image.load(file_path)
                images[str(i)] = pygame.transform.scale(img, (width, height))
            except:
                images[str(i)] = create_digit_placeholder(i, width, height)
        else:
            images[str(i)] = create_digit_placeholder(i, width, height)
    return images


def create_digit_placeholder(digit, width, height):
    surf = pygame.Surface((width, height))
    surf.fill((100, 100, 100))
    font = pygame.font.SysFont(None, 60)
    text = font.render(str(digit), True, (255, 255, 255))
    text_rect = text.get_rect(center=(width//2, height//2))
    surf.blit(text, text_rect)
    return surf


def draw_score(surface, score, images, x, y, spacing=5, digits=6):
    if not images:
        return
    score_str = str(score).zfill(digits)
    if "0" in images:
        digit_width = images["0"].get_width()
    else:
        digit_width = 80
    for i, digit in enumerate(score_str):
        if digit in images:
            img = images[digit]
            x_pos = x + i * (digit_width + spacing)
            surface.blit(img, (x_pos, y))


background = load_background('images/background/-1.png')
digit_images = load_digit_images("images/digits", 80, 80)

current_score = 0
display_x = 920
display_y = 157
digit_spacing = 0
num_digits = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    draw_score(screen, current_score, digit_images, 
               display_x, display_y, digit_spacing, num_digits)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()