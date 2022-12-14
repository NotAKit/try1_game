from screening.player import Player
from helpers.helpers import *
from screening.player import *
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
from screening.enemies import Enemy



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# добавляем врагов
for i in range(8):
    m = Enemy()
    all_sprites.add(m)
    enemies.add(m)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()
    if player_health == 0:
        running = False
    # проверка столкновений
    hits = pygame.sprite.spritecollide(player, enemies, True)
    if hits:
        player_health -= 1
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()