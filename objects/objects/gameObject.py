class GameObject:

    def __init__(self, level: int, pos: tuple) -> None:
        self.level = level
        self.pos = pos

    def get_level(self):
        return self.level if not self.level < 0 else 0
    
    def get_rect(self):
        rect = self.surface.get_rect()
        rect.topleft = self.pos
        return rect
    
    def get_surface(self):
        return self.surface

    def get_pos(self):
        return self.pos

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]
