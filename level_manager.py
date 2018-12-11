import random
import xmltodict
import constants
from brick import Brick
from level_loader import LevelLoader


class LevelManager:
    level_loader = None
    brick_width = None
    brick_height = None
    bricks = []

    def __init__(self, resolution, random_level):
        self.level_loader = LevelLoader(resolution)
        if random_level:
            self.generate_random_bricks(20, 10)
        else:
            self.generate_bricks_from_xml("Levels\Level1.xml")

    def initialize_brick_size(self, columns, rows):
        self.level_loader.initialize_brick_size(columns, rows)
        self.brick_height = self.level_loader.brick_height
        self.brick_width = self.level_loader.brick_width

    def append_brick(self, column, row, color_id, type_id):
        self.bricks.append(Brick(constants.SCREEN_MARGIN + column * (self.brick_width + constants.BRICK_DISTANCE),
                                 constants.SCREEN_MARGIN + row * (self.brick_height + constants.BRICK_DISTANCE),
                                 self.brick_width,
                                 self.brick_height,
                                 color_id,
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
                blocks = row["Bricks"]
                for block in blocks["Brick"]:
                    column_number = int(block["@column"])
                    color_id = int(block.get("@color", 0))
                    block_type = int(block.get("@type", 0))
                    parsed_bricks.append((row_number, column_number, color_id, block_type))

            from operator import itemgetter
            max_row = max(parsed_bricks, key=itemgetter(0))[0]
            max_column = max(parsed_bricks, key=itemgetter(1))[1]
            self.initialize_brick_size(max_column + 1, max_row + 1)

            for parsed_brick in parsed_bricks:
                self.append_brick(parsed_brick[1], parsed_brick[0], parsed_brick[2], parsed_brick[3])

    def get_bottomright_corner(self):
        return max(brick.rect.bottomright for brick in self.bricks)

    def get_topleft_corner(self):
        return min(brick.rect.topleft for brick in self.bricks)
