# player.py

import pygame
from settings import GRAVITY, GROUND_LEVEL

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/cuphead.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.velocity = pygame.math.Vector2(0, 0)
        self.on_ground = False

    def handle_input(self, keys):
        self.velocity.x = 0
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = -15
            self.on_ground = False

    def apply_gravity(self):
        self.velocity.y += GRAVITY
        self.rect.y += self.velocity.y

        if self.rect.bottom >= GROUND_LEVEL:
            self.rect.bottom = GROUND_LEVEL
            self.velocity.y = 0
            self.on_ground = True

    def update(self, keys):
        self.handle_input(keys)
        self.rect.x += self.velocity.x
        self.apply_gravity()
