
def productOfMatrices(MatrixOne, MatrixTwo):
    '''Произведение матриц'''
    newMatrix = [[0 for y in range(len(MatrixTwo[0]))] for x in range(len(MatrixOne))]
    for i in range(len(MatrixOne)):
        for j in range(len(MatrixTwo[0])):
            for k in range(len(MatrixOne)):
                newMatrix[i][j] += MatrixOne[i][k] * MatrixTwo[k][j]
    return newMatrix

def bubble_sort(n, vector):
    '''Сортировка, нужна для обратной сортировки вектора ответов'''
    for run in range(len(n)):
        for j in range(len(n)-1-run):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector

def multiplicationVectorInScolar(vector, a):
    '''Умножение вектора на число
    и убираю -0 получаются при вычислении'''
    newVector = vector.copy()
    a = 0 if a == -0 else a
    for x in range(len(vector)):
        newVector[x] *= a
    return newVector

def sumVectors(vectorOne, VectorTwo):
    '''Сумма векторов'''
    newVector = [vectorOne[x] + VectorTwo[x] for x in range(len(vectorOne))]
    return newVector

def clearZero(matrix):
    '''Все равно появляются -0 их меняю на 0
    На ответ не влияет, просто для красоты'''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -0:
                matrix[i][j] = 0
    return matrix

# Модом гауса (Прямой ход)
def straightStroke(matrixA, vectorB):
    '''Тут метод Гауса в матричном виде'''
    newMatrix = [matrixA[x] + vectorB[x] for x in range(len(matrixA))]
    for k in range(len(matrixA)):
        newMatrix[k] = multiplicationVectorInScolar(newMatrix[k], 1 / newMatrix[k][k])
        for i in range(k+1, len(matrixA)):
            a = multiplicationVectorInScolar(newMatrix[k], (-1)*newMatrix[i][k])
            newMatrix[i] = sumVectors(newMatrix[i], a)

    return clearZero(newMatrix)

# Обратный ход
def reverseStroke(matrix):
    '''Обратный ход, так же в матричном виде'''
    l = len(matrix)
    for n in range(l-1, 0, -1):
        for i in range(n-1, 0, -1):
            a = matrix[n][n] * matrix[i][n]
            b = matrix[n][-1] * matrix[i][n]
            matrix[i][n] -= a
            matrix[i][-1] -= b
    return [[matrix[x][y] for y in range(l)] for x in range(l)], [[x[-1]] for x in matrix]

# Это вектор, на который будем умножать обратную матрицу
vectorB = [[-8], [-1], [0], [0], [1], [0], [8], [0], [0], [0], [0], [0],]
matrix = [
    #a0 b0 c0 d0 a1 b1 c1 d1 a2 b2 c2 d2
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [0, 1, 2, 3, 0, -1, 0, 0, 0, 0, 0, 0], # 8
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 1, 2, 3, 0, -2, 0, 0], # 9
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 2, 6, 0, 0, -2, 0], # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 8],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6],  # 12 * 1 и + к 11
    [0, 0, 1, 3, 0, 0, -1, 0, 0, 0, 1, 6]  # 11
]
n = [1, 5, 4, 8, 2, 9, 6, 10, 3, 7, 12, 11] # Новый порядок уравнений

a = straightStroke(matrix, vectorB)
finMatrix, finVectorB = reverseStroke(a)

odds = productOfMatrices(finMatrix, finVectorB)

# Вывод результата
result, iterr = {}, 0
for x in '012':
    for y in 'abcd':
        a = y+x
        result.update({a : odds[iterr]})
        iterr += 1
print(*[x+': '+str(result[x]) for x in result], sep='\n')
