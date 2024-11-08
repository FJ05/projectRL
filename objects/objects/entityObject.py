import time
from objects.objects.gameObject import GameObject
class EntityObject(GameObject):

    def __init__(self, level: int, pos: tuple) -> None:
        super().__init__(level, pos)
        self.health = 1000000 # This thinks that health should normaly be
        self.maxHealth = 1000000
        self.damage_cooldown = 0.0 # Number in seconds
        self.damage = 0
        self.reach = 0
        self.acc = (0,0)
        self.vel = (0,0)
        self.velMax = (0,0)
        self.start_time = 0
        self.damaged = False

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

    def get_speed(self):
        return (self.velMax[0]**2 + self.velMax[1]**2)**0.5

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def set_damage(self, damage):
        self.damage = damage

    def get_damage(self):
        return self.damage
    
    def set_damage_cooldown(self, cooldown):
        self.damage_cooldown = cooldown

    def get_damage_cooldown(self):
        return self.damage_cooldown
    
    def set_reach(self, reach):
        self.reach = reach

    def get_reach(self):
        return self.reach
    
    def set_on_damage_cooldown(self, bool):
        self.damaged = bool
        self.start_time = time.time()

    def check_damage_cooldown(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.get_damage_cooldown():
            self.set_on_damage_cooldown(False)
