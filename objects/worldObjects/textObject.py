import pygame

from objects.objects.worldObject import WorldObject

class TextObject(WorldObject):

    def __init__(self, level : int, pos : tuple, text: str, size: int, textColor: tuple, backgroundColor : tuple = None) -> None:
        super().__init__(level, pos)
        self.backgroundColor = None
        self.textColor = None
        self.size = None
        self.text = None
        self.create_text(text, size, textColor, backgroundColor)

    def create_text(self, text : str, size : int, textColor: tuple, backgroundColor : tuple = (255,255,255)) -> None:
        self.text = text
        self.size = size
        self.textColor = textColor
        self.backgroundColor = backgroundColor

        self.font = pygame.font.Font('freesansbold.ttf', self.size)

        self.surface = self.font.render(self.text, True, self.textColor, self.backgroundColor)
        self.rect = self.get_rect()

    def set_text(self, text: str):
        self.text = text
        self.surface = self.font.render(text, True, self.textColor, self.backgroundColor)
        self.rect = self.get_rect()


