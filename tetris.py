import pygame
import ctypes
import platform
from game_settings import Settings
from block import Block
from shape import Shape
from board import Board
import game_functions as func

class Tetris():
    """A class representing the game."""

    def __init__(self):
        """Initialize game."""
        pygame.init()

        if platform.system() == 'Windows':
            # Ensure correct screen size to be displayed.
            ctypes.windll.user32.SetProcessDPIAware()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.title_screen = True

        self.current_shape = Shape(self.screen)
        self.board = Board(self.screen)

        # Make a clock object to set fps limit.
        self.clock = pygame.time.Clock()


    def run_game(self):
        """Main function for Tetris."""
        while True:
            # Delta time calculation.
            self.clock.tick(self.settings.fps)

            func.check_events(self.current_shape, self.board)
            # TODO: Uncomment these lines to show title screen.
            #if self.title_screen:
            #    self.title_screen = func.update_title_screen(self.screen, self.settings)
            #else:
                #func.update_screen(self.screen, self.settings)
            new_shape = func.update_screen(self.screen, self.settings, self.current_shape, self.board)
            if new_shape:
                self.current_shape = Shape(self.screen)

if __name__ == '__main__':
    Tetris().run_game()
