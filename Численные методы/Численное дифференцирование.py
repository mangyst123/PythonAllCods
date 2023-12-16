import math

def module(a):
    return -a if a < 0 else a
def outTable(X, Vficislen, fTochn):
    '''Вывод таблицы'''
    print('Точка\tВычисленное значение\tТочное значение\t\tРазница')
    for i in range(len(X)):
        if Vficislen[i] == 'NON':
            print(X[i], Vficislen[i], '\t', fTochn[i] , 'NON', sep='\t')
        else:
            print(X[i], Vficislen[i], fTochn[i] , module(Vficislen[i] - fTochn[i]), sep='\t')
    print()

def maxdifference(X, Vficislen, fTochn):
    '''Вернем максимальный разброс среди найденых
    и точных значений'''
    mx = module(Vficislen[1] - fTochn[1])
    for i in range(len(X)):
        if Vficislen[i] != 'NON' and module(Vficislen[i] - fTochn[i]) > mx:
            mx = module(Vficislen[i] - fTochn[i])
    return mx
def leftDifFormul(F, h):
    '''Формула левых прямоугольников'''
    fVicislitelen = []

    fVicislitelen += ['NON']
    for x in range(1, len(F)):
        fVicislitelen += [(F[x]-F[x-1]) / h]
    return fVicislitelen
def rightDifFormul(F, h):
    '''Формула правых прямоугольников'''
    fVicislitelen = []

    for x in range(len(F)-1):
        fVicislitelen += [(F[x+1]-F[x]) / h]
    fVicislitelen += ['NON']
    return fVicislitelen
def midlDifFormul(F, h):
    '''Формула средних прямоугольников'''
    fVicislitelen = []

    fVicislitelen += ['NON']
    for x in range(1, len(F)-1):
        fVicislitelen += [(F[x+1]-F[x-1]) / (2*h)]
    fVicislitelen += ['NON']
    return fVicislitelen

def f(a):
    '''Подынтегральная функция'''
    return math.sin(a)
def F(a):
    '''Интеграл функции'''
    return math.cos(a)

def main():
    # Создаем точки Х
    a, b, h = -5.0, 0.5, 0.5
    X=[]
    p = a
    while p <= b:
        X += [p]
        p += h

    fNotDif = [f(x) for x in X]
    fDif = [F(x) for x in X]

    one = leftDifFormul(fNotDif, h)
    two = rightDifFormul(fNotDif, h)
    three = midlDifFormul(fNotDif, h)
    print('*'*30, 'Левая', '*'*30, sep='')
    outTable(X, one, fDif)
    print('*'*30, 'Правая', '*'*30, sep='')
    outTable(X, two, fDif)
    print('*'*30, 'Центральная','*'*30, sep='')
    outTable(X, three, fDif)

    print('Максимальный разброс:')
    print('Правая: ', '\t', maxdifference(X, one, fDif), '\n',
          'Левая:  ', '\t', maxdifference(X, two, fDif), '\n',
          'Центральная: ', '\t', maxdifference(X, three, fDif), sep='' )

if __name__ == '__main__':
    main()
