from venv import create

import pygame

from engine.eventHandlers.inputHandlers.clickInputHandler import ClickInputHandler
from engine.eventHandlers.inputHandlers.movementInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler
from objects.entities.arrow import Arrow

from objects.entities.player import Player
from objects.worldObjects.backGroundObject import BackgroundObject
class Arena(Game):

    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        # this is the background asset which will be loaded as the background
        self.arena_path = "assets/environment/arena.png"

        self.screen_size = None
        # this is the background asset which will be loaded as the background
        self.arena_path = "assets/environment/arena.png"

    def run(self):

        self.eventHandler.process_events()
        self.renderer.render()

    def create_objects(self):

        self.screen_size = pygame.display.get_window_size()
        self.worldObjects.append(BackgroundObject(1, (0, 0), (5, 125,52), self.screen_size))

        self.create_player()

    def create_player(self):
        player = Player(3, (self.screen_size[0] / 2, self.screen_size[1] / 2))
        player.add_tag("player")
        player.object_create(self.create_arrows)

        # sets display size
        size = pygame.display.get_window_size()

        # sets display size
        background_size = pygame.display.get_window_size()
        
        # Loads the background image
        background_img = pygame.image.load(self.arena_path).convert()
        
        # sets the game backgound as the background
        background = BackgroundObject(1, (0, 0), (255, 255, 255), (800, 600), image=background_img)
        self.worldObjects.append(background)
        
        # Sets the player pos in the middle of the screen
        player = Player(3, (size[0]/2, size[1]/2))
        player.object_create(self.create_arrows)
        background = BackgroundObject(1, (0, 0), (255, 255, 255), background_size, image=background_img)
        self.worldObjects.append(background)
        
        # Sets the player pos in the middle of the screen
        player = Player(3, (background_size[0]/2, background_size[1]/2))

        inputHandler = InputHandler(player.update_movement, player)
        attackHandler = ClickInputHandler(player.shoot, player)
        self.eventHandler.add_event(inputHandler.process_input)
        self.eventHandler.add_event(attackHandler.process_input)

        self.entityObjects.append(player)

    def create_arrows(self, pos, angle):
        arrow = Arrow(3, pos, angle)
        self.eventHandler.add_event(arrow.update_movement)
        self.entityObjects.append(arrow)
