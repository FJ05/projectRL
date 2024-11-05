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
from objects.worldObjects.collitionObject import CollitionObject
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

        # Loads the background image
        background_img = pygame.image.load(self.arena_path).convert()
        
        # sets the game backgound as the background
        background = BackgroundObject(1, (0, 0), (255, 255, 255), self.screen_size, image=background_img)
        self.worldObjects.append(background)

        self.create_walls()
        self.create_player()

    def create_player(self):  
        # Sets the player pos in the middle of the screen
        player = Player(3, (self.screen_size[0]/2, self.screen_size[1]/2))
        player.add_tag("player")
        player.object_create(self.create_arrows)
        inputHandler = InputHandler(player.update_movement, player)
        attackHandler = ClickInputHandler(player.shoot, player)
        self.eventHandler.add_event(self.check_collitions)
        self.eventHandler.add_event(inputHandler.process_input)
        self.eventHandler.add_event(attackHandler.process_input)

        self.entityObjects.append(player)

    def create_walls(self):
        self.worldObjects.append(CollitionObject(2,(300,300),(100,200)))
        self.worldObjects.append(CollitionObject(2,(300,800),(100,200)))

    def create_arrows(self, pos, angle):
        arrow = Arrow(3, pos, angle)
        self.eventHandler.add_event(arrow.update_movement)
        self.entityObjects.append(arrow)

    def check_collitions(self):
        walls = self.get_world_by_tag("wall")
        player = self.get_entities_by_tag("player")[0]
        # Loop all the walls and check if player is colliding with one of them?
        player.collition(False)
        for wall in walls:

            if wall.get_rect().colliderect(player.get_rect()):
                player.collition(True)
        