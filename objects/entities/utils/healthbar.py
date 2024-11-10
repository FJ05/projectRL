import pygame
from objects.objects.gameObject import GameObject

# This class is for displaying the heath of entities
class Healthbar(GameObject):
    # init with a pos and level
    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        # Set no rect for now
        self.rect = None
        self.maxSize = 100 # Set its max size in pixels
        self.size = 100 # Set its starting size
        self.add_tag("healthbar")
        self.create_surface()

    def calculate_lenght(self, health, maxHealth):
        ratio = health / maxHealth # get the ratio between health and maxHealth
        self.size = min(self.maxSize,self.maxSize * ratio) # Make the size cap at max size. # This is made so the health bar isn't super longs when wired health and max health ratio combines into play like when testing.
        self.create_surface() # Recreate the surface


    def create_surface(self):
        self.rect = (max(0.001,self.size),10) # make it so the rect is never 0 in x.
        self.surface = pygame.Surface(self.rect)
        self.surface.fill((0,255,0))
