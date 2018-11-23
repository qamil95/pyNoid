import constants


def get_frame(text):
    return '*' * len(text)


def print_title():
    title = f"**{constants.WINDOW_TITLE}**"
    print(get_frame(title))
    print(title)
    print(get_frame(title))


def print_help():
    help_text = "** Press space to start **"
    print(get_frame(help_text))
    print(help_text)
    print(get_frame(help_text))


class Launcher:
    resolution = None
    random_level = True
    mouse_input = True

    def set_configuration(self):
        print_title()
        self.set_resolution()
        self.set_level()
        self.set_input_method()
        print_help()

    def set_resolution(self):
        width = input(f"Screen width (default - {constants.DEFAULT_RESOLUTION[0]}): ")
        height = input(f"Screen height(default - {constants.DEFAULT_RESOLUTION[1]}): ")
        try:
            self.resolution = (int(width), int(height))
        except ValueError:
            print(f">>> Wrong values, using default resolution {constants.DEFAULT_RESOLUTION}")
            self.resolution = constants.DEFAULT_RESOLUTION

    def set_level(self):
        level = input("1 - random level, 2 - level from xml (default - XML): ")
        if level == "1":
            self.random_level = True
        else:
            self.random_level = False
        print(">>> " + ("Random" if self.random_level else "XML") + " level would be used")

    def set_input_method(self):
        method = input("1 - mouse, 2 - keyboard (default - keyboard): ")
        if method == "1":
            self.mouse_input = True
        else:
            self.mouse_input = False
        print(">>> " + ("Mouse" if self.mouse_input else "Keyboard") + " input would be used")
