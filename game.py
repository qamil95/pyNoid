import pygame
import sys
import constants
from brickmanager import BrickManager
from brick import BrickTypes
from ball import Ball


class Game:
    def __init__(self, resolution, random_level, mouse_input):
        self.resolution = resolution

        pygame.init()
        pygame.display.set_caption(constants.WINDOW_TITLE)

        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.mouse_input = mouse_input

        self.brickManager = BrickManager(resolution, random_level)
        self.border = self.create_border()
        self.player = pygame.Rect(resolution[0] / 2, resolution[1] - 100, 200, 50)
        self.ball = Ball(resolution[0] / 2, resolution[1] / 2, 20, 20)

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
        for brick in self.brickManager.bricks:
            if brick.rect.colliderect(self.ball.rect):
                brick.type = BrickTypes.DESTROYED

    def draw_screen(self):
        self.screen.fill(pygame.Color("grey"))
        pygame.draw.rect(self.screen, pygame.Color("grey60"), self.border, constants.BORDER_WIDTH)
        for brick in self.brickManager.bricks:
            if brick.type != BrickTypes.DESTROYED:
                pygame.draw.rect(self.screen, brick.color, brick.rect)
        pygame.draw.rect(self.screen, pygame.Color("red"), self.player)
        pygame.draw.rect(self.screen, pygame.Color("green"), self.ball.rect)
        pygame.display.flip()

    def main_loop(self):
        while True:
            self.clock.tick(constants.FRAMES_PER_SECOND)
            self.handle_events()
            self.handle_input()
            self.calculate_state()
            self.draw_screen()
