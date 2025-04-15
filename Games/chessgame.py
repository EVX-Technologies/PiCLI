import chess

# Initialize the chess board
board = chess.Board()

# Game loop: keep playing until the game ends
while not board.is_game_over():
    print(board)
    move = input("Enter your move (e.g., 'e2e4'): ")
    try:
        board.push_san(move)  # Make the move
    except ValueError:
        print("Invalid move, please try again.")

print("Game Over")
