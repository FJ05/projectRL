from objects.objects.gameObject import GameObject
class WorldObject(GameObject):
    
    def __init__(self, level: int, pos: tuple) -> None:
        super().__init__(level, pos)
        self.level = level
        self.position = pos