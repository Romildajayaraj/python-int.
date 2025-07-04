import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print('|'.join(row))
        if i < 2:
            print('-----')

# Check for win
def is_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cols
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_conditions)

# Check for draw
def is_draw(brd):
    return ' ' not in brd

# Get available moves
def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == ' ']

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    elif is_winner(brd, 'X'):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            best_score = min(score, best_score)
        return best_score

# AI makes move
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player move
        try:
            move = int(input("Enter your move (0-8): "))
        except ValueError:
            print("Please enter a number from 0 to 8.")
            continue
        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'

        print_board()
        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move()
        print("AI's Move:")
        print_board()
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()
