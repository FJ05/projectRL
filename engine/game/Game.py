class Game:

    def __init__(self, eventHandler, renderer):
        self.exit_game = None

        self.eventHandler = eventHandler
        self.renderer = renderer
        self.entityObjects = []
        self.worldObjects = []

    def get_game_objects(self):
        return self.entityObjects, self.worldObjects

        # This
    def create_objects(self):
        print("No initial object exist for this game")

    def set_exit_game(self, exit_game_call_back):
        self.exit_game = exit_game_call_back

    def get_entities_by_tag(self, tag: str):

        entities = []
        for entity in self.entityObjects:
            if entity.tags.count(tag) > 0:
                entities.append(entity)

        return entities

    def get_world_by_tag(self, tag: str):

        worldObjects = []
        for world in self.worldObjects:
            if world.tags.count(tag) > 0:
                worldObjects.append(world)

        return worldObjects

