import pygame
from objects.objects.entityObject import EntityObject
class EnemyObject(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.add_tag("enemy")
        

    def inflict_damage(self, damage): # A method to inflict damage to a enemy.
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def heal(self, health): # A method to heal the enemy
        self.health += health
        self.health = min(self.health, self.maxHealth)
        

    def kill(self): # A method to kill the enemy. The enemy will then be removed next frame after getting the dead tag.
        self.add_tag("dead")
        self.healthbar.add_tag("dead")