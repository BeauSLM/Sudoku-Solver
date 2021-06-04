# ----------Sudoku.py-------------
# Beau McCartney
# June 2021

# file input
def init_file():
    return open('lib/' + input("Enter file name: "), 'r')

def init_matrix(fhand):
    matrix = [[0 for i in range(9)] for j in range(9)]
    i = 0
    j = 0
    for line in fhand:
        line = line.strip()
        for number in line:
            matrix[i][j] = int(number)
            j += 1
        i += 1
        j = 0
    print("Puzzle:" )
    for row in matrix:
        print(row)
    return matrix

if __name__ == "__main__":
    fhand = init_file()
    matrix = init_matrix(fhand)
