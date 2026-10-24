
def check_winner(board):
    win_directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1)
    ]
    for row in range(board.rows):
        for col in range(board.cols):
            # Get the current symbol
            symbol = board.cells[row][col]
            # Skip empty cells
            if symbol is None:
                continue
            # Check each direction
            for dr, dc in win_directions:
                count = 0
                # Check consecutive cells
                for step in range(board.win_length):
                    next_row = row + step * dr
                    next_col = col + step * dc
                    # Check board boundaries
                    if not (0 <= next_row < board.rows and
                            0 <= next_col < board.cols):
                        break
                    # Check whether symbols match
                    if board.cells[next_row][next_col] != symbol:
                        break
                    count += 1
                # Check whether the winning length was reached
                if count == board.win_length:
                    return symbol
    return None

def is_draw(board):
    return check_winner(board) is None and not board.available_moves()
