from game_settings import Settings

class Utilities():
    """A class to store all utilities for Tetris."""

    def __init__(self):
        """Initializes the game utilities."""

        self.settings = Settings()
        # Shapes
        self.shapes = [([[1, 1, 1],      # T Shape
                         [0, 1, 0]], self.settings.purple),

                       ([[0, 2, 2],      # S Shape
                        [2, 2, 0]], self.settings.green),

                       ([[3, 3, 0],      # Z Shape
                        [0, 3, 3]], self.settings.red),

                       ([[4, 0, 0],      # J Shape
                        [4, 4, 4]], self.settings.blue),

                       ([[0, 0, 5],      # L Shape
                        [5, 5, 5]], self.settings.brown),

                                        # I Shape
                       ([[6, 6, 6, 6]], self.settings.light_blue),

                       ([[7, 7],         # O Shape
                        [7, 7]], self.settings.yellow)]
