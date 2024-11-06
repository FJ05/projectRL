from venv import create

import pygame
import math

from joblib.externals.loky.backend.utils import kill_process_tree

from engine.eventHandlers.inputHandlers.clickInputHandler import ClickInputHandler
from engine.eventHandlers.inputHandlers.movementInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler
from objects.entities.arrow import Arrow

from objects.entities.player import Player
from objects.entities.blue_slime import Blue_Slime
from objects.worldObjects.backGroundObject import BackgroundObject
from objects.worldObjects.collitionObject import CollitionObject
class Arena(Game):

    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        # this is the background asset which will be loaded as the background
        self.arena_path = "assets/environment/arena.png"

        self.screen_size = None

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
        self.create_enemies()

        self.eventHandler.add_event(self.kill_arrows_hitting_wall)

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

    def create_enemies(self):
        enemy = Blue_Slime(3, (0,0))
        self.eventHandler.add_event(self.update_enemies)

        self.entityObjects.append(enemy)


    def create_walls(self):
        self.worldObjects.append(CollitionObject(0,(0,0),(self.screen_size[0],100)))
        self.worldObjects.append(CollitionObject(0,(0,self.screen_size[1]-100),(self.screen_size[0],200)))
        self.worldObjects.append(CollitionObject(0, (0, 0), (100, self.screen_size[1])))
        self.worldObjects.append(CollitionObject(0, (self.screen_size[0]-100, 0), (100, self.screen_size[1])))

    def create_arrows(self, pos, angle):
        # Create the arrow with the calculated angle
        arrow = Arrow(3, pos, angle)
        self.eventHandler.add_event(arrow.update_movement)
        self.entityObjects.append(arrow)

    def update_enemies(self):
        player = self.get_entities_by_tag("player")[0]
        enemies = self.get_entities_by_tag("Enemy")

        for enemy in enemies:
            enemy.update_movement(player.get_pos())

    def check_collitions(self):
        walls = self.get_world_by_tag("wall")
        player = self.get_entities_by_tag("player")[0]
        # Loop all the walls and check if player is colliding with one of them?
        player.collition(False)
        for wall in walls:

            if wall.get_rect().colliderect(player.get_rect()):
                player.collition(True)
                
    def kill_arrows_hitting_wall(self):
        walls = self.get_world_by_tag("wall")
        arrows = self.get_entities_by_tag("arrow")

        for wall in walls:
            for arrow in arrows:
                if wall.get_rect().colliderect(arrow.get_rect()):
                    self.entityObjects.remove(arrow)