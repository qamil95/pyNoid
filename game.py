import pygame
import sys
import constants
from level_manager import LevelManager
from brick import BrickTypes
from ball import Ball
from colors import pygame_colors, Colors


class Game:
    def __init__(self, resolution, random_level, mouse_input):
        self.resolution = resolution

        pygame.init()
        pygame.display.set_caption(constants.WINDOW_TITLE)

        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.mouse_input = mouse_input

        self.level_manager = LevelManager(resolution, random_level)
        self.borders = self.create_border()
        self.player = pygame.Rect(resolution[0] / 2, resolution[1] - 100, 200, 50)
        self.ball = Ball(resolution[0] / 2, resolution[1] / 2, 20, 20)

    def create_border(self):
        left, top = self.level_manager.get_topleft_corner()
        right, bottom = self.level_manager.get_bottomright_corner()
        width = right - left
        left_border = pygame.Rect(left - 2 * constants.BORDER_WIDTH,
                                  top - 2 * constants.BORDER_WIDTH,
                                  constants.BORDER_WIDTH,
                                  self.resolution[1] + constants.BOTTOM_BORDER_DISTANCE)
        top_border = pygame.Rect(left - 2 * constants.BORDER_WIDTH,
                                 top - 2 * constants.BORDER_WIDTH,
                                 width + 4 * constants.BORDER_WIDTH,
                                 constants.BORDER_WIDTH)
        right_border = pygame.Rect(right + constants.BORDER_WIDTH,
                                   top - constants.BORDER_WIDTH,
                                   constants.BORDER_WIDTH,
                                   self.resolution[1] + constants.BOTTOM_BORDER_DISTANCE)
        bottom_border = pygame.Rect(left - 2 * constants.BORDER_WIDTH,
                                    self.resolution[1] + constants.BOTTOM_BORDER_DISTANCE,
                                    width + 4 * constants.BORDER_WIDTH,
                                    constants.BORDER_WIDTH)

        return [left_border, top_border, right_border, bottom_border]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.ball.start()

    def handle_input(self):
        if self.mouse_input:
            x, _ = pygame.mouse.get_pos()
            self.player.centerx = x
        else:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.player.centerx -= 3
            elif pressed[pygame.K_RIGHT]:
                self.player.centerx += 3

    def calculate_state(self):
        self.ball.update_position()
        self.ball.check_brick_collision(self.level_manager.bricks)
        self.ball.check_paddle_collision(self.player)
        self.ball.check_border_collision(self.borders)
        self.ball.bounce()

    def draw_screen(self):
        self.screen.fill(pygame_colors[Colors.LIGHT_GREY])
        for border in self.borders:
            pygame.draw.rect(self.screen, pygame_colors[Colors.GREY], border)
        for brick in self.level_manager.bricks:
            if brick.type != BrickTypes.DESTROYED:
                pygame.draw.rect(self.screen, brick.color, brick.rect)
        pygame.draw.rect(self.screen, pygame_colors[Colors.RED], self.player)
        pygame.draw.rect(self.screen, pygame_colors[Colors.GREEN], self.ball.rect)
        pygame.display.flip()

    def main_loop(self):
        while True:
            self.clock.tick(constants.FRAMES_PER_SECOND)
            self.handle_events()
            self.handle_input()
            self.calculate_state()
            self.draw_screen()
