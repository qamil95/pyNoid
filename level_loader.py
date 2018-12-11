import constants
import level_parser
import random
from level import Level


class LevelLoader:
    def __init__(self, resolution):
        self.screen_width = resolution[0]
        self.screen_height = resolution[1]
        self.level = None

    def initialize_brick_size(self, columns, rows):
        width = (self.screen_width - 2 * constants.SCREEN_MARGIN - (columns + 1) * constants.BRICK_DISTANCE) / columns
        height = ((self.screen_height / 3) - constants.SCREEN_MARGIN - (rows + 1) * constants.BRICK_DISTANCE) / rows
        self.level = Level(int(width), int(height))

    def load_random_level(self, columns, rows):
        self.initialize_brick_size(columns, rows)

        for x in range(columns):
            for y in range(rows):
                self.level.append_brick(x, y, random.randint(0, 14), 1)

    def load_xml_level(self, file_path):
        parsed_bricks = level_parser.parse(file_path)

        from operator import itemgetter
        max_row = max(parsed_bricks, key=itemgetter(0))[0]
        max_column = max(parsed_bricks, key=itemgetter(1))[1]
        self.initialize_brick_size(max_column + 1, max_row + 1)

        for parsed_brick in parsed_bricks:
            self.level.append_brick(parsed_brick[1], parsed_brick[0], parsed_brick[2], parsed_brick[3])
