from game_settings import Settings

class Board():
    """A class representing the playing board."""

    def __init__(self):
        """Initialize the board."""
        self.settings = Settings()
        self.initialize_board()


    def initialize_board(self):
        """Initialize the board."""
        self.clear_board()


    def clear_board(self):
        """Returns an empty board."""
        board = []
        for row in range(self.settings.board_height):
            row = []
            for col in range(self.settings.board_width):
                row.append(None)
            board.append(row)
        self.board = board
