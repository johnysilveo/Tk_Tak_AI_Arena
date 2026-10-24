



class Board:
    def __init__(self, rows, cols, win_length):
        self.rows = rows
        self.cols = cols
        self.win_length = win_length
        self.cells = [[None for _ in range(cols)] for _ in range(rows)]

    def make_move(self, row, col, symbol):
        # Validate the symbol
        if symbol not in ('X', 'O'):
            return False
        # Validate row and column boundaries
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return False
        # Check if the cell is already occupied
        if self.cells[row][col] is not None:
            return False
        # Place the symbol
        self.cells[row][col] = symbol
        # Confirm successful move
        return True

    def available_moves(self):
        moves = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] is None:
                    moves.append((row, col))
        return moves

    def reset(self):
        self.cells = [
            [
                None for _ in range(self.cols)
            ]
                      for _ in range(self.rows)
                      ]