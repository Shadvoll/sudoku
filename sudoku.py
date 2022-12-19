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


filename = 'sudoku-task0.txt'
matrix = readSudoku(filename)
printSudoku(matrix)
