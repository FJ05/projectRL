import pygame


# This render requiers each game object to exist with a level. So it knows in what order stuff are rendered.
class Renderer:

    def __init__(self) -> None:
        self.screen = None
        self.objects = None
    # A mehod to set what screen the render should render onto
    def set_screen(self, screen):
        self.screen = screen
    # A method to give the renderer the object it should render
    def set_objects(self, objects):
        self.objects = objects
    # The method run each fram that renders objects onto the screen
    def render(self):
        # Get all objects and combineds them to one list.
        screen_objects = self.objects[0] + self.objects[1]
        # Sorts them by thier level. level meaning order they should be renderd.
        sorted_objects = sorted(screen_objects, key=lambda obj: obj.get_level())
        # Render them in that order by looping and bliting them to the screen
        for render_object in sorted_objects:
            self.screen.blit(render_object.get_surface(), render_object.get_rect())
            
        
        # update the screen
        pygame.display.update()