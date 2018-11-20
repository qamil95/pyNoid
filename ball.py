import pygame


class Ball:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
