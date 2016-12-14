import pygame
import ctypes
from game_settings import Settings
from block import Block
import game_functions as func

class Tetris():
    """A class representing the game."""

    def __init__(self):
        """Initialize game."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Tetris Reborn')
        self.title_screen = True


    def run_game(self):
        """Main function for Tetris."""
        while True:
            func.check_events()
            if self.title_screen:
                self.title_screen = func.update_title_screen(self.screen, self.settings)
            else:
                func.update_screen(self.screen, self.settings)


if __name__ == '__main__':
    Tetris().run_game()
