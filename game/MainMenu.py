import pygame.display

from engine.eventHandlers.inputHandlers.clickObjectInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler

from objects.worldObjects.textObject import TextObject
from objects.worldObjects.backGroundObject import BackgroundObject
class MainMenu(Game):

    def __init__(self):
        super().__init__(EventHandler(), Renderer())

    def reset(self):
        self.__init__()

    def run(self):

        self.eventHandler.process_events()
        self.renderer.render()

    def create_objects(self):
        size = pygame.display.get_window_size()
        self.worldObjects.append(BackgroundObject(1, (0, 0), (178, 255, 46), size))
        start_button = TextObject(2, (size[0] / 2, size[1] / 2), "Start", 30, (0, 20, 0))
        inputHandler = InputHandler(self.exit_game, start_button)
        self.eventHandler.add_event(inputHandler.process_input)

        self.worldObjects.append(start_button)