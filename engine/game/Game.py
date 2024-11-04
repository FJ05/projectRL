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

