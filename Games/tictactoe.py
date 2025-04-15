import random

# Initialize the board
board = [" " for _ in range(9)]


def print_board():
    """Displays the board."""
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)


def check_win(player):
    """Checks if the given player ('X' or 'O') has won."""
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Rows
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Columns
        (0, 4, 8),
        (2, 4, 6)
    ]  # Diagonals
    return any(board[a] == board[b] == board[c] == player
               for a, b, c in win_conditions)


def get_empty_positions():
    """Returns a list of available positions."""
    return [i for i in range(9) if board[i] == " "]


def player_move():
    """Lets the player choose a move."""
    while True:
        try:
            move = int(input("Enter a position (1-9): ")) - 1
            if move in get_empty_positions():
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def computer_move():
    """Computer makes a strategic move."""
    # Step 1: Check if the computer can win
    for move in get_empty_positions():
        board[move] = "O"
        if check_win("O"):
            return
        board[move] = " "  # Reset move

    # Step 2: Block player's winning move
    for move in get_empty_positions():
        board[move] = "X"
        if check_win("X"):
            board[move] = "O"
            return
        board[move] = " "  # Reset move

    # Step 3: Pick the center if available
    if 4 in get_empty_positions():
        board[4] = "O"
        return

    # Step 4: Pick a random move
    move = random.choice(get_empty_positions())
    board[move] = "O"


# Game loop
while True:
    print_board()
    player_move()

    if check_win("X"):
        print_board()
        print("You win!")
        break
    elif not get_empty_positions():
        print_board()
        print("It's a draw!")
        break

    computer_move()

    if check_win("O"):
        print_board()
        print("Computer wins!")
        break
