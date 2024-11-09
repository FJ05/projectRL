class Game:

    def __init__(self, eventHandler, renderer):
        # A varible to hold the exist game function.
        self.end_reason = ""
        self.exit_game = None
        self.score = 0
        # Set the eventHandler and renderer for this game
        self.eventHandler = eventHandler
        self.renderer = renderer
        # Create empty entityObject and worldObject lists
        self.entityObjects = []
        self.worldObjects = []

    # A method to retrun the object lists
    def get_game_objects(self):
        return self.entityObjects, self.worldObjects

    # A fall back method that exists if no method has been created in the child game class
    def create_objects(self):
        print("No initial object exist for this game")
    
    def reset(self):
        print("This game did not have a real reset function falling back on this one")

    # A method to set the exit function varible
    def set_exit_game(self, exit_game_call_back):
        self.exit_game = exit_game_call_back

    # A method to get all entities that has the tag specified
    def get_entities_by_tag(self, tag: str, exclude = False): # Exclude mean you revert the process and get all but the tag

        entities = []
        for entity in self.entityObjects:
            if exclude:
                if entity.tags.count(tag) > 0:
                    continue
                else:
                    entities.append(entity)
            else:
                if entity.tags.count(tag) > 0:
                    entities.append(entity)

        return entities
    # A method to get all the word objects that has the tag specified
    def get_world_by_tag(self, tag: str, exclude = False): # Exclude mean you revert the process and get all but the tag

        worldObjects = []
        for world in self.worldObjects:
            if exclude:
                if world.tags.count(tag) > 0:
                    continue
                else:
                    worldObjects.append(world)
            else:
                if world.tags.count(tag) > 0:
                    worldObjects.append(world)

        return worldObjects
    
    def set_end_data(self, data):
        self.end_reason = data["reason"]
        self.score = data["score"]
