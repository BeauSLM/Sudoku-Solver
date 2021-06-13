# ----------Sudoku.py-------------
# Beau McCartney
# June 2021

# Create file handle
def init_file():
    return open('lib/' + input("Enter file name: ") + '.txt', 'r')

# Read in contents of the file, into a 9x9 list
def init_board(fhand):
    # initialize a list with nine elements, each element is a list with 9 integer elements
    board = [[0 for i in range(9)] for j in range(9)]

    # Populate the list with the puzzle values in the file
    i = 0
    j = 0
    for line in fhand:
        line = line.strip()
        for number in line:
            board[i][j] = int(number)
            j += 1
        i += 1
        j = 0
    fhand.close()
    print("Puzzle:" )
    print_board(board)
    return board

# Print the board as a matrix
def print_board(board):
    for line in board:
        print(line)

# Check if number can be placed in board[row][column] on board legally
def check_if_placeable(board, number, row, column):
    # Check rows and columns
    for i in range(9):
        if board[row][i] == number and i != column:
            return False
        if board[i][column] == number and i != row:
            return False
    # Check the corresponding square
    square_row = row - row % 3
    square_col = column - column % 3
    for i in range(3):
        for j in range(3):
            if (square_row + i) == row and (square_col + j) == column:
                continue
            if board[square_row + i][square_col + j] == number:
                return False
    return True

# Count the remaining number of empty cells
def count_remaining(board):
    count = 0
    for line in board:
        for number in line:
            if number == 0:
                count += 1
    return count

def check_valid(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] > 0:
                if not check_if_placeable(board, board[row][column], row, column):
                    return False
    return True

class calls:
    calls = 0

call_track = calls()

# Simple recursive brute-force algorithm to solve the sudoku game
def solve_board(board):
    call_track.calls += 1
    # Find and record and empty square
    empty_row = -1
    empty_col = -1
    break_check = False
    for row in range(9):
        for column in range(9):
            if (board[row][column] == 0):
                empty_row = row
                empty_col = column
                break_check = True
                break
        if break_check:
            break

    # Place a number in the cell. Return if board is finished, set cell to zero if a solution isn't possible
    for number in range(1, 10):
        if check_if_placeable(board, number, empty_row, empty_col):
            board[empty_row][empty_col] = number
            solve_board(board)
            if count_remaining(board) == 0:
                return
            board[empty_row][empty_col] = 0

if __name__ == "__main__":
    board = init_board(init_file())
    if not check_valid(board):
        print("Invalid puzzle, aborting. ")
        exit(1)
    solve_board(board)
    print("Final board:")
    print_board(board)
    print(call_track.calls , "number of calls")
