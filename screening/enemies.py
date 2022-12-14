import pygame
import random
from helpers.helpers import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = enemy_y_coordinate() + random.randrange(1,15)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(10, 20)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = enemy_y_coordinate() + random.randrange(1,15)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(10, 20)

def enemy_y_coordinate():
    list = [210, 330, 485, 620]
    return random.choice(list)

# print(enemy_y_coordinate())