import pygame
# this handler support click on text
class EndInputHandler:

    def __init__(self, call_back_function, object=None) -> None:
        self.call_back = call_back_function
        self.object = object

    def process_input(self):
        if self.object is None:
            return

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()

            if self.object.rect.collidepoint(mouse_pos):  # Check if click is within rect bounds
                exit()
                

