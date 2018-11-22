import pygame
from brick import BrickTypes


class Ball:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.position = pygame.Vector2(float(x), float(y))
        self.movement = pygame.Vector2(3.0, -3.0)
        self.collision_x = False
        self.collision_y = False

    def check_collision_axis(self, to_check: pygame.Rect):
        position = pygame.Vector2(self.position)
        ball = self.rect.copy()
        while ball.colliderect(to_check):
            position -= self.movement / 10
            ball.center = (int(position.x), int(position.y))

        ball.center = (int(position.x + self.movement.x / 10), int(position.y))
        self.collision_x = self.collision_x or ball.colliderect(to_check)

        ball.center = (int(position.x), int(position.y + self.movement.y / 10))
        self.collision_y = self.collision_y or ball.colliderect(to_check)

    def update_position(self):
        self.position += self.movement
        self.rect.center = (int(self.position.x), int(self.position.y))

    def check_brick_collision(self, bricks):
        for brick in bricks:
            if brick.rect.colliderect(self.rect):
                if brick.type != BrickTypes.DESTROYED:
                    self.check_collision_axis(brick.rect)
                    brick.type = BrickTypes.DESTROYED

    def bounce(self):
        if self.collision_x:
            self.movement.x *= -1
        if self.collision_y:
            self.movement.y *= -1

        self.collision_x = self.collision_y = False
