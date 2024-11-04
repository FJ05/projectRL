import pygame

class GameManager:

    def __init__(self, games, resolution=(800, 600), fullscreen=False):
        # Pygame shit
        pygame.init()
        self.screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN if fullscreen else 0)
        pygame.display.set_caption("Game Obama")

        self.running = None
        self.dt = None
        self.clock = None


        # Games for the manager to manage,
        self.games = games
        self.current_game_index = 0

        # Pass the callback to each game, so the games know how to close the manager (used for when pressing x)
        for game in self.games:
            # Setters under here
            game.eventHandler.set_exist_callback(self.set_running_state)
            game.renderer.set_screen(self.screen)
            game.renderer.set_objects(game.get_game_objects)
            game.set_exit_game(self.end_current_game)

            # Doers under here
            game.create_objects()



    def run(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0  # Frame rate independent physics

        while self.running:
            print(self.current_game_index)
            game = self.games[self.current_game_index]
            game.run()

            # limits FPS to 60
            self.dt = self.clock.tick(60) / 1000

        self.end()

    def set_running_state(self, state: bool):
        self.running = not bool

    def end_current_game(self):
        #Callback function to end the current game's loop.
        print("nub")
        self.current_game_index = (self.current_game_index + 1) % len(self.games)

    def end(self):
        pygame.quit()

