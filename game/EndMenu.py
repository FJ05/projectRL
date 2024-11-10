import pygame.display

from engine.eventHandlers.inputHandlers.clickObjectInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler

from objects.worldObjects.textObject import TextObject
from objects.worldObjects.backGroundObject import BackgroundObject

# This class is for a simple death or win menu. Menus are games afterall!
class EndMenu(Game):

    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        self.screen_size = None

    def reset(self):
        self.__init__()

    def run(self):

        self.eventHandler.process_events()
        self.renderer.render()

    # Create all text object, background and thier inputhandler to be able to click on text
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
        self.end_menu_create()

    def end_menu_create(self):
        reason_text = TextObject(2, (self.screen_size[0] / 2 - 40, self.screen_size[1] / 4 ), self.end_reason, 70, (0, 20, 0))
        reason_text.add_tag("reason")

        score_text = TextObject(2, (self.screen_size[0] / 2 - 40, self.screen_size[1] / 4 + 70 ), "?", 50, (0, 20, 0))
        score_text.add_tag("score")

        self.eventHandler.add_event(self.update_text)

        self.worldObjects.append(reason_text)
        self.worldObjects.append(score_text)

    # update the text on the screen to say what reason the game ender so win or loose and the score from the previos game.
    def update_text(self):
        reason_text = self.get_world_by_tag("reason")[0]
        reason_text.set_text(self.end_reason)

        score_text = self.get_world_by_tag("score")[0]
        score_text.set_text(f'Your Score: {self.score}')
