import pygame

from engine.eventHandlers.inputHandlers.defualtInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler

from objects.entities.player import Player
from objects.worldObjects.backGroundObject import BackgroundObject
class Arena(Game):

    def __init__(self):
        super().__init__(EventHandler(), Renderer())



    def run(self):

        self.eventHandler.process_events()
        self.renderer.render()

    def create_objects(self):
        size = pygame.display.get_window_size()
        self.worldObjects.append(BackgroundObject(1, (0, 0), (5, 125,52), size))
        player = Player(3, (size[0]/2, size[1]/2))
        inputHandler = InputHandler(player.update_movement, player)
        self.eventHandler.add_event(inputHandler.process_input)
        self.entityObjects.append(player)