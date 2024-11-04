import pygame
import math
from objects.objects.entityObject import EntityObject


class Arrow(EntityObject):

    def __init__(self, level: int, pos: tuple, angle):
        super().__init__(level, pos)
        self.velMax = [7, 7]  # Maximum velocity
        self.angle = angle
        self.rect = (20, 20)

        image_path = "assets/player/player.png"

        self.surface = pygame.image.load(image_path).convert_alpha()

    def update_movement(self):
        self.pos = self.get_x() + math.cos(self.angle) * self.getMaxVelX(), self.get_y() + math.sin(self.angle) * self.getMaxVelY()
