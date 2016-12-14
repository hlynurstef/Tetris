import pygame
import ctypes
import platform
from game_settings import Settings
from block import Block
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
        pygame.display.set_caption('Tetris Reborn')
        self.title_screen = True


    def run_game(self):
        """Main function for Tetris."""
        while True:
            func.check_events()
            # TODO: Uncomment these lines to show title screen.
            #if self.title_screen:
            #    self.title_screen = func.update_title_screen(self.screen, self.settings)
            #else:
                #func.update_screen(self.screen, self.settings)
            func.update_screen(self.screen, self.settings)

if __name__ == '__main__':
    Tetris().run_game()
