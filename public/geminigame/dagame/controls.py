import pygame

class Controls:
    """
    Handles keyboard inputs and maps them to game actions.
    """

    def __init__(self, control_keys):
        """
        Initialize the Controls object with a mapping of keys to actions.

        :param control_keys: A dictionary mapping from pygame key codes to actions (functions).
        """
        self.control_keys = control_keys
        self.pressed_keys = {}

    def update_pressed_keys(self):
        """
        Update the state of pressed keys.
        """
        self.pressed_keys = pygame.key.get_pressed()

    def handle_controls(self):
        """
        Execute actions based on the current state of pressed keys.
        """
        for key, action in self.control_keys.items():
            if self.pressed_keys[key]:
                action()
