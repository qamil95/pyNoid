from launcher import Launcher
from game import Game

launcher = Launcher()
launcher.set_configuration()
game = Game(launcher.resolution, launcher.random_level)
game.main_loop()
