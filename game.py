import pygame
import sys
from brickmanager import BrickManager
from brick import BrickTypes


class Game:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height

        pygame.init()
        pygame.display.set_caption("*** pyNoid ***")

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.brickManager = BrickManager(self.screen_width, self.screen_height)
        # self.brickManager.generate_random_bricks(20, 10)
        self.brickManager.generate_bricks_from_xml("Level1.xml")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def handle_keyboard(self, position):
        pressed = pygame.key.get_pressed()
        for key in self.move_mapping:
            if pressed[key]:
                position += self.move_mapping[key]

    def draw_screen(self):
        # TEMPORARY
        player = pygame.Rect(self.ball_position.x, self.ball_position.y, 200, 50)
        for brick in self.brickManager.bricks:
            if brick.rect.colliderect(player):
                brick.type = BrickTypes.DESTROYED
        # END TEMPORARY

        self.screen.fill(pygame.Color("grey"))
        for brick in self.brickManager.bricks:
            if brick.type != BrickTypes.DESTROYED:
                pygame.draw.rect(self.screen, brick.color, brick.rect)
        pygame.draw.rect(self.screen, pygame.Color("red"), player)
        pygame.display.flip()

    def main_loop(self):
        while True:
            self.clock.tick(60)
            self.handle_events()
            self.handle_keyboard(self.ball_position)
            self.draw_screen()

    ball_position = pygame.math.Vector2(10, 10)
    move_mapping = {pygame.K_LEFT: pygame.Vector2(-1, 0),
                    pygame.K_RIGHT: pygame.Vector2(1, 0),
                    pygame.K_UP: pygame.Vector2(0, -1),
                    pygame.K_DOWN: pygame.Vector2(0, 1)}
