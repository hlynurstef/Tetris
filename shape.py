from game_settings import Settings
from utilities import Utilities
from random import randrange
from block import Block


class Shape():
    """A class representing a single Tetris shape."""

    def __init__(self, screen):
        """Initializes a single random Tetris shape."""
        self.screen = screen
        self.settings = Settings()
        self.initialize_shape()


    def initialize_shape(self):
        """Initialize the shape."""
        shape = self.get_random_shape()
        self.set_starting_position(shape[0])
        self.shape = self.build_shape(shape[0], shape[1])


    def get_random_shape(self):
        """Gets a random shape."""
        shapes = Utilities().shapes
        choice = shapes[randrange(0, len(shapes))]
        # TODO: not sure if this works as an assignment as a class variable or if it will go out of scope.
        return choice


    def build_shape(self, shape, color):
        """Builds the shape."""
        new_shape = []
        for y in range(len(shape)):
            row = []
            for x in range(len(shape[y])):
                if shape[y][x]:
                    row.append(Block(self.screen, color, self.x + (x * 40), self.y + (y * 40)))
            new_shape.append(row)
        return new_shape


    def set_starting_position(self, shape):
        """Sets the starting position of the shape."""
        self.x = 200
        self.y = 40

        # Check if O Shape
        if len(shape[0]) == 2:
            self.x = 240


    def rotate(self, clockwise=True):
        """
        Rotates shape clockwise if it's possible to rotate.
        If counter=False then rotate counter clockwise.
        """
        if self.unable_to_rotate():
            return
        if clockwise:
            self.shape = [[shape[y][x] for y in reversed(range(len(shape)))]
                                 for x in range(len(shape[0]))]
        else:
            self.shape = [[shape[y][x] for y in range(len(shape))]
					             for x in reversed(range(len(shape[0])))]


    def unable_to_rotate(self):
        """Returns True if shape is unable to rotate."""
        # TODO: check if shape is able to rotate.


    def update(self, speed):
        """Update the position of the shape."""
        for row in self.shape:
            for block in row:
                block.rect.y += int(200 * speed)


    def blitme(self):
        """Blit the Shape to the screen."""
        for row in self.shape:
            for block in row:
                block.blitme()
