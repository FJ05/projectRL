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
from objects.entities.enemies.black_slime import Black_Slime
from objects.entities.enemies.pink_slime import Pink_Slime
from objects.worldObjects.backGroundObject import BackgroundObject
from objects.worldObjects.collitionObject import CollitionObject
from objects.worldObjects.textObject import TextObject


# This class is for the main game.
class Arena(Game):
    # Create class with new eventhandlers and render.
    def __init__(self):
        super().__init__(EventHandler(), Renderer())
        # Set the bakground asset for the arena
        self.arena_path = "assets/environment/arena.png"
        self.screen_size = None
        self.score = 0

    # The run method to run each process each frame.
    def run(self):
        self.eventHandler.process_events()
        self.renderer.render()

    # A method to reset the game just init the object to original state
    def reset(self):
        self.__init__()

    # A method to create all objects needed before the game is actually running
    def create_objects(self):
        self.screen_size = pygame.display.get_window_size() # Get screen size
        self.setup_player()
        self.setup_enemies()
        self.setup_events()

        self.setup_arena()
        self.setup_walls()

    # A method that setups the arena like bakground
    def setup_arena(self):
        # Create the bakground
        background_img = pygame.image.load(self.arena_path).convert()
        background = BackgroundObject(1, (0, 0), (255, 255, 255), self.screen_size, image=background_img)
        self.worldObjects.append(background)

        # Graphics for the score
        score_text = TextObject(4, (self.screen_size[0] / 1.2, self.screen_size[1] / 11), f"Score: {self.score}", 30, (255, 255, 255))
        score_text.add_tag("Score")
        self.worldObjects.append(score_text)

        # Graphics for the wave
        wave_text = TextObject(4, (self.screen_size[0] / 1.2, self.screen_size[1] / 8), f"Wave: ?", 30, (255, 255, 255))
        wave_text.add_tag("wave")
        self.worldObjects.append(wave_text)

        # Graficx for controll text
        controlls = TextObject(4, (40, self.screen_size[1] / 11), f"Controlls: WASD + Left Click", 30, (255, 255, 255))
        controlls.add_tag("controlls")
        self.worldObjects.append(controlls)

    # A method to create the player and its handlers
    def setup_player(self):
        player_position = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        player = self.initialize_player(player_position)
        # Set the player controller so we can use it to change sprite.
        self.player_controller = player
        input_handler, attack_handler = self.initialize_input_handlers(player)
        self.entityObjects.append(player)
        
        # Register events and or inputhandlers for player
        self.eventHandler.add_event(self.check_collisions)
        self.eventHandler.add_event(input_handler.process_input)
        self.eventHandler.add_event(attack_handler.process_input)
    # Creates the player and returns it.
    def initialize_player(self, position):
        player = Player(3, position)
        player.add_tag("player")
        player.object_create(self.create_arrow)
        return player
    # Create the player inputhandlers
    def initialize_input_handlers(self, player):
        input_handler = InputHandler(player.update_movement, player)
        attack_handler = ClickInputHandler(player.shoot, player)
        return input_handler, attack_handler

    # Creates the controller with a list of the Enemies we want to exist in the game currently
    def setup_enemies(self):
        enemy_list = [Blue_Slime(0,(0,0)), Green_Slime(0,(0,0)),Black_Slime(0,(0,0)),Pink_Slime(0,(0,0))] # The list of enemies that can spawn
        contoller = Controller(self.spawn_enemy, self.get_enemy_count, enemy_list) # The controller that spawns enemies when condition is right.
        contoller.set_update_wave(self.update_wave)
        # Add the event that work with enemies.
        self.eventHandler.add_event(contoller.spawn)
        self.eventHandler.add_event(self.update_enemies)
        self.eventHandler.add_event(self.update_bouncy_slimeball)
    # Create the walls
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
        self.eventHandler.add_event(self.damage_player)
        self.eventHandler.add_event(self.update_healthbars)
        self.eventHandler.add_event(self.remove_dead_enemies)
        self.eventHandler.add_event(self.update_score)

    # Event methods / function
    def update_enemies(self):
        player = self.get_entities_by_tag("player")[0]
        enemies = self.get_entities_by_tag("enemy")
        # for each enemy update thier movement based on where the player is
        for enemy in enemies:
            enemy.update_movement(player.get_pos())
        # update the slimeballs that move.
        slimeballs = self.get_entities_by_tag("slimeball")
        for slimeball in slimeballs:
            slimeball.update_movement()
    # A sepetete method to handle the bouncy slimeballs and when they hit a wall
    def update_bouncy_slimeball(self):
        slimeballs = self.get_entities_by_tag("bouncy_slimeball")
        walls = self.get_world_by_tag("wall")
        # loop all slimeballs and walls to find if they collide / hit
        for slimeball in slimeballs:
            for wall in walls:
                if wall.get_rect().colliderect(slimeball.get_rect()):
                    slimeball.update_movement(True)
                else:
                    slimeball.update_movement(False)

    # check for collitions between player and walls
    def check_collisions(self):
        player = self.get_entities_by_tag("player")[0]
        walls = self.get_world_by_tag("wall")
        
        player.collition(False)
        for wall in walls:
            if wall.get_rect().colliderect(player.get_rect()):
                player.collition(True)

    # Loop all entiies tthat should be killed on wall collide
    def kill_arrows_hitting_wall(self):
        walls = self.get_world_by_tag("wall")
        arrows = self.get_entities_by_tag("arrow")
        slimeballs = self.get_entities_by_tag("slimeball")
        arrows += slimeballs
        for wall in walls:
            for arrow in arrows:
                if wall.get_rect().colliderect(arrow.get_rect()):
                    if self.entityObjects.count(arrow) <= 0:
                        continue # Skip Arrows that do not actually exist in the list. Or that has already been removed.

                    self.entityObjects.remove(arrow)
    # Remove all enemies with the dead tag
    def remove_dead_enemies(self):
        dead_entities = self.get_entities_by_tag("dead")
        for entity in dead_entities:
            tags = entity.get_tags()

            self.score += 10 # Adds 10 score for each kill
            self.update_score() # updates the score
            self.entityObjects.remove(entity)
            # If the entity looped over was the final boss end the game with a win.
            if tags.count("final_boss_slime"):
                self.exit_game({"next_game": 1,
                                "reason": "YOU WIN",
                                "score": self.score})
                return

    # Damage enemies.
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

    # Damage player
    def damage_player(self,):
        player = self.get_entities_by_tag("player")[0]
        enemies = self.get_entities_by_tag("enemy")
        projectiles = self.get_entities_by_tag("projectile")
        enemies += projectiles
        # If player has no health the game is lost/ ended.
        if player.health <= 0:
            self.exit_game({"next_game": 1,
                                "reason": "You Loose",
                                "score": self.score})

        for enemy in enemies:
            d = math.dist(player.get_pos(), enemy.get_pos())
            if (d <= enemy.get_reach() or enemy.get_rect().colliderect(player.get_rect())) and player.damaged == False:
                player.health -= enemy.get_damage()
                self.player_controller.stun_sprite() # Stun the sprite when getting hit. This means shot that it been hit,
                player.set_on_damage_cooldown(True)
            else:
                player.check_damage_cooldown()
                    
    # Update healthbars so move so they exist over entties and also update thier length based on health
    def update_healthbars(self):
        entities = self.get_entities_by_tag("enemy")
        entities += self.get_entities_by_tag("player")

        for entity in entities:
            entity.update_healthbar()
            if self.entityObjects.count(entity.healthbar) <= 0 and entity.healthbar is not None:
                self.entityObjects.append(entity.healthbar)

    # Helper methods

    def create_arrow(self, pos, angle):
        self.player_controller.sprite()
        ####################################
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

        # Gets the score text
        scores = self.get_world_by_tag("Score")
        
        # Sets it text to be the new score
        for score in scores:
            score.set_text(f"Score: {self.score}")

    def update_wave(self, wave_int):
        # Updates the wave text with the current score

        # Gets the wave text
        waves = self.get_world_by_tag("wave")
        
        # Sets it text to be the new wave
        for wave in waves:
            wave.set_text(f"Wave: {wave_int}")