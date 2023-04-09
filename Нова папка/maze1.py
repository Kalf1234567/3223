import pygame
import random

# инициализация Pygame
pygame.init()

# установка размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# установка заголовка окна
pygame.display.set_caption("Лабиринт")

# установка фона
background = pygame.image.load("background.jpg")

# установка персонажа
player_image = pygame.image.load("hero.png")
player_width = 50
player_height = 50
player_x = WINDOW_WIDTH // 2 - player_width // 2
player_y = WINDOW_HEIGHT - player_height
player_speed = 5

# установка врага
enemy_image = pygame.image.load("1234.jpg")
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, WINDOW_WIDTH - enemy_width)
enemy_y = random.randint(0, WINDOW_HEIGHT - enemy_height)
enemy_speed = 3

# установка золота
gold_image = pygame.image.load("treasure.png")
gold_width = 50
gold_height = 50
gold_x = random.randint(0, WINDOW_WIDTH - gold_width)
gold_y = random.randint(0, WINDOW_HEIGHT - gold_height)

wall_image = pygame.image.load("aaaaa.png")
wall_width = 1
wall_height = 1
wall_image = pygame.image.load("aaaaa.png")
wall_width, wall_height = wall_image.get_width(), wall_image.get_height()

# установка уровней
levels = [
    {"map": [
        "WWWWWWWWWW",
        "W.......EW",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "WWWWWWWWWW",
    ], "enemy_speed": 3, "gold_x": 100, "gold_y": 100},
    {"map": [
        "WWWWWWWWWW",
        "W.......EW",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "WWWWWWWWWW",
    ], "enemy_speed": 4, "gold_x": 200, "gold_y": 200},
    {"map": [
        "WWWWWWWWWW",
        "W.......EW",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "W........W",
        "WWWWWWWWWW",
    ], "enemy_speed": 5, "gold_x": 300, "gold_y": 300},
]
current_level = 0

# функция, которая рисует карту уровня
def draw_map(level):
    map = levels[level]["map"]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "W":
                window.blit(wall_image, (x * wall_width, y * wall_height))

def check_collision(enemy_x, enemy_y, player_x, player_y, player_width, player_height):
    if (enemy_x < player_x + player_width and
        enemy_x + enemy_width > player_x and
        enemy_y < player_y + player_height and
        enemy_y + enemy_height > player_y):
        return True
    else:
        return False
# основной игровой цикл
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление персонажем с помощью стрелок
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # проверка столкновения с врагом
    if check_collision(enemy_x, enemy_y, player_x, player_y, player_width, player_height):
        print("Игрок столкнулся с врагом!")
        running = False

    # проверка столкновения с золотом
    if (gold_x < player_x + player_width and
        gold_x + gold_width > player_x and
        gold_y < player_y + player_height and
        gold_y + gold_height > player_y):
        print("Игрок нашел золото!")
        gold_x = random.randint(0, WINDOW_WIDTH - gold_width)
        gold_y = random.randint(0, WINDOW_HEIGHT - gold_height)

    # движение врага
    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed

    # отрисовка элементов на экране
    window.blit(background, (0, 0))
    window.blit(player_image, (player_x, player_y))
    window.blit(enemy_image, (enemy_x, enemy_y))
    window.blit(gold_image, (gold_x, gold_y))
    draw_map(current_level)
    pygame.display.update()

# завершение Pygame
pygame.quit()