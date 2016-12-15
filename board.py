from game_settings import Settings

class Board():
    """A class representing the playing board."""

    def __init__(self, screen):
        """Initialize the board."""
        self.screen = screen
        self.settings = Settings()
        self.initialize_board()
        self.height = self.settings.board_height
        self.width = self.settings.board_width
        self.x = 80
        self.y = 0


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


    def check_collision(self, shape):
        for row in shape:
            for block in row:
                x = self.get_x_index(block)
                y = self.get_y_index(block)

                if (x < 0 or x > self.settings.board_width-1
                or y < 0 or y > self.settings.board_height-1
                or self.board[y][x]):
                    return True
        return False


    def fix_board(self, board):
        new_board = []
        for i in reversed(range(self.height)):
            if board[i] != [None] * self.width:
                new_board.append(board[i])

        new_board += [[None] * self.width for x in range(self.height - len(new_board))]
        new_board.reverse()
        return new_board


    def fix_block_positions(self):
        for y in reversed(range(len(self.board))):
            for x in range(len(self.board[y])):
                if self.board[y][x]:
                    self.board[y][x].rect.x = self.x + (x * 40)
                    self.board[y][x].rect.y = self.y + (y * 40)


    """
    def clear_full_lines(self):
        Removes all lines that are full.
        lines_removed = 0
        for y in reversed(range(self.settings.board_height)):
            if self.line_is_full(y):
                self.clear_line(y)
        self.fix_board()"""

    def remove_full_lines(self):
        new_board = [[None] * self.width if self.line_is_full(x) else x for x in reversed(self.board)]
        new_board.reverse()
        self.board = self.fix_board(new_board)
        self.fix_block_positions()


    def clear_line(self, line_index):
        """ Clears a single line on the board."""
        for x in range(10):
            self.board[line_index][x] = None


    def line_is_full(self, line):
        """Checks if the given line is full."""
        for x in line:
            if not x :
                return False
        return True


    def line_is_empty(self, line_index):
        """Checks if the given line is empty."""
        for i in range(self.settings.board_with):
            if self.board[line_index][i] != None:
                return False
        return True


    def blitme(self):
        """Draw the board."""
        for row in self.board:
            for block in row:
                if block:
                    block.blitme()
