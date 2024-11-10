import pygame
import time
import math

from objects.objects.enemyObject import EnemyObject
from objects.entities.enemies.boss.bounce_slime_ball import Bouncy_Slime_ball
# a class for the final boss
class Final_Boss_Slime(EnemyObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.velMax = [0.5, 0.5]  # Maximum velocity
        self.image_path = "assets/mobs/boss.png"
        self.rect = pygame.display.get_window_size()
        self.add_tag("final_boss_slime")
        self.set_health(2000)
        self.set_maxHealth(2000)
        self.set_damage(50)
        self.set_reach(20)
        # load the slime with given enemy asset
        self.surface =  pygame.image.load(self.image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.rect[0] / 16 / 2, self.rect[1] / 9))

        # varibles to track its last attack and attack speed.
        self.last_attack = 0
        self.attack_speed = 1

    def update_movement(self, player_pos): # Updates movement of slime as a vector towards player position

        dy = player_pos[1] - self.get_y() + 40
        dx = player_pos[0] - self.get_x() + 40

        # Calculate the angle to mouse, adjusted by 90 degrees
        angle = math.atan2(dy, dx)


        self.attack(angle) # Attack the player with the calculated angle

       # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player_pos[0] - self.get_x(),
                                      player_pos[1] - self.get_y())
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length((self.velMax[0]**2 + self.velMax[1]**2)**0.5)
        self.pos = self.get_x() + dirvect[0], self.get_y() + dirvect[1]



    def attack(self, angle):
        # Check if an attack can be done, meaning It's not in cooldown
        elapsed_time = time.time() - self.last_attack

        if elapsed_time >= self.attack_speed:
            # Spawn the bouncy slimeball
            slimeball = Bouncy_Slime_ball(3, (self.pos[0] + (self.get_size()[0]/2), self.pos[1] + (self.get_size()[1]/2)), angle, (self.damage / 2), )
            self.spawn_function(slimeball)
            self.last_attack = time.time() # update last attack


    # A method to set the functon with the boss can spawn enemies. The method exist in arena game.
    def set_spawn_function(self, function):
        self.spawn_function = function