



class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [[None for _ in range(size)] for _ in range(size)]

    def make_move(self, row, col, symbol):
        # Validate the symbol
        if symbol not in ('X', 'O'):
            return False
        # Validate row and column boundaries
        if not (0 <= row < self.size and 0 <= col < self.size):
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
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col] is None:
                    moves.append((row, col))
        return moves

    def board_reset(self):
        self.cells = [[None for _ in range(self.size)] for _ in range(self.size)]