import pygame


class Ball:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.position = pygame.Vector2(float(x), float(y))
        self.movement = pygame.Vector2(3.0, -3.0)

    def check_collision_axis(self, brick: pygame.Rect):
        position = pygame.Vector2(self.position)
        ball = self.rect.copy()
        while ball.colliderect(brick):
            position -= self.movement / 10
            ball.center = (int(position.x), int(position.y))

        ball.center = (int(position.x + self.movement.x / 10), int(position.y))
        collision_x = ball.colliderect(brick)

        ball.center = (int(position.x), int(position.y + self.movement.y / 10))
        collision_y = ball.colliderect(brick)

        return collision_x, collision_y

    def update_position(self):
        self.position += self.movement
        self.rect.center = (int(self.position.x), int(self.position.y))

    def bounce(self, x, y):
        if x:
            self.movement.x *= -1
        if y:
            self.movement.y *= -1
