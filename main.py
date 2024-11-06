from engine.utils.getScreenResolution import get_screen_resolution
from game.Arena import Arena
from game.MainMenu import MainMenu
from engine.manager import GameManager

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def run():

    menu = MainMenu()
    arena = Arena()
    config = [menu,arena]

    res = get_screen_resolution()

    manager = GameManager(config, res, False)
    manager.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
