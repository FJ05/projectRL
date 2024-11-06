import pygame
import math
from objects.objects.entityObject import EntityObject


class Arrow(EntityObject):

    def __init__(self, level: int, pos: tuple, angle):
        super().__init__(level, pos)
        self.velMax = [15, 15]  # Velocity of arrow
        self.angle = angle
        self.rect = pygame.display.get_window_size() # size of the window for correct scaling
        self.add_tag("arrow")

        rect = pygame.display.get_window_size()
        image_path = "assets/objects/arrow.png"

        self.surface = pygame.image.load(image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (((rect[0] / 16) / 3) / 5, (rect[1] / 9) / 5)) # for scaling the image to it's correct size
        transform_angle = math.degrees(-self.angle) - 90 #This is the angle the arrow is traveling at

        self.surface = pygame.transform.rotate(self.surface, transform_angle)

    def update_movement(self):
        self.pos = self.get_x() + math.cos(self.angle) * self.getMaxVelX(), self.get_y() + math.sin(self.angle) * self.getMaxVelY()
