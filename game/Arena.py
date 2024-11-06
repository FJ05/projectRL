from venv import create

import pygame
import math


from engine.eventHandlers.inputHandlers.clickInputHandler import ClickInputHandler
from engine.eventHandlers.inputHandlers.movementInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler
from objects.entities.arrow import Arrow

from objects.entities.player import Player
from objects.entities.enemies.blue_slime import Blue_Slime
from objects.worldObjects.backGroundObject import BackgroundObject
from objects.worldObjects.collitionObject import CollitionObject
class Arena(Game):
    
    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        self.arena_path = "assets/environment/arena.png"
        self.screen_size = None

    def run(self):
        self.eventHandler.process_events()
        self.renderer.render()

    def create_objects(self):
        self.screen_size = pygame.display.get_window_size() # Get screen size
        self.setup_background()
        self.setup_walls()
        self.setup_player()
        self.setup_enemies()
        self.setup_events()

    def setup_background(self): # Skapa Bakrunden
        background_img = pygame.image.load(self.arena_path).convert()
        background = BackgroundObject(1, (0, 0), (255, 255, 255), self.screen_size, image=background_img)
        self.worldObjects.append(background)

    def setup_player(self): #Skapa spelaren och dess inputhandlers
        player_position = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        player = self.initialize_player(player_position)
        input_handler, attack_handler = self.initialize_input_handlers(player)
        self.entityObjects.append(player)
        
        # Register events and or inputhandlers
        self.eventHandler.add_event(self.check_collisions)
        self.eventHandler.add_event(input_handler.process_input)
        self.eventHandler.add_event(attack_handler.process_input)

    def initialize_player(self, position):
        player = Player(3, position)
        player.add_tag("player")
        player.object_create(self.create_arrow)
        return player

    def initialize_input_handlers(self, player):
        input_handler = InputHandler(player.update_movement, player)
        attack_handler = ClickInputHandler(player.shoot, player)
        return input_handler, attack_handler

    def setup_enemies(self):
        enemy = Blue_Slime(3, (0, 0))
        self.entityObjects.append(enemy)
        self.eventHandler.add_event(self.update_enemies)

    def setup_walls(self):
        wall_positions = [
            (0, 0, self.screen_size[0], 100),  # Top
            (0, self.screen_size[1] - 100, self.screen_size[0], 100),  # Bottom
            (0, 0, 100, self.screen_size[1]),  # Left
            (self.screen_size[0] - 100, 0, 100, self.screen_size[1])  # Right
        ]
        for pos in wall_positions:
            wall = CollitionObject(0, pos[:2], pos[2:])
            wall.add_tag("wall")
            self.worldObjects.append(wall)

    def setup_events(self):
        # Registers all the game events for cleaner code separation
        self.eventHandler.add_event(self.arrows_hitting_enemies)
        self.eventHandler.add_event(self.kill_arrows_hitting_wall)
        self.eventHandler.add_event(self.remove_dead_enemies)

    # Event methods
    def update_enemies(self):
        player = self.get_entities_by_tag("player")[0]
        enemies = self.get_entities_by_tag("enemy")
        for enemy in enemies:
            enemy.update_movement(player.get_pos())

    def check_collisions(self):
        player = self.get_entities_by_tag("player")[0]
        walls = self.get_world_by_tag("wall")
        
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
                    if self.entityObjects.count(arrow) <= 0:
                        continue # Skip Arrows that do not actually exist in the list. Or that has already been removed.

                    self.entityObjects.remove(arrow)

    def remove_dead_enemies(self):
        dead_entities = self.get_entities_by_tag("dead")
        for entity in dead_entities:
            self.entityObjects.remove(entity)

    def arrows_hitting_enemies(self):
        enemies = self.get_entities_by_tag("enemy")
        arrows = self.get_entities_by_tag("arrow")
        
        for enemy in enemies:
            for arrow in arrows:
                if enemy.get_rect().colliderect(arrow.get_rect()):
                    enemy.inflict_damage(arrow.get_damage())
                    self.entityObjects.remove(arrow)

    # Helper methods
    def create_arrow(self, pos, angle):
        arrow = Arrow(3, pos, angle)
        arrow.add_tag("arrow")
        self.eventHandler.add_event(arrow.update_movement)
        self.entityObjects.append(arrow)
