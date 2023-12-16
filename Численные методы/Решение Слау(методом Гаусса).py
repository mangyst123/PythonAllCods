def stringProdConst(string:list, c:float) -> list:
    '''Умножение строки на число'''
    return [round(string[i] * c, 10) for i in range(len(string))]

def sumStrings(stringOne:list, stringTwo:list) -> list:
    '''Складывает поэлементно строки'''
    return [round(stringOne[i] + stringTwo[i], 10) for i in range(len(stringOne))]

def straightStroke(A, b):
    '''Прямой ход (в виде уравнений)
    Добавить выбор главного элемента'''
    er = isGausAlgoritm(A)
    if er != 'Можно применять алгоритм':
        print(f'Алогритм Гауса применять нельзя, т к {er}')
    else:
        lenA = len(A)
        for h in range(lenA):
            b[h] /= A[h][h]
            A[h] = stringProdConst(A[h], 1 / A[h][h])
            for j in range(h+1, lenA):
                b[j] -= b[h] * A[j][h]
                A[j] = sumStrings(A[j], stringProdConst(A[h], -A[j][h]))
    return A, b

def reverseStroke(A, b):
    '''Обратный ход (в виде уравнений)'''
    lenA = len(A)
    for h in range(lenA-1, -1, -1):
        for j in range(h-1, -1, -1):
            b[j] -=  b[h] * A[j][h]
            b[j] = b[j]
            A[j][h] -= A[j][h]
    return A, b

def isGausAlgoritm(A):
    '''Проверка, можно ли применить алгоритм Гауса для этой матрицы'''
    if len(A) != len(A[0]):
        return 'матрица не квадратная (i!=j)'
    else:
        for x in range(len(A)):
            if A[x][x] == 0:
                return 'есть 0'
    return 'Можно применять алгоритм'

def generateMatrixAndB(variant, e, n):
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

def printMod(string, A, b):
    print(string, *[[x for x in A[i]] + ['|', b[i]] for i in range(len(A))], '', sep='\n')

def main():
    n = 10
    A, b = generateMatrixAndB(5, 10**(-2), n)
    printMod('Расширенная матрица (A|b):', A, b)

    straightStroke(A, b)
    printMod('Прямой ход (A|b):', A, b)

    reverseStroke(A, b)
    printMod('Обратный ход (A|b):', A, b)

    print(*[ f'x{x}: {b[x]}' for x in range(len(b))], sep='\n')

if __name__ == '__main__':
    main()
