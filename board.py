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
        for row in shape.shape:
            for block in row:
                x = self.get_x_index(block)
                y = self.get_y_index(block)
                self.board[y][x] = block


    def has_landed(self, shape):
        """Return True if shape has landed on board."""
        for row in shape:
            for block in row:
                x = self.get_x_index(block)
                y = self.get_y_index(block) + 1
                if y >= self.settings.board_height or self.board[y][x]:
                    return True
        return False


    def can_move_to_left(self, shape):
        """Return True if shape can move left."""
        for i in range(len(shape)):
            x = self.get_x_index(shape[i][0]) - 1
            y = self.get_y_index(shape[i][0])
            if x < 0 or self.board[y][x]:
                return False
        return True


    def can_move_to_right(self, shape):
        """Return True if shape can move right."""
        for i in range(len(shape)):
            x = self.get_x_index(shape[i][-1]) + 1
            y = self.get_y_index(shape[i][-1])
            if x > self.settings.board_width-1 or self.board[y][x]:
                return False
        return True


    def get_x_index(self, block):
        """Return x index for block."""
        return int((block.rect.x / 40) - 2)


    def get_y_index(self, block):
        """Return y index for block."""
        return int((block.rect.y / 40))


    def blitme(self):
        """Draw the board."""
        for row in self.board:
            for block in row:
                if block:
                    block.blitme()
