from core.game import Game

# Create a new game
game = Game(rows=5, cols=5, win_length=4)

# Make two moves
game.make_move(0, 0)
game.make_move(1, 1)

# Display state before reset
print("Before reset:")
print("Board:", game.board.cells)
print("Current player:", game.current_player)

# Restart the game
game.reset()

# Display state after reset
print("\nAfter reset:")
print("Board:", game.board.cells)
print("Current player:", game.current_player)
print("Status:", game.status)
print("Winner:", game.winner)