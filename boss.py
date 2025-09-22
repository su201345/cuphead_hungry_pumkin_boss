# boss.py

import pygame
import random

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/hungry_pumpkin.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.projectiles = pygame.sprite.Group()
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer % 90 == 0:
            self.throw_food()

        self.projectiles.update()

    def throw_food(self):
        food = Projectile((self.rect.centerx, self.rect.bottom))
        self.projectiles.add(food)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/burger.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.velocity = pygame.math.Vector2(random.choice([-4, 4]), 5)

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if self.rect.top > 600:
            self.kill()
