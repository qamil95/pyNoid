def print_title():
    title = "***** pyNoid *****"
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
            print("Wrong values, using default 1280x720")
            self.resolution = (1280, 720)

    def set_level(self):
        level = input("1 - random level, 2 - level from xml: ")
        if level == "1":
            self.random_level = True
        else:
            self.random_level = False
        print("Random level would be generated" if self.random_level else "XML level would be used")
