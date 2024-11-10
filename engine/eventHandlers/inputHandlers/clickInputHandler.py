import pygame
import math
# This is an inputhandler that handlers when the user clicked.
# It also is the function that inits the shoot arrows function sequence.
class ClickInputHandler():

    # Takes in a callback function, normally the function that will be run if input is registered.
    # It also takes in an object, this is the object that is being interacted with, in this the click.
    def __init__(self, call_back_function, object=None) -> None:
        self.call_back = call_back_function
        self.object = object
        self.pressed = False

    # A function for the event process_input that's run every frame.
    def process_input(self):
        # Return if no object has been given
        if self.object is None:
            return
        # Get mouse button
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0] and self.pressed == False:  # Left mouse button and that pressed is falls.
            # Setting pressed to true so holding in mouse click does not work you have to click.
            self.pressed = True
            # Get angle between the mouse and the object given(probably the player)
            mouse_pos = pygame.mouse.get_pos()
            dy = mouse_pos[1] - self.object.get_y()
            dx = mouse_pos[0] - self.object.get_x()

            # Calculate the angle to mouse in radians
            angle = math.atan2(dy, dx)

            self.call_back(angle)
        # If the mouse button is not presses set self.pressed to falls.
        elif mouse_buttons[0] == False and self.pressed == True:
            self.pressed = False


