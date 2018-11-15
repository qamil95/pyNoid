import random
import xmltodict
from brick import Brick


class BrickManager:
    BRICK_DISTANCE = 1
    SCREEN_MARGIN = 20
    brick_width = None
    brick_height = None
    bricks = []

    def __init__(self, resolution):
        self.screen_width = resolution[0]
        self.screen_height = resolution[1]

    def initialize_brick_size(self, columns, rows):
        self.brick_width = int((self.screen_width - 2*self.SCREEN_MARGIN - (columns+1)*self.BRICK_DISTANCE) / columns)
        self.brick_height = int(((self.screen_height / 3) - self.SCREEN_MARGIN - (rows+1)*self.BRICK_DISTANCE) / rows)

    def append_brick(self, column, row, type_id):
        self.bricks.append(Brick(self.SCREEN_MARGIN + column*(self.brick_width + self.BRICK_DISTANCE),
                                 self.SCREEN_MARGIN + row*(self.brick_height + self.BRICK_DISTANCE),
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
