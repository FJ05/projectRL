import pygame
import math
import random

from objects.objects.entityObject import EntityObject

class Bouncy_Slime_ball(EntityObject):

    def __init__(self, level: int, pos: tuple, angle, damage = 10):
        super().__init__(level, pos)
        self.velMax = [3, 3]  # Velocity of arrow
        self.angle = angle
        self.rect = pygame.display.get_window_size() # size of the window for correct scaling
        self.add_tag("bouncy_slimeball")
        self.add_tag("projectile")
        self.bounces = 0
        self.set_damage(damage)
        rect = pygame.display.get_window_size()
        sound = pygame.mixer.Sound("sounds/entity_sounds/arrow.mp3")
        image_path = "assets/objects/slimeball.png"

        self.surface = pygame.image.load(image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, ((rect[0] / 16) / 5, (rect[1] / 9))) # for scaling the image to it's correct size
        transform_angle = math.degrees(-self.angle) - 90 #This is the angle the arrow is traveling at

        self.surface = pygame.transform.rotate(self.surface, transform_angle)
        
        pygame.mixer.Sound.play(sound)

    def update_movement(self, hitting):
        if self.bounces >= 7:
            self.add_tag("dead")

        x = self.get_x()
        y = self.get_y()

        if hitting:

            x -= math.cos(self.angle) * self.getMaxVelX()
            y -= math.sin(self.angle) * self.getMaxVelY()

            self.angle = self.angle - (math.pi/2)
            self.bounces += 1
        else:
            x += math.cos(self.angle) * self.getMaxVelX()
            y += math.sin(self.angle) * self.getMaxVelY()


        self.pos = (x,y)