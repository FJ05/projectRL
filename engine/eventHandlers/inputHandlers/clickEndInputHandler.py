import pygame
# This inputhandler exists to support click on text to end the game.
class EndInputHandler:

    # Takes in a callback function, normally the function that will be run if input is registered.
    # It also takes in an object, this is the object that is being interacted with, in this case clicked on.
    def __init__(self, call_back_function, object=None) -> None:
        self.call_back = call_back_function
        self.object = object


    # A function for the event process_input that's run every frame.
    def process_input(self):
        # Return if the object is none
        if self.object is None:
            return

        # Get mouse buttons
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()

            if self.object.rect.collidepoint(mouse_pos):  # Check if click is within rect bounds
                exit() # Exit python and therefor the game.
                

