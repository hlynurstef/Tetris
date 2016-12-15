from game_settings import Settings
from utilities import Utilities
from random import randrange
from block import Block
import pygame


class Shape():
    """A class representing a single Tetris shape."""

    def __init__(self, screen):
        """Initializes a single random Tetris shape."""
        self.screen = screen
        self.settings = Settings()
        self.utils = Utilities()
        self.x = 200
        self.y = 0
        self.initialize_shape()
        self.moving_right = False
        self.moving_left = False
        self.clockwise = True



    def initialize_shape(self):
        """Initialize the shape."""
        self.get_random_shape()
        self.time_of_last_fall = pygame.time.get_ticks()
        self.fall_frequency = 500
        self.time_of_last_sidestep = pygame.time.get_ticks()
        self.side_frequency = 150


    def get_random_shape(self):
        """Gets a random shape."""
        shapes = self.utils.shapes
        index = randrange(0, len(shapes))
        self.arr_shape = shapes[index]

        shape_settings = self.utils.shape_info[index]
        self.name = shape_settings[0]
        self.image = shape_settings[1]

        self.shape = self.build_shape(self.arr_shape, self.image)


    def build_shape(self, shape, image):
        """Builds the shape."""
        new_shape = []
        for y in range(len(shape)):
            row = []
            for x in range(len(shape[y])):
                if shape[y][x]:
                    row.append(Block(self.screen, image, self.x + (x * 40), self.y + (y * 40)))
            if row:
                new_shape.append(row)
        return new_shape


    def rotate(self, board):
        """Rotates shape if it's possible to rotate."""
        if self.clockwise:
            arr_shape = [[self.arr_shape[y][x] for y in reversed(range(len(self.arr_shape)))]
                                 for x in range(len(self.arr_shape[0]))]
        else:
            arr_shape = [[self.arr_shape[y][x] for y in range(len(self.arr_shape))]
					             for x in reversed(range(len(self.arr_shape[0])))]

        shape = self.build_shape(arr_shape, self.image)

        for i in shape:
            print(i)
        if not board.check_collision(shape):
            self.shape = shape
            self.arr_shape = arr_shape
            if self.name == 'S' or self.name == 'Z':
                self.clockwise = not self.clockwise


    def rotate_shape(self):
        """ Returns a rotated copy of the shape."""



    def unable_to_rotate(self):
        """Returns True if shape is unable to rotate."""
        # TODO: check if shape is able to rotate.


    def update(self, board):
        """Update the position of the shape."""
        current_time = pygame.time.get_ticks()
        if current_time - self.time_of_last_fall > self.fall_frequency:
            if board.has_landed(self.shape):
                return True
            for row in self.shape:
                for block in row:
                    block.rect.y += 40
            self.y += 40
            self.time_of_last_fall = current_time

        if self.moving_left and board.can_move_to_left(self.shape):
            self.move_piece_sideways('LEFT', current_time)
        if self.moving_right and board.can_move_to_right(self.shape):
            self.move_piece_sideways('RIGHT', current_time)


    def move_piece_sideways(self, direction, current_time):
        """
        Moves shape either to the left or right.
        direction='LEFT' or direction='RIGHT'.
        """
        if current_time - self.time_of_last_sidestep > self.side_frequency:
            for row in self.shape:
                for block in row:
                    if direction == 'LEFT':
                        block.rect.x -= 40
                        self.x -= 40
                    elif direction == 'RIGHT':
                        block.rect.x += 40
                        self.x += 40
            self.time_of_last_sidestep = current_time


    def blitme(self):
        """Blit the Shape to the screen."""
        for row in self.shape:
            for block in row:
                block.blitme()
