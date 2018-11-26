import pygame
from enum import Enum
from colors import pygame_colors, Colors


class BrickTypes(Enum):
    DESTROYED = 0
    STANDARD = 1
    ADDITIONAL_BALL = 3
    SOLID = 100


class Brick:
    def __init__(self, x, y, width, height, color_id, type_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.type = BrickTypes(type_id)
        self.color = pygame_colors[Colors(color_id)]
