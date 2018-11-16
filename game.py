import pygame
import sys
import constants
from brickmanager import BrickManager
from brick import BrickTypes


class Game:
    def __init__(self, resolution, random_level):
        self.resolution = resolution

        pygame.init()
        pygame.display.set_caption(constants.WINDOW_TITLE)

        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

        self.brickManager = BrickManager(resolution, random_level)
        self.border = self.create_border()
        self.player = pygame.Rect(resolution[0] / 2, resolution[1] / 2, 200, 50)
        self.ball = pygame.Rect(100, 100, 20, 20)

    def create_border(self):
        left, top = self.brickManager.get_topleft_corner()
        right, bottom = self.brickManager.get_bottomright_corner()
        width = right - left
        return pygame.Rect(left - constants.BORDER_WIDTH,
                           top - constants.BORDER_WIDTH,
                           width + 2 * constants.BORDER_WIDTH,
                           self.resolution[1])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def handle_keyboard(self):
        pressed = pygame.key.get_pressed()
        for key in self.move_mapping:
            if pressed[key]:
                self.ball = self.ball.move(self.move_mapping[key])

    def handle_mouse(self):
        x, _ = pygame.mouse.get_pos()
        self.player.centerx = x

    def draw_screen(self):
        # TEMPORARY
        for brick in self.brickManager.bricks:
            if brick.rect.colliderect(self.ball):
                brick.type = BrickTypes.DESTROYED
        # END TEMPORARY

        self.screen.fill(pygame.Color("grey"))
        pygame.draw.rect(self.screen, pygame.Color("grey60"), self.border, constants.BORDER_WIDTH)
        for brick in self.brickManager.bricks:
            if brick.type != BrickTypes.DESTROYED:
                pygame.draw.rect(self.screen, brick.color, brick.rect)
        pygame.draw.rect(self.screen, pygame.Color("red"), self.player)
        pygame.draw.rect(self.screen, pygame.Color("green"), self.ball)
        pygame.display.flip()

    def main_loop(self):
        while True:
            self.clock.tick(constants.FRAMES_PER_SECOND)
            self.handle_events()
            self.handle_keyboard()
            self.handle_mouse()
            self.draw_screen()

    move_mapping = {pygame.K_LEFT: (-1, 0),
                    pygame.K_RIGHT: (1, 0),
                    pygame.K_UP: (0, -1),
                    pygame.K_DOWN: (0, 1)}
