from random import randrange
from block import Block
from pygame.time import get_ticks
import pygame


class Shape():
    """A class representing a single Tetris shape."""

    def __init__(self, screen, settings, sounds, effect_channel, utils, x=200, y=0):
        """Initializes a single random Tetris shape."""
        self.screen = screen
        self.settings = settings
        self.sounds = sounds
        self.effect_channel = effect_channel
        self.utils = utils
        self.x = x
        self.y = y
        self.initialize_shape()
        self.moving_right = False
        self.moving_left = False
        self.clockwise = True
        self.moving_fast = False
        self.first_press_down_key = True
        self.moving_fast_start_index = 1


    def initialize_shape(self):
        """Initialize the shape."""
        self.get_random_shape()
        self.time_of_last_fall = get_ticks()
        self.fall_frequency = 800
        self.time_of_last_sidestep = get_ticks()
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

        if not board.check_collision(shape):
            self.effect_channel.play(self.sounds.rotate)
            self.shape = shape
            self.arr_shape = arr_shape
            if self.name == 'S' or self.name == 'Z':
                self.clockwise = not self.clockwise


    def unable_to_rotate(self):
        """Returns True if shape is unable to rotate."""
        # TODO: check if shape is able to rotate.


    def update(self, board, game_stats):
        """Update the position of the shape."""
        current_time = get_ticks()
        if current_time - self.time_of_last_fall > self.fall_frequency:
            if board.has_landed(self.shape):
                if self.moving_fast:
                    game_stats.add_score((self.get_lowest_y_value() // 40) - self.moving_fast_start_index)
                return True
            for row in self.shape:
                for block in row:
                    block.rect.y += 40
            self.y += 40
            self.time_of_last_fall = current_time

        if self.moving_left and board.can_move_to_left(self.shape):
            self.move_shape_left(current_time)
        if self.moving_right and board.can_move_to_right(self.shape):

            self.move_shape_right(current_time)

        self.fall_frequency = game_stats.fall_frequency


    def move_shape_right(self, current_time):
        """Move shape to the left."""
        if current_time - self.time_of_last_sidestep > self.side_frequency:
            self.effect_channel.play(self.sounds.move_sideways)
            for row in self.shape:
                for block in row:
                    block.rect.x += 40
            self.x += 40
            self.time_of_last_sidestep = current_time


    def move_shape_left(self, current_time):
        """Move shape to the left."""
        if current_time - self.time_of_last_sidestep > self.side_frequency:
            self.effect_channel.play(self.sounds.move_sideways)
            for row in self.shape:
                for block in row:
                    block.rect.x -= 40
            self.x -= 40
            self.time_of_last_sidestep = current_time


    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.shape = self.build_shape(self.arr_shape, self.image)
        self.time_of_last_fall = get_ticks()


    def start_moving_fast(self):
        """Sets the moving fast flag for calculating score."""
        if self.first_press_down_key:
            self.moving_fast = True
            self.moving_fast_start_index = self.get_lowest_y_value() // 40
            self.first_press_down_key = False


    def stop_moving_fast(self):
        """Sets the moving fast flag for calculating score."""
        self.moving_fast = False


    def get_lowest_y_value(self):
        """Returns the lowest y value of the shapes blocks."""
        lowest = 720
        for row in self.shape:
            for block in row:
                if block.rect.y < lowest:
                    lowest = block.rect.y
        return lowest



    def blitme(self):
        """Blit the Shape to the screen."""
        for row in self.shape:
            for block in row:
                block.blitme()
