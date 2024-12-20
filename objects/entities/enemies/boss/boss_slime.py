import pygame
import time
import math

from objects.objects.enemyObject import EnemyObject
from objects.entities.enemies.boss.slime_ball import Slime_ball

# A class for the mini boss
class Boss_Slime(EnemyObject):

    # Initiate its damage and pos and level
    def __init__(self, level: int, pos: tuple, damage, health, reach, wave):
        super().__init__(level, pos)
        self.velMax = [0.5, 0.5]  # Maximum velocity
        self.image_path = "assets/mobs/boss_slime.png" #  the sprite
        rect = pygame.display.get_window_size()
        self.add_tag("boss_slime")
        self.set_health(health)
        self.set_maxHealth(health)
        self.set_damage(damage)
        self.set_reach(reach)
        # load the slime with given enemy asset
        self.surface =  pygame.image.load(self.image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (rect[0] / 16, rect[1] / 9))

        # varibles to track its last attack and attack speed.
        self.last_attack = 0
        self.attack_speed = 0.8 - wave*0.01 # How often the boss can attack

    def update_movement(self, player_pos): # Updates movement of slime as a vector towards player position
        
        dy = player_pos[1] - self.get_y() + 40
        dx = player_pos[0] - self.get_x() + 40

        # Calculate the angle to mouse or the dir the boss will move
        angle = math.atan2(dy, dx)


        self.attack(angle) # Attack the player with the calculated angle

       # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player_pos[0] - self.get_x(),
                                      player_pos[1] - self.get_y())
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length((self.velMax[0]**2 + self.velMax[1]**2)**0.5)
        self.pos = self.get_x() + dirvect[0], self.get_y() + dirvect[1]


    # A method to attack / send a slimeball with a specified angle
    def attack(self, angle):
        # First it calculates if the elapsed time since and attack is more then the cooldown
        elapsed_time = time.time() - self.last_attack

        if elapsed_time >= self.attack_speed:
            # Spawn the slimebal
            slimeball = Slime_ball(3, (self.pos[0] + (self.get_size()[0]/2), self.pos[1] + (self.get_size()[1]/2)), angle, (self.damage / 2))
            self.spawn_function(slimeball)
            self.last_attack = time.time()

    # A method to set the functon with the boss can spawn enemies. The method exist in arena game.
    def set_spawn_function(self, function):
        self.spawn_function = function
