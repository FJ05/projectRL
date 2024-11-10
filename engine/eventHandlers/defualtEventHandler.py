import pygame

# This class handlers events. Events are literally functions but with a cool name that they should be run
# and happen each frame. It has a default event which is the exit event.
class EventHandler:

    def __init__(self) -> None:
        self.should_exit_callback = None
        self.added_events = []

    # The method that is run each frame and loops all events.
    def process_events(self):

        # Get all pygame events.
        events = pygame.event.get()

        # Loop all events.
        for event in events:
            if event.type == pygame.QUIT:
                self.should_exit_callback(True)  # Set exit condition through callback

        # Loop all custom events that have been added using the add_event method
        for event in self.added_events:
            event() # Execute the function / event.

    # Adds events(function) to the custom list
    def add_event(self, event):
        self.added_events.append(event)

    # Removes events(function) from the custom list
    def remove_event(self, event):
        self.added_events.remove(event)

    # Clears all event that have been added.
    def clear_events(self):
        self.added_events = []

    # A method to set the function to be run when the quit event is triggerd.
    def set_exist_callback(self, should_exit_callback):
        self.should_exit_callback = should_exit_callback