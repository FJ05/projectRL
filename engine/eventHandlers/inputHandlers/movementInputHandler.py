import pygame
# this handler support wasd movement.
class InputHandler:

    # takes in a callback function and an entity
    def __init__(self, call_back_function, entity_object=None) -> None:
        self.call_back = call_back_function
        self.entity = entity_object

    # The function that will run each frame to process this event.
    def process_input(self):
        # return if the entity is not given
        if self.entity is None:
            return

        keys = pygame.key.get_pressed()  # Get the state of all keys

        # Initialize the direction as (0, 0)
        dir_x, dir_y = 0, 0

        # Vertical movement logic
        if keys[pygame.K_w] and not keys[pygame.K_s]:  # Move up if 'W' is pressed and 'S' is not
            dir_y = -1
        elif keys[pygame.K_s] and not keys[pygame.K_w]:  # Move down if 'S' is pressed and 'W' is not
            dir_y = 1

        # Horizontal movement logic
        if keys[pygame.K_d] and not keys[pygame.K_a]:  # Move right if 'D' is pressed and 'A' is not
            dir_x = 1
        elif keys[pygame.K_a] and not keys[pygame.K_d]:  # Move left if 'A' is pressed and 'D' is not
            dir_x = -1

        # Call the callback function with the new direction
        self.call_back((dir_x, dir_y))
