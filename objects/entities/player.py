import pygame
from pygame.display import update

from objects.objects.entityObject import EntityObject

class Player(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.velMax = [7, 7]  # Maximum velocity
        self.colliding = False
        self.last_dir = (0,0)
        # sets the path to the player
        self.image_path = "assets/player/player.png"
        rect = pygame.display.get_window_size()

        # load the player with given player asset
        self.surface =  pygame.image.load(self.image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (rect[0] / 16, rect[1] / 9))

    def update_movement(self, dir):
        
        x, y = self.get_x(), self.get_y()
        vel_x, vel_y = self.getMaxVelX(), self.getMaxVelY()

        if self.colliding:
            # Revert last frames movement into wall
            x -= self.last_dir[0] * vel_x
            y -= self.last_dir[1] * vel_y

            # Only update position in the direction away from last dir
            if dir[0] != -self.last_dir[0]:  # Allow movement only away or along x-axis
                x += dir[0] * vel_x
            if dir[1] != -self.last_dir[1]:  # Allow movement only away or along y-axis
                y += dir[1] * vel_y

        else:
            # Normal movement if not colliding
            x += dir[0] * vel_x
            y += dir[1] * vel_y

        # Update position and last direction
        self.pos = (x, y)
        self.last_dir = dir



    def collition(self, is_colliding):
        self.colliding = is_colliding

    def shoot(self, angle):
        self.create_arrow_call_back(self.get_pos(), angle)

    def object_create(self, call_back):
        self.create_arrow_call_back = call_back