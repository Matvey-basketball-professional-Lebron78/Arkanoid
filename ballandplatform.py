import sys
import pygame
import math 
pygame.init() #что-то

#константы целого экрана
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

#константы игрового окна
WINDOW_WIDTH = 833
WINDOW_HEIGHT = 685
WINDOW_X = 52
WINDOW_Y = 55

#цвета
WHITE = (255,  255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#платформа
class Platform():
    #создаём объект платформы с определёнными параметрами
    def __init__(self, x, y, width, height, speed, window_width, window_x):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.screen_width = window_x + window_width
    #перемещение платформы влево, если она не достигла края
    def move_left (self, window_x):
        if self.rect.left > window_x:
            self.rect.x -= self.speed
    #перемещение платформы вправо, если она не достигает другого края
    def move_right (self):
        if self.rect.right < self.screen_width:
            self.rect.x += self.speed
    #отрисовка платформы
    def draw (self, screen) :
        pygame.draw.rect (screen, BLUE, self.rect)

#мяч
class Ball():
    #создаём объект мяча с определёнными параметрами
    def __init__(self, x, y, radius, speed, window_width, window_height, window_x, window_y):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.speed = speed
        self.angle = math.pi / 4 
        self.screen_width = window_x + window_width
        self.screen_height = window_y + window_height
        self.active = False
    
    #устанавливает мяч в исходной позиции на платформе
    def activate(self,platform_rect):
        if not self.active:
            self.active = True
            self.rect.midbottom = platform_rect.midtop
    #обновление положения мяча, если он активен
    def update(self, platform):
        if not self.active:
            return
        
        dx = math.cos(self.angle) * self.speed
        dy = -math.sin(self.angle) * self.speed

        self.rect.x += dx
        self.rect.y += dy

        self._check_boundary_collision(window_x = WINDOW_X)
        self._check_platform_collision(platform)
    
    #отталкивание от стенок
    def _check_boundary_collision(self, window_x):
        if self.rect.left <= window_x:
            self.rect.left = window_x
            self.angle = math.pi - self.angle
        elif self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width
            self.angle = math.pi - self.angle
        if self.rect.top <= 0:
            self.rect.top = 0
            self.angle = -self.angle
    
    # отталкивание от платформы
    def _check_platform_collision(self, platform):
        if self.rect.colliderect(platform.rect) and self.rect.bottom >= platform.rect.top:
            # вычисляем расстояние от цетра платформы до центра мяча
            delta_x = self.rect.centerx - platform.rect.centerx
            # нормализуем относительно половины ширины и ограничим 
            new_delta_x = max(-1, min(1, delta_x/(platform.rect.width/2)))
            # ищем угол отражения
            max_angle = math.radians(75)
            real_angle = new_delta_x * max_angle

            speed = self.speed
            self.angle = math.pi / 2 + real_angle
            self.rect.bottom = platform.rect.top
    def draw(self, screen):
        pygame.draw.circle(screen, RED, self.rect.center, self.radius)


def start(screen, clock):
    #создание платформы посередине снизу
    platform = Platform(x = WINDOW_WIDTH // 2 + WINDOW_X - 50, 
                        y = WINDOW_HEIGHT + WINDOW_Y - 30,
                        width = 100,
                        height = 20,
                        speed = 5,
                        window_width = WINDOW_WIDTH,
                        window_x = WINDOW_X)

    #создание мяча на поатформе
    ball = Ball(x = platform.rect.centerx,
                y = platform.rect.top - 10,
                radius = 10,
                speed = 7,
                window_width = WINDOW_WIDTH,
                window_height = WINDOW_HEIGHT,
                window_x = WINDOW_X,
                window_y = WINDOW_Y)

    #обработка события закрытия окна
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            #привязка нажатия кнопок мыши к перемещениям платформы
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    platform.move_left(window_x = WINDOW_X)
                elif event.button == 3:
                    platform.move_right()
                elif event.button == 2:
                    ball.activate(platform.rect)
        
        # if game.lose:
        #    return score
         
        #при удержании кнопки платформа продолжает двигаться
        mouse_button = pygame.mouse.get_pressed()
        if mouse_button[0]:
            platform.move_left(window_x = WINDOW_X)
        if mouse_button[2]:
            platform.move_right()
        #неактивный мяч - на платформе + обновление координат активного мяча
        if not ball.active:
            ball.rect.midbottom = platform.rect.midtop
        ball.update(platform)
        #инактивация мяча в случае вылета за нижнюю границу
        if ball.rect.top > WINDOW_Y + WINDOW_HEIGHT:
            ball.active = False
        #отрисовка объектов
        screen.fill(WHITE)
        platform.draw(screen)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    #создаётся окно, с заголовком
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Arkanoid")
    clock = pygame.time.Clock()
    x = start(screen, clock)
    print(x)
    pygame.quit()
    sys.exit()
