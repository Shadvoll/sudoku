N = M = 9
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
    
filename = 'sudoku-task0.txt'
matrix = readSudoku(filename)
printSudoku(matrix)
