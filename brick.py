import pygame
from enum import Enum
from colors import pygame_colors, Colors


class BrickTypes(Enum):
    DESTROYED = 0
    LIGHT = 1
    DARK = 2
    SOLID = 100


class Brick:
    def __init__(self, x, y, width, height, type_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.type = BrickTypes(type_id)
        self.color = self.color[self.type]

    color = {BrickTypes.LIGHT: pygame_colors[Colors.YELLOW],
             BrickTypes.DARK: pygame_colors[Colors.ORANGE],
             BrickTypes.SOLID: pygame_colors[Colors.BLUE]}
