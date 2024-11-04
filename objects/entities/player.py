import pygame
from pygame.display import update

from objects.objects.entityObject import EntityObject

class Player(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.vel = [0, 0]  # Initial velocity
        self.acc = [0.05, 0.05]
        self.velMax = [7, 7]  # Maximum velocity
        
        self.rect = (100,100)
        
        # sets the path to the player
        image_path = "assets/player/player.png"

        # load the player with given player asset
        self.surface =  pygame.image.load(image_path).convert_alpha()

    def update_movement(self, dir):
        self.pos = self.get_x() + dir[0] * self.getMaxVelX() , self.get_y() + dir[1] * self.getMaxVelY()

    def shoot(self, angle):
        self.create_arrow_call_back(self.get_pos(), angle)


    def object_create(self, call_back):
        self.create_arrow_call_back = call_back