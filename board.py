from game_settings import Settings

class Board():
    """A class representing the playing board."""

    def __init__(self, screen):
        """Initialize the board."""
        self.screen = screen
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


    def add_to_board(self, shape):
        """Add shape to the board."""
        for row in shape:
            for block in row:
                x = (block.rect.x / 40) - 2
                y = (block.rect.y / 40)
                self.board[y][x] = block


    def blitme(self):
        """Draw the board."""
        for row in self.board:
            for block in row:
                if block:
                    block.blitme()
