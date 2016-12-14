from game_settings import Settings
from utilities import Utilities
from random import randrange


class Shape():
    """A class representing a single Tetris shape."""

    def __init__(self):
        """Initializes a single random Tetris shape."""

        self.settings = Settings()
        self.get_random_shape()
        self.x = 0
        self.y = 0


    def get_random_shape(self):
        """Gets a random shape."""
        shapes = Utilities().shapes
        choice = shapes[randrange(0, len(shapes))]
        # TODO: not sure if this works as an assignment as a class variable or if it will go out of scope.
        self.shape = choice[0]
        self.color = choice[1]
