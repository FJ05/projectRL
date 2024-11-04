import pygame
import math
class ClickInputHandler():

    def __init__(self, call_back_function, object=None) -> None:
        self.call_back = call_back_function
        self.object = object
        self.pressed = False

    def process_input(self):
        if self.object is None:
            return
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0] and self.pressed == False:  # Left mouse button
            self.pressed = True
            mouse_pos = pygame.mouse.get_pos()
            dy = mouse_pos[1] - self.object.get_y()
            dx = mouse_pos[0] - self.object.get_x()

            # Calculate the angle to mouse, adjusted by 90 degrees
            angle = math.atan2(dy, dx)
            self.call_back(angle)
        elif mouse_buttons[0] == False and self.pressed == True:
            self.pressed = False


