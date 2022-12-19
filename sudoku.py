N = M = 9
def readSudoku(filename):
    with open(filename) as f:
        lines = f.readlines()
    res = []
    for line in lines:
        if len(line) > 2:
            tmp = list(map(int,line.split()))
            res.append(tmp)
    return res

def printSudoku(matrix):
    for i in range(N):
        print(*matrix[i],sep=' ')
    
filename = 'sudoku-task0.txt'
matrix = readSudoku(filename)
printSudoku(matrix)
