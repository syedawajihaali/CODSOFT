import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def full(board):
    return all(cell != " " for row in board for cell in row)

def emptycells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def minimax(board, depth, maximizing_player):
    if winner(board, "X"):
        return -1
    if winner(board, "O"):
        return 1
    if full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for row, col in emptycells(board):
            board[row][col] = "O"
            eval = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row, col in emptycells(board):
            board[row][col] = "X"
            eval = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def bestmove(board):
    best_move = None
    best_eval = float("-inf")
    for row, col in emptycells(board):
        board[row][col] = "O"
        eval = minimax(board, 0, False)
        board[row][col] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            row, col = map(int, input("Enter your move (row col)(in range 0-2): ").split())
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "X"
            print_board(board)

            if winner(board, "X"):
                print("You win!")
                break
            if full(board):
                print("It's a draw!")
                break

            print("AI's move:")
            ai_row, ai_col = bestmove(board)
            board[ai_row][ai_col] = "O"
            print_board(board)

            if winner(board, "O"):
                print("AI wins!")
                break
            if full(board):
                print("It's a draw!")
                break

        except ValueError:
            print("Invalid input. Please enter row and col as integers.")

if __name__ == "__main__":
    main()
