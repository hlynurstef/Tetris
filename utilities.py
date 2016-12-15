from game_settings import Settings

class Utilities():
    """A class to store all utilities for Tetris."""

    def __init__(self):
        """Initializes the game utilities."""

        self.settings = Settings()
        # Shapes
        self.shapes = [[ [0, 0, 0],
                         [1, 1, 1],      # T Shape
                         [0, 1, 0]],

                        [[0, 0, 0],
                         [0, 2, 2],      # S Shape
                         [2, 2, 0]],

                        [[0, 0, 0],
                         [3, 3, 0],      # Z Shape
                         [0, 3, 3]],

                        [[0, 0, 0],
                         [4, 4, 4],      # J Shape
                         [0, 0, 4]],

                        [[0, 0, 0],
                         [5, 5, 5],      # L Shape
                         [5, 0, 0]],

                        [[0, 0, 0, 0],
                         [6, 6, 6, 6],   # I Shape
                         [0, 0, 0, 0]],

                        [[0, 0, 0, 0],
                         [0, 7, 7, 0],   # O Shape
                         [0, 7, 7, 0],
                         [0, 0, 0, 0]]]


        self.shape_info = [ ('T', self.settings.T_block),
                            ('S', self.settings.S_block),
                            ('Z', self.settings.Z_block),
                            ('J', self.settings.J_block),
                            ('L', self.settings.L_block),
                            ('I', self.settings.I_block),
                            ('O', self.settings.O_block)]
