import pygame

class Settings():
    """A class to store all settings for Tetris."""

    def __init__(self):
        """Initializes the game settings."""

        # Colors.
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # I Block color
        self.light_blue = (49, 199, 239)
        # O Block color
        self.yellow = (247, 211, 8)
        # T Block color
        self.purple = (173, 77, 156)
        # S Block color
        self.green = (0, 255, 0)
        # Z Block color
        self.red = (255, 0, 0)
        # J Block color
        self.blue = (0, 0, 255)
        # L Block color
        self.brown = (239, 121, 33)

        # Screen settings.
        self.screen_width = 800
        self.screen_height = 720
        self.caption = "Tetris"

        self.fps = 15

        # Size of each block in grid
        self.scale = 40

        # Screen dimensions
        # Single block: 40x40 pixels
        # Screen width: 20 Blocks
        # Screen height: 18 Blocks
        # Board size: 10 Blocks x 18 Blocks
        # Left side: 2 Blocks
        # Right side: 7 Blocs

        # Images
        self.wall = pygame.image.load('images/wall_full.png')
