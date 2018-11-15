import pygame
from enum import Enum


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

    color = {BrickTypes.DESTROYED: pygame.Color("grey"),
             BrickTypes.LIGHT: pygame.Color("orange"),
             BrickTypes.DARK: pygame.Color("darkorange"),
             BrickTypes.SOLID: pygame.Color("dodgerblue")}
