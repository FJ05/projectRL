import pygame

# This class exists to manage the games and what game to currently run.
# It's also the class that setup pygame.
# It's inspired by common starter code for pygame.
class GameManager:

    def __init__(self, games, resolution=(800, 600), fullscreen=False):
        # Pygame shit
        pygame.init()
        self.screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN if fullscreen else 0)
        pygame.display.set_caption("RLGame")

        self.running = None
        self.dt = None
        self.clock = None
        # The reason the last game ended
        self.end_reason = ""

        # Games for the manager to manage,
        self.games = games
        self.current_game_index = 0

        # Each game has to have some statring values added to the class. Loop all games and init it.
        for game in self.games:
            self.init_game(game)


    # The main loop.
    def run(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0  # Frame rate independent physics

        # The main loop running the currect game index.
        while self.running:
            game = self.games[self.current_game_index]
            # Runs the game
            game.run()

            # limits FPS to 60
            self.clock.tick(60)
        # End the python game is the main loop stopped.
        self.end()

    # A method to init all games with values then currently don't have.
    # It also creates objects in the background to be then render ready.
    def init_game(self, game):
        # Setters under here
            game.eventHandler.set_exist_callback(self.set_running_state)
            game.renderer.set_screen(self.screen)
            game.renderer.set_objects(game.get_game_objects())
            game.set_exit_game(self.end_current_game)

            # Doers under here
            game.create_objects()
    # A method to set the running state
    def set_running_state(self, state: bool):
        self.running = not state # due the name in eventhandler being should_exit and the name here being running, makes us add not to invert the bool.

    # A method to end the current game and go to the next one, Take in end data
    def end_current_game(self, end_data: dir): # next game means the next game in the game list
        #Callback function to end the current game's loop.
        self.end_reason = end_data["reason"]
        # reset the ended game
        game = self.games[self.current_game_index]
        game.reset()
        # init it again to be ready in the future
        self.init_game(game)
        # Change the game index using end_data
        self.current_game_index = (self.current_game_index + end_data["next_game"]) % len(self.games)


        new_game = self.games[self.current_game_index]
        # Set the end data to the new game
        new_game.set_end_data(end_data)

    # A method to end the game.
    def end(self):
        pygame.quit()

