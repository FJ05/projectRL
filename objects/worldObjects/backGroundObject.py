import pygame
from objects.objects.worldObject import WorldObject

class BackgroundObject(WorldObject):

    def __init__(self, level: int, pos: tuple, color: tuple = (0, 0, 0), rect: tuple = (800, 600), image=None) -> None:
        super().__init__(level, pos)
        self.color = color
        self.rect = rect  #size of the background
        self.image = image
        self.create_color()

    def create_image(self):
        pass

    def get_surface(self):
        return self.image if self.image else self.surface  # return the image if available, otherwise the color surface
    
    def get_rect(self):
        if self.image:
            return self.image.get_rect(topleft=self.position)  # use the image’s rect with the top-left position
        else:
            return pygame.Rect(*self.position, *self.rect)  # yse self.rect as size if no image is provided

    def get_level(self):
        return self.level  # return the level to control render order

    def create_color(self):
        # create a surface filled with the specified color if no image is given
        self.surface = pygame.Surface(self.rect)
        self.surface.fill(self.color)
