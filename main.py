# main.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GROUND_LEVEL
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cuphead")
clock = pygame.time.Clock()

# Colors
PURPLE = (50, 0, 50)
GREEN = (0, 200, 0)

# Sprites
player = Player((100, GROUND_LEVEL - 100))
all_sprites = pygame.sprite.Group(player)

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(keys)

    screen.fill(PURPLE)
    pygame.draw.rect(screen, GREEN, (0, GROUND_LEVEL, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_LEVEL))  # ground
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
