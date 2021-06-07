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
            if square_row + i != row or square_col + j != column:
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

# Simple recursive brute-force algorithm to solve the sudoku game
def solve_board(board):
    row = 0
    column = 0
    while row < 9:
        while column < 9:
            for number in range(1, 10):
                if board[row][column] == 0:
                    if check_if_placeable(board, number, row, column):
                        board[row][column] = number
                        solve_board(board)
            column += 1
        row += 1

if __name__ == "__main__":
    board = init_board(init_file())
    solve_board(board)
    print("Final board:")
    print_board(board)
