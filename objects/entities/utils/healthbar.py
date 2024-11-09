import pygame
from objects.objects.gameObject import GameObject


class Healthbar(GameObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)

        self.rect = None
        self.maxSize = 100 # px
        self.size = 100
        self.add_tag("healthbar")
        self.create_surface()

    def calculate_lenght(self, health, maxHealth):
        ratio = health / maxHealth
        self.size = min(100,self.maxSize * ratio)
        self.create_surface()


    def create_surface(self):
        self.rect = (max(0.001,self.size),10)
        self.surface = pygame.Surface(self.rect)
        self.surface.fill((0,255,0))
