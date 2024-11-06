import pygame
from objects.objects.gameObject import GameObject
class EntityObject(GameObject):

    def __init__(self, level: int, pos: tuple) -> None:
        super().__init__(level, pos)
        self.health = 1000000 # This thinks that health should normaly be
        self.damage = 0
        self.acc = (0,0)
        self.vel = (0,0)
        self.velMax = (0,0)

    def getVelX(self):
        return self.vel[0]

    def getVelY(self):
        return self.vel[1]

    def getMaxVelX(self):
        return self.velMax[0]

    def getMaxVelY(self):
        return self.velMax[1]

    def getAccX(self):
        return self.acc[0]

    def getAccY(self):
        return self.acc[1]

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def set_damage(self, damage):
        self.damage = damage

    def get_damage(self):
        return self.damage