import pygame
from pygame.display import update

from objects.objects.entityObject import EntityObject

class Blue_Slime(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.velMax = [5, 5]  # Maximum velocity
        self.colliding = False
        self.last_dir = (0,0)
        self.speed = 5
        # sets the path to the player
        self.image_path = "assets/player/player.png"
        rect = pygame.display.get_window_size()
        self.add_tag("Enemy")

        # load the player with given player asset
        self.surface =  pygame.image.load(self.image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (rect[0] / 16, rect[1] / 9))

    def update_movement(self, player_pos):
        
       # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player_pos[0] - self.get_x(),
                                      player_pos[1] - self.get_y())
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.pos = player_pos[0] + dirvect[0], player_pos[1] + dirvect[1]

    def collition(self, is_colliding):
        self.colliding = is_colliding

    def shoot(self, angle):
        self.create_arrow_call_back(self.get_pos(), angle)

    def object_create(self, call_back):
        self.create_arrow_call_back = call_back