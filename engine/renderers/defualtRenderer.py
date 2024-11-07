import pygame


# This render requiers each game object to exist with a level. So it knows in what order stuff are rendered.
class Renderer:

    def __init__(self) -> None:
        self.screen = None
        self.objects = None

    def set_screen(self, screen):
        self.screen = screen

    def set_objects(self, objects):
        self.objects = objects

    def render(self):
        screen_objects = self.objects[0] + self.objects[1]

        sorted_objects = sorted(screen_objects, key=lambda obj: obj.get_level())
        
        for render_object in sorted_objects:
            self.screen.blit(render_object.get_surface(), render_object.get_rect())
            
        

        pygame.display.update()