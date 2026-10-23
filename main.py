from core.board import Board

board = Board(3)

print(board.make_move(1, 1, "X"))  # True
print(board.make_move(1, 1, "O"))  # False - occupied
print(board.make_move(5, 5, "X"))  # False - out of bounds
print(board.make_move(0, 0, "A"))  # False - invalid symbol

for row in board.cells:
    print(row)