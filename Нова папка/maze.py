import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Определение размеров блоков
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Создание уровня
level = [
    "##########",
    "#        #",
    "#  $     #",
    "#        #",
    "#  ####  #",
    "#        #",
    "#@       #",
    "##########"
]

# Отображение уровня на экране
def draw_level(level):
    for y, row in enumerate(level):
        for x, block in enumerate(row):
            block_rect = pygame.Rect(x * BLOCK_WIDTH, y * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
            if block == "#":
                pygame.draw.rect(screen, BLACK, block_rect)
            elif block == "@":
                pygame.draw.rect(screen, WHITE, block_rect)
            elif block == "$":
                pygame.draw.rect(screen, RED, block_rect)

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона белым цветом
    screen.fill(WHITE)

    # Отображение уровня
    draw_level(level)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
