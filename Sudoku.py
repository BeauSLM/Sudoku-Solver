# ----------Sudoku.py-------------
# Beau McCartney
# June 2021

# Create file handle
def init_file():
    return open('lib/' + input("Enter file name: "), 'r')

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
    print("Puzzle:" )
    for row in board:
        print(row)
    return board

if __name__ == "__main__":
    fhand = init_file()
    matrix = init_board(fhand)
