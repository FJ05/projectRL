import pygame
# this handler support wasd movement.
class InputHandler:

    def __init__(self, call_back_function, entity_object=None) -> None:
        self.call_back = call_back_function
        self.entity = entity_object

    def process_input(self):
        if self.entity is None:
            return

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()
            print("Rect:",self.entity.get_rect())
            print("Pos: ",self.entity.pos)
            if self.entity.rect.collidepoint(mouse_pos):  # Check if click is within rect bounds
                print("Clicked start")
                self.call_back()

