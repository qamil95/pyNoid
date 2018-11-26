from enum import Enum
import pygame


class Colors(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    CYAN = 3
    VIOLET = 4
    GREEN = 5
    BLUE = 6
    YELLOW = 7
    ORANGE = 8
    BROWN = 9
    LIGHT_RED = 10
    DARK_GREY = 11
    GREY = 12
    LIGHT_GREEN = 13
    LIGHT_BLUE = 14
    LIGHT_GREY = 15


pygame_colors = {Colors.BLACK: pygame.Color(0, 0, 0),
                 Colors.WHITE: pygame.Color(255, 255, 255),
                 Colors.RED: pygame.Color(136, 0, 0, 0),
                 Colors.CYAN: pygame.Color(170, 255, 238, 0),
                 Colors.VIOLET: pygame.Color(204, 68, 204, 0),
                 Colors.GREEN: pygame.Color(0, 204, 85, 0),
                 Colors.BLUE: pygame.Color(0, 0, 170, 0),
                 Colors.YELLOW: pygame.Color(238, 238, 119, 0),
                 Colors.ORANGE: pygame.Color(221, 136, 85, 0),
                 Colors.BROWN: pygame.Color(102, 68, 0, 0),
                 Colors.LIGHT_RED: pygame.Color(255, 119, 119, 0),
                 Colors.DARK_GREY: pygame.Color(51, 51, 51, 0),
                 Colors.GREY: pygame.Color(119, 119, 119, 0),
                 Colors.LIGHT_GREEN: pygame.Color(170, 255, 102, 0),
                 Colors.LIGHT_BLUE: pygame.Color(0, 136, 255, 0),
                 Colors.LIGHT_GREY: pygame.Color(187, 187, 187, 0)}
