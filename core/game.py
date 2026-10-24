from core.board import Board
from core.rules import check_winner, is_draw


class Game:
    def __init__(self, rows=3, cols=3, win_length=3):
        # Create the game board
        self.board = Board(rows, cols, win_length)
        # Set the starting player
        self.current_player = "X"
        # Set the initial game status
        self.status = "playing"
        self.winner = None

    def make_move(self, row, col):
        if self.status != "playing":
            return False
        if not self.board.make_move(row, col, self.current_player):
            return False
        winner = check_winner(self.board)
        if winner is not None:
            self.winner = winner
            self.status = "won"
        elif is_draw(self.board):
            self.status = "draw"
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
        return True


    def reset(self):
        self.board.reset()
        self.current_player = "X"
        self.status = "playing"
        self.winner = None













