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

        image_path = "assets/player/player.png"

        self.surface =  pygame.image.load(image_path).convert_alpha()

    def update_movement(self, dir):
        self.pos = self.get_x() + dir[0] * self.getMaxVelX() , self.get_y() + dir[1] * self.getMaxVelY()

    def update_movement_vel(self, dir):
        self.pos = self.get_x() + dir[0] * self.getVelX(), self.get_y() + dir[1] * self.getVelY()

    def update_movement_acc(self, dir):
        if dir == (0,0):
            self.vel = (0,0)
            return
        print(self.vel)
        if self.getVelX() >= self.getMaxVelX() and self.getVelY() >= self.getMaxVelY():
            self.update_movement(dir)
        else:
            self.vel = self.getVelX() + self.getAccX(), self.getVelY() + self.getAccY()
            self.update_movement_vel(dir)

