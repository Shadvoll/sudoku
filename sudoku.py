import copy


N = M = 9 #GLOBAL consts
'''
    readSudoku(filename)
    Discription:
        Cчитывание матрицы судоку из filename (.txt файл). Пропускаются пустые строки.
        Цифры должны идти через пробел. Ожидается на входе 9 х 9 матрица, нет проверки.
    INPUT:
        filename - название файла .txt для чтения
    OUTPUT:
        list of lists. Судоку матрица в виде списка списков цирф.

'''
def readSudoku(filename):
    with open(filename) as f:
        lines = f.readlines()
    res = []
    for line in lines:
        if len(line) > 2:
            tmp = list(map(int,line.split()))
            res.append(tmp)
    return res
'''
    printSudoku( matrix )
    Description:
        Вывод матрицы судоку.
    INPUT:
        matrix - list of lists. Судоку матрица в виде списка списков цирф.
    
'''
def printSudoku(matrix):
    for i in range(N):
        print(*matrix[i],sep=' ')
    

def getCol(index,matrix):
    i = index // M
    j = index % M
    res = []
    for i in range(N):
        res.append(matrix[i][j])
    return res

def getRow(index,matrix):
    i = index // M
    j = index % M
    res = []
    for j in range(M):
        res.append(matrix[i][j])
    return res

def getTile(index,matrix):
    row = index // M
    col = index % M
    i3 = row//3 * 3
    j3 = col//3 * 3
    res = []
    for i in range(i3,i3+3):
        for j in range(j3,j3+3):
            res.append(matrix[i][j])
    return res

def checkRules(index,num,matrix):
    return (num not in getRow(index,matrix)) and (num not in getCol(index,matrix)) and (num not in getTile(index,matrix))

def isSolved(matrix):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                return False
    return True


def solve(index,matrix,origin_matrix):
    if isSolved(matrix):
        return matrix
#     print_2dlist(matrix)
    i = index // M
    j = index % M
    if origin_matrix[i][j] == 0:
        for num in range(1,9+1):
            if checkRules(index,num,matrix):
                matrix[i][j] = num
                matrix = solve(index+1,matrix,origin_matrix)
    else:
        matrix = solve(index+1,matrix,origin_matrix)

filename = 'sudoku-task0.txt'
origin_matrix = readSudoku(filename)
matrix = copy.deepcopy(origin_matrix)
matrix_res = solve(0,matrix,origin_matrix)
printSudoku(matrix_res)
