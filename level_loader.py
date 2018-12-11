import constants


class LevelLoader:
    def __init__(self, resolution):
        self.screen_width = resolution[0]
        self.screen_height = resolution[1]
        self.brick_width = None
        self.brick_height = None

    def generate_random_bricks(self):
        pass

    def generate_bricks_from_xml(self):
        pass

    def initialize_brick_size(self, columns, rows):
        width = (self.screen_width - 2 * constants.SCREEN_MARGIN - (columns + 1) * constants.BRICK_DISTANCE) / columns
        height = ((self.screen_height / 3) - constants.SCREEN_MARGIN - (rows + 1) * constants.BRICK_DISTANCE) / rows
        self.brick_width = int(width)
        self.brick_height = int(height)
