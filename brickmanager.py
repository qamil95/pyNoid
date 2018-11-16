import random
import xmltodict
import constants
from brick import Brick


class BrickManager:
    brick_width = None
    brick_height = None
    bricks = []

    def __init__(self, resolution, random_level):
        self.screen_width = resolution[0]
        self.screen_height = resolution[1]
        if random_level:
            self.generate_random_bricks(20, 10)
        else:
            self.generate_bricks_from_xml("Level1.xml")

    def initialize_brick_size(self, columns, rows):
        width = (self.screen_width - 2 * constants.SCREEN_MARGIN - (columns + 1) * constants.BRICK_DISTANCE) / columns
        height = ((self.screen_height / 3) - constants.SCREEN_MARGIN - (rows + 1) * constants.BRICK_DISTANCE) / rows
        self.brick_width = int(width)
        self.brick_height = int(height)

    def append_brick(self, column, row, type_id):
        self.bricks.append(Brick(constants.SCREEN_MARGIN + column * (self.brick_width + constants.BRICK_DISTANCE),
                                 constants.SCREEN_MARGIN + row * (self.brick_height + constants.BRICK_DISTANCE),
                                 self.brick_width,
                                 self.brick_height,
                                 type_id))

    def generate_random_bricks(self, columns, rows):
        self.initialize_brick_size(columns, rows)
        for x in range(columns):
            for y in range(rows):
                self.append_brick(x, y, random.randint(1, 2))

    def generate_bricks_from_xml(self, file_path):
        with open(file_path) as fd:
            doc = xmltodict.parse(fd.read())
            rows = doc["Level"]["Rows"]
            parsed_bricks = []
            for row in rows["Row"]:
                row_number = int(row["@id"])
                blocks = row["Blocks"]
                for block in blocks["Block"]:
                    column_number = int(block["@column"])
                    block_type = int(block["@type"])
                    parsed_bricks.append((row_number, column_number, block_type))

            from operator import itemgetter
            max_row = max(parsed_bricks, key=itemgetter(0))[0]
            max_column = max(parsed_bricks, key=itemgetter(1))[1]
            self.initialize_brick_size(max_column + 1, max_row + 1)

            for parsed_brick in parsed_bricks:
                self.append_brick(parsed_brick[1], parsed_brick[0], parsed_brick[2])

    def get_bottomright_corner(self):
        return max(brick.rect.bottomright for brick in self.bricks)

    def get_topleft_corner(self):
        return min(brick.rect.topleft for brick in self.bricks)
