import pygame

from objects.objects.enemyObject import EnemyObject

class Green_Slime(EnemyObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.velMax = [4, 4]  # Maximum velocity
        self.image_path = "assets/objects/arrow.png"
        rect = pygame.display.get_window_size()
        self.add_tag("green_slime")
        self.set_health(10)
        self.set_damage(40)
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

    def collition(self, is_colliding):
        self.colliding = is_colliding

    def shoot(self, angle):
        self.create_arrow_call_back(self.get_pos(), angle)

    def object_create(self, call_back):
        self.create_arrow_call_back = call_back