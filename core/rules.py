from core import Board


def check_winner(board):
    winner = False
    for row in board.cells:
        if row[0] is not None and row[0] == row[1] == row[2]:
            winner = True
    for col in range(board.size):
        if (board.cells[0][col] is not None
                and board.cells[0][col] == board.cells[1][col] == board.cells[2][col]):
            winner = True
    return winner
