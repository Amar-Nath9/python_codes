# Define the board
board = [" " for i in range(9)]

# Print the board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Check if the move is valid
def valid_move(move):
    if move < 0 or move > 8:
        return False
    if board[move] != " ":
        return False
    return True

# Get the player's move
def get_move(player):
    move = input("Enter {}'s move (0-8): ".format(player))
    while not move.isdigit():
        move = input("Invalid input. Enter {}'s move (0-8): ".format(player))
    move = int(move)
    while not valid_move(move):
        move = input("Invalid move. Enter {}'s move (0-8): ".format(player))
        move = int(move)
    return move

# Check if the game is over
def game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    # Check for tie
    if " " not in board:
        return True
    return False

# Play the game
def play_game():
    print_board()
    player = "X"
    while not game_over():
        move = get_move(player)
        board[move] = player
        print_board()
        if game_over():
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

    if " " not in board:
        print("Tie game!")
    else:
        print(player + " wins!")

play_game()
