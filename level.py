import constants
from brick import Brick


class Level:
    def __init__(self, width, height):
        self.brick_width = width
        self.brick_height = height
        self.bricks = []
        self.bricks_to_hit = 0

    def append_brick(self, column, row, color_id, type_id):
        brick = Brick(constants.SCREEN_MARGIN + column * (self.brick_width + constants.BRICK_DISTANCE),
                      constants.SCREEN_MARGIN + row * (self.brick_height + constants.BRICK_DISTANCE),
                      self.brick_width,
                      self.brick_height,
                      color_id,
                      type_id)
        self.bricks.append(brick)
        if brick.is_hittable:
            self.bricks_to_hit += 1
