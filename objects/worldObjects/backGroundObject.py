from socket import create_connection

import pygame.draw

from objects.objects.worldObject import WorldObject

class BackgroundObject(WorldObject):

    def __init__(self, level: int, pos: tuple, color: tuple, rect: tuple) -> None:
        super().__init__(level, pos)
        self.color = color
        self.rect = rect

        self.create_color()

    def create_image(self):
        pass

    def create_color(self):
        # Create a color only Piece
        self.surface = pygame.Surface(self.rect)
        self.surface.fill(self.color)

