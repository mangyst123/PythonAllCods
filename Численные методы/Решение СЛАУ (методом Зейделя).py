import time

def abs(a):return a if a > 0 else -a

def norma(a):
    '''Находит норму ветора (максимум модулей элементов)'''
    return max([abs(x) for x in a])

def newVectorX(alpha, X, betta):
    '''Методом Зейделся'''
    newX = X.copy()
    for i in range(len(betta)):
        newX[i] = betta[i]
        for j in range(i):
            if i != j:
                newX[i] +=  alpha[i][j]*newX[j]
        for j in range(i, len(betta)):
            if i != j:
                newX[i] +=  alpha[i][j]*X[j]
    return newX

def razVectors(a, b):
    '''Зарность векторо'''
    return [a[x] - b[x] for x in range(len(a))]

def calculationFormula(alpha, betta, E=10**(-10)):
    '''Метод простых итераций (реализация)
        с модификацией'''
    X = [[0 for x in range(len(betta))]] # Выбор начального вектора (изначально такой)
    count = 1
    while True:
        X += [newVectorX(alpha, X[-1], betta)]
        if norma(razVectors(X[-1], X[-2])) < E:
            break
        count += 1
    return X[-1], count

def alpha(A):
    '''Создаем матрицу альфа'''
    a = []
    for i in range(len(A)):
        a += [[]]
        for j in range(len(A)):
            if i == j:
                a[i] += [0]
            else:
                a[i] += [-A[i][j] / A[i][i]]
    return a

def betta(A, b):
    '''Создаем вектор бетта'''
    return [b[x] / A[x][x] for x in range(len(A))]

def generateMatrixAndB(variant, n, e=10**(-4)):
    '''Создаю матриу для заданного варианта
       (для проверки алгоритма)'''
    A = []
    for i in range(n):
        A += [[]]
        for j in range(n):
            if i != j:
                A[i] += [(variant+i)*e]
            else:
                A[i] += [(variant+i)]
    # Создание вектора b
    b = [sum([A[i][j] * (variant+j) for j in range(n)]) for i in range(n)]
    return A, b

def main():
    n = 10
    A, b = generateMatrixAndB(5, n)
    Xk, count = calculationFormula(alpha(A), betta(A, b))

    print('\n', *[f'x{k}: {Xk[k]}\n' for k in range(len(Xk))], sep='')
    print('Количество итераций (k+1):', count)

if __name__ == '__main__':
    main()
