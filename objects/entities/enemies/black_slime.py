import pygame

from objects.objects.enemyObject import EnemyObject

class Black_Slime(EnemyObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.velMax = [2, 2]  # Maximum velocity
        self.image_path = "assets/mobs/black_slime.png"
        rect = pygame.display.get_window_size()
        self.add_tag("black_slime")
        self.set_health(120)
        self.set_maxHealth(120)
        self.set_damage(25)
        self.set_reach(10)
        # load the slime with given enemy asset
        self.surface =  pygame.image.load(self.image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (rect[0] / 16, rect[1] / 9))

    def update_movement(self, player_pos): # Updates movement of slime as a vector towards player position
        
       # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player_pos[0] - self.get_x(),
                                      player_pos[1] - self.get_y())
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length((self.velMax[0]**2 + self.velMax[1]**2)**0.5)
        self.pos = self.get_x() + dirvect[0], self.get_y() + dirvect[1]