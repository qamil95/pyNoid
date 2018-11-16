import constants


def print_title():
    title = f"**{constants.WINDOW_TITLE}**"
    print('*' * len(title))
    print(title)
    print('*' * len(title))


class Launcher:
    resolution = None
    random_level = True

    def set_configuration(self):
        print_title()
        self.set_resolution()
        self.set_level()

    def set_resolution(self):
        width = input("Screen width: ")
        height = input("Screen height: ")
        try:
            self.resolution = (int(width), int(height))
        except ValueError:
            print(f"Wrong values, using default resolution {constants.DEFAULT_RESOLUTION}")
            self.resolution = constants.DEFAULT_RESOLUTION

    def set_level(self):
        level = input("1 - random level, 2 - level from xml: ")
        if level == "1":
            self.random_level = True
        else:
            self.random_level = False
        print("Random level would be generated" if self.random_level else "XML level would be used")
