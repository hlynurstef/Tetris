import pygame

class Settings():
    """A class to store all settings for Tetris."""

    def __init__(self):
        """Initializes the game settings."""

        # Colors.
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.flesh_color = (255, 214, 156)

        self.light_blue = (49, 199, 239)    # I Block color
        self.yellow = (247, 211, 8)         # O Block color
        self.purple = (173, 77, 156)        # T Block color
        self.green = (0, 255, 0)            # S Block color
        self.red = (255, 0, 0)              # Z Block color
        self.blue = (0, 0, 255)             # J Block color
        self.brown = (239, 121, 33)         # L Block color

        # Screen settings.
        self.screen_width = 800
        self.screen_height = 720
        self.caption = "Tetris"

        self.fps = 60
        self.starting_fall_frequency = 800

        # Size of each block in grid
        self.scale = 40

        # Board dimensions
        self.board_width = 10
        self.board_height = 18

        # Images
        self.wall = pygame.image.load('images/wall_full.png')
        self.title_screen = pygame.image.load('images/title_screen.png')
        self.scoreboard = pygame.image.load('images/scoreboard.png')
        self.J_block = pygame.image.load('images/shapes/J.png')
        self.L_block = pygame.image.load('images/shapes/L.png')
        self.O_block = pygame.image.load('images/shapes/O.png')
        self.S_block = pygame.image.load('images/shapes/S.png')
        self.Z_block = pygame.image.load('images/shapes/Z.png')
        self.T_block = pygame.image.load('images/shapes/T.png')
        self.I_block = pygame.image.load('images/shapes/I.png')

        # Font
        self.font = 'fonts/game_boy.ttf'
        self.font_size = 40
