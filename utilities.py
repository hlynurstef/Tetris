from game_settings import Settings

class Utilities():
    """A class to store all utilities for Tetris."""

    def __init__(self):
        """Initializes the game utilities."""

        self.settings = Settings()
        # Shapes
        self.shapes = [([[1, 1, 1],      # T Shape
                         [0, 1, 0]], self.settings.T_block),

                       ([[0, 2, 2],      # S Shape
                         [2, 2, 0]], self.settings.S_block),

                       ([[3, 3, 0],      # Z Shape
                         [0, 3, 3]], self.settings.Z_block),

                       ([[4, 4, 4],      # J Shape
                         [0, 0, 4]], self.settings.J_block),

                       ([[5, 5, 5],      # L Shape
                         [5, 0, 0]], self.settings.L_block),

                                        # I Shape
                       ([[6, 6, 6, 6]], self.settings.I_block),

                       ([[7, 7],         # O Shape
                         [7, 7]], self.settings.O_block)]
