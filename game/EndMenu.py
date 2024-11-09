import pygame.display

from engine.eventHandlers.inputHandlers.clickObjectInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler

from objects.worldObjects.textObject import TextObject
from objects.worldObjects.backGroundObject import BackgroundObject
class EndMenu(Game):

    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        self.screen_size = None

    def reset(self):
        self.__init__()

    def run(self):

        self.eventHandler.process_events()
        self.renderer.render()

    def create_objects(self):

        self.screen_size = pygame.display.get_window_size()
        self.worldObjects.append(BackgroundObject(1, (0, 0), (178, 255, 46), self.screen_size))
        main_menu_button = TextObject(2, (self.screen_size[0] / 3, self.screen_size[1] / 2), "Main Menu", 30, (0, 20, 0))
        main_menu_button.set_skip(1)
        inputHandler = InputHandler(self.exit_game, main_menu_button)
        self.eventHandler.add_event(inputHandler.process_input)

        restart_button = TextObject(2, (self.screen_size[0] / 3, self.screen_size[1] / 2 + 40), "Restart", 30,
                                      (0, 20, 0))
        restart_button.set_skip(2)
        restart_inputHandler = InputHandler(self.exit_game, restart_button)
        self.eventHandler.add_event(restart_inputHandler.process_input)



        self.worldObjects.append(main_menu_button)
        self.worldObjects.append(restart_button)
        self.end_reason_create()

    def end_reason_create(self):
        reason_text = TextObject(2, (self.screen_size[0] / 2 - 40, self.screen_size[1] / 4 ), self.end_reason, 70, (0, 20, 0))
        reason_text.add_tag("reason")
        self.eventHandler.add_event(self.update_reason)
        self.worldObjects.append(reason_text)

    def update_reason(self):
        reason_text = self.get_world_by_tag("reason")[0]
        reason_text.set_text(self.end_reason)
