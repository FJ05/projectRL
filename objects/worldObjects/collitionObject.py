import pygame
from objects.objects.worldObject import WorldObject

class CollitionObject(WorldObject):

    def __init__(self, level: int, pos: tuple, rect: tuple) -> None:
        super().__init__(level, pos)
        self.add_tag("wall")
        self.rect = rect

        self.surface = pygame.Surface(self.rect)
        # This will be under here will be removed or the same will be in effect if level is changed.
        