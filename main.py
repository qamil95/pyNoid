from launcher import Launcher
from game import Game

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# MAIN
launcher = Launcher()
launcher.set_configuration()
game = Game(launcher.resolution, launcher.random_level)
game.main_loop()
