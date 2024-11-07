import pygame

class EventHandler:
    def __init__(self) -> None:
        self.should_exit_callback = None
        self.added_events = []
        # Here we use dependency injection by passing a callback for setting the exit condition.


    def process_events(self):
        # This method processes the events and checks if we should quit

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.should_exit_callback(True)  # Set exit condition through callback

        for event in self.added_events: # Loops all functions / events in the self.added events and runs them.
            event()

    def add_event(self, event):
        self.added_events.append(event)

    def remove_event(self, event):
        self.added_events.remove(event)

    def clear_events(self):
        self.added_events = []

    # A method to set the function to be run when the quit event is run.
    def set_exist_callback(self, should_exit_callback):
        self.should_exit_callback = should_exit_callback