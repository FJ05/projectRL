from objects.objects.gameObject import GameObject
# A parent class for all worldobject
class WorldObject(GameObject):
    
    def __init__(self, level: int, pos: tuple) -> None:
        super().__init__(level, pos)
        self.level = level
        self.position = pos