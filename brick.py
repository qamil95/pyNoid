import pygame
from enum import Enum
from colors import pygame_colors, Colors


class BrickTypes(Enum):
    DESTROYED = 0
    STANDARD = 1
    STANDARD_OTHER_COLOR = 2  # For backward compatibility
    ADDITIONAL_BALLS = 3  # Spawns two additional balls after hit
    SOLID = 100  # Brick which is not destroyable


class Brick:
    def __init__(self, x, y, width, height, color_id, type_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.type = BrickTypes(type_id)
        self.color = pygame_colors[Colors(color_id)]

    def is_hittable(self):
        return self.type != BrickTypes.DESTROYED and self.type != BrickTypes.SOLID
