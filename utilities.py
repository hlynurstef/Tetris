class Utilities():
    """A class to store all utilities for Tetris."""

    def __init__(self):
        """Initializes the game utilities."""

        # Shapes
        self.tetris_shapes = [[[1, 1, 1],   # T Shape
                               [0, 1, 0]],

                               [[0, 2, 2],  # S Shape
                                [2, 2, 0]],

                               [[3, 3, 0],  # Z Shape
                                [0, 3, 3]],

                               [[4, 0, 0],  # J Shape
                                [4, 4, 4]],

                               [[0, 0, 5],  # L Shape
                                [5, 5, 5]],

                               [[6, 6, 6, 6]],  # I Shape

                               [[7, 7],     # O Shape
                                [7, 7]]]
