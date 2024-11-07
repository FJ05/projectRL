import pygame
import math


from engine.eventHandlers.inputHandlers.clickInputHandler import ClickInputHandler
from engine.eventHandlers.inputHandlers.movementInputHandler import InputHandler
from engine.game.Game import Game
from engine.renderers.defualtRenderer import Renderer
from engine.eventHandlers.defualtEventHandler import EventHandler
from objects.entities.arrow import Arrow
from game.WaveController import Controller

from objects.entities.player import Player
from objects.entities.enemies.blue_slime import Blue_Slime
from objects.entities.enemies.green_slime import Green_Slime
from objects.worldObjects.backGroundObject import BackgroundObject
from objects.worldObjects.collitionObject import CollitionObject
from objects.worldObjects.textObject import TextObject

class Arena(Game):
    
    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        self.arena_path = "assets/environment/arena.png"
        self.screen_size = None
        self.score = 0

    def run(self):
        self.eventHandler.process_events()
        self.renderer.render()
        # Adds the score to the world
        self.update_score()

    def reset(self):
        self.__init__()

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
        enemy_list = [Blue_Slime(0,(0,0)), Green_Slime(0,(0,0))] # The list of enemies that can spawn
        contoller = Controller(self.spawn_enemy, self.get_enemy_count, enemy_list) # The controller that spawns enemies when condition is right.
        self.eventHandler.add_event(contoller.spawn)
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
        self.eventHandler.add_event(self.damage_player)

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
            self.score += 10 # Adds 10 score for each kill
            self.update_score() # updates the score
            self.entityObjects.remove(entity)

    def arrows_hitting_enemies(self):
        enemies = self.get_entities_by_tag("enemy")
        arrows = self.get_entities_by_tag("arrow")
        
        for enemy in enemies:
            for arrow in arrows:
                if enemy.get_rect().colliderect(arrow.get_rect()):
                    enemy.inflict_damage(arrow.get_damage())
                    if self.entityObjects.count(arrow) <= 0:
                        continue # Skip Arrows that do not actually exist in the list. Or that has already been removed.
                    self.entityObjects.remove(arrow)

    def damage_player(self):
        player = self.get_entities_by_tag("player")[0]
        enemies = self.get_entities_by_tag("enemy")
        if player.health <= 0:
            self.exit_game()

        for enemy in enemies:
            d = math.dist(player.get_pos(), enemy.get_pos())
            if d <= enemy.get_reach() and player.damaged == False:
                player.health -= enemy.get_damage()
                player.set_on_damage_cooldown(True)
            else:
                player.check_damage_cooldown()
            

    # Helper methods
    def create_arrow(self, pos, angle):
        arrow = Arrow(3, pos, angle)
        arrow.add_tag("arrow")
        self.eventHandler.add_event(arrow.update_movement)
        self.entityObjects.append(arrow)

    def spawn_enemy(self, enemy):
        self.entityObjects.append(enemy)

    def get_enemy_count(self):
        enemies = self.get_entities_by_tag("enemy")
        return len(enemies)
    
    def update_score(self):
        # Updates the score text with the current score
        size = pygame.display.get_window_size()
        score_text_str = str(self.score)
        
        # Graphics for the score
        score_text = TextObject(4, (size[0] / 2, size[1] / 11), f"Score: {score_text_str}", 30, (255, 255, 255))
        score_text.add_tag("Score")

        scores = self.get_world_by_tag("Score")
        # Removes the past score if there is a score to update
        if self.score != 0:
            for score in scores:
                self.worldObjects.remove(score)
        
        # Adds the current score to Arena
        self.worldObjects.append(score_text)