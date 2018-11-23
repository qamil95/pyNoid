import pygame
import constants
from math import isclose
from brick import BrickTypes


class Ball:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.position = pygame.Vector2(float(x), float(y))
        self.movement = pygame.Vector2()
        self.collision_x = False
        self.collision_y = False

    def start(self, ball_speed=constants.START_BALL_SPEED):
        if isclose(self.movement.length(), 0.0):
            self.movement.y = -ball_speed

    def check_collision_axis(self, to_check: pygame.Rect):
        position = pygame.Vector2(self.position)
        ball = self.rect.copy()
        collision_step = self.movement / constants.CHECK_COLLISION_STEPS
        while ball.colliderect(to_check):
            position -= collision_step
            ball.center = (int(position.x), int(position.y))

        ball.center = (int(position.x + collision_step.x), int(position.y))
        self.collision_x = self.collision_x or ball.colliderect(to_check)

        ball.center = (int(position.x), int(position.y + collision_step.y))
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

    def check_paddle_collision(self, paddle: pygame.Rect):
        if paddle.colliderect(self.rect):
            distance = self.rect.centerx - paddle.centerx
            angle_ratio = distance / (paddle.w / 2)
            new_angle = (angle_ratio * constants.MAX_PADDLE_BOUNCE_ANGLE)
            self.movement.rotate_ip(self.movement.angle_to(pygame.Vector2(0, -1)) + new_angle)

    def check_border_collision(self, borders):
        for border in borders:
            self.check_collision_axis(border)

    def bounce(self):
        if self.collision_x:
            self.movement.x *= -1
        if self.collision_y:
            self.movement.y *= -1

        self.collision_x = self.collision_y = False
