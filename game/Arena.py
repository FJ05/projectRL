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
        # this is the background asset which will be loaded as the background
        self.arena_path = "assets/environment/arena.png"



    def run(self):

        self.eventHandler.process_events()
        self.renderer.render()

    def create_objects(self):
        # sets display size
        background_size = pygame.display.get_window_size()
        
        # Loads the background image
        background_img = pygame.image.load(self.arena_path).convert()
        
        # sets the game backgound as the background
        background = BackgroundObject(1, (0, 0), (255, 255, 255), background_size, image=background_img)
        self.worldObjects.append(background)
        
        # Sets the player pos in the middle of the screen
        player = Player(3, (background_size[0]/2, background_size[1]/2))
        inputHandler = InputHandler(player.update_movement, player)
        self.eventHandler.add_event(inputHandler.process_input)
        self.entityObjects.append(player)