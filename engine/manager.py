import pygame

class GameManager:

    def __init__(self, games, resolution=(800, 600), fullscreen=False):
        # Pygame shit
        self.end_reason = ""
        pygame.init()
        self.screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN if fullscreen else 0)
        pygame.display.set_caption("RLGame")

        self.running = None
        self.dt = None
        self.clock = None


        # Games for the manager to manage,
        self.games = games
        self.current_game_index = 0

        # Pass the callback to each game, so the games know how to close the manager (used for when pressing x)
        for game in self.games:
            self.init_game(game)



    def run(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0  # Frame rate independent physics

        while self.running:
            game = self.games[self.current_game_index]
            game.run()

            # limits FPS to 60
            self.clock.tick(60)

        self.end()

    
    def init_game(self, game):
        # Setters under here
            game.eventHandler.set_exist_callback(self.set_running_state)
            game.renderer.set_screen(self.screen)
            game.renderer.set_objects(game.get_game_objects())
            game.set_exit_game(self.end_current_game)

            # Doers under here
            game.create_objects()

    def set_running_state(self, state: bool):
        self.running = not bool

    def end_current_game(self, end_data: dir): # next game means the next game in the game list
        #Callback function to end the current game's loop.
        self.end_reason = end_data["reason"]
        print(self.end_reason)
        game = self.games[self.current_game_index]
        game.reset()
        self.init_game(game)
        self.current_game_index = (self.current_game_index + end_data["next_game"]) % len(self.games)

        new_game = self.games[self.current_game_index]

        new_game.set_end_data(end_data)
    def end(self):
        pygame.quit()

