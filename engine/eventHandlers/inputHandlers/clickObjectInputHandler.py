import pygame
# This inputhandler exists to support click on text to change the game to a new one.
# This means hopping between diffrent games. Check manager.py or Systemskiss.
class InputHandler:

    # Takes in a callback function, normally the function that will be run if input is registered.
    # It also takes in an object, this is the object that is being interacted with, in this case clicked on.
    def __init__(self, call_back_function, object=None) -> None:
        self.call_back = call_back_function
        self.object = object
        # A sound to be played when swithing games.
        self.click_sound = pygame.mixer.Sound("sounds/menu/button_click.mp3")

    # A function for the event process_input that's run every frame.
    def process_input(self):
        # Return if no object has been given
        if self.object is None:
            return

        # Get mouse buttons
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()

            if self.object.rect.collidepoint(mouse_pos):  # Check if click is within rect bounds
                # play sound
                pygame.mixer.Sound.play(self.click_sound)
                # Get how many games are to skip. If the skip is higher than index of games it will start over due to mod
                skip = self.object.skip
                # Call the call back with end game data.
                self.call_back({"next_game": skip, "reason":"Start Game", "score": 0})
                

