from level_loader import LevelLoader


class LevelManager:
    def __init__(self, resolution, random_level):
        self.level_loader = LevelLoader(resolution)
        if random_level:
            self.level_loader.load_random_level(20, 10)
        else:
            self.level_loader.load_xml_level("Levels\Level1.xml")
        self.bricks = self.level_loader.level.bricks

    def initialize_brick_size(self, columns, rows):
        self.level_loader.initialize_brick_size(columns, rows)

    def get_bottomright_corner(self):
        return max(brick.rect.bottomright for brick in self.level_loader.level.bricks)

    def get_topleft_corner(self):
        return min(brick.rect.topleft for brick in self.level_loader.level.bricks)
