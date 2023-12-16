import math
def abs(a): return a if a > 0 else -a

def fun1X(x, y):
    return -(9 - y**2)**0.5
def fun2Y(x, y):
    return math.sin(x) + 1

def printResult(X, Y):
    print(f'Начальные значения:\nx = {X[0]}\ty = {Y[0]}')
    print('Все полученные (х, y): ')
    for x in range(1, len(X)):
        print('x =', X[x],'\t', 'y =', Y[x])

def totalFun(a, b, E=10**(-10)):
    '''(Решение методом простых итераций)
    Начальная система:
        x^2 + y^2 = 9;
        sin(x) + 1 = y;'''
    X, Y = [a], [b]

    while True:
        X += [fun1X(X[-1], Y[-1])]
        Y += [fun2Y(X[-2], Y[-1])]
        if abs(X[-1] -X[-2]) <= E and abs(Y[-1] -Y[-2]) <= E:
            break
    return X, Y

def main():
    X, Y = totalFun(2.62, 1.52)
    print(f'(Простой)\nКоличество х и y: {len(X)}\nx(k-1): {X[-1]}\ty(k-1): {Y[-1]}\n')
    print(f'Подставими в уравнения для проверки:\n{X[-1]**2+Y[-1]**2-9}=0\n{math.sin(X[-1])+1-Y[-1]}=0')

if __name__ == '__main__':
    main()
