import math
def abs(a): return a if a > 0 else -a

def fun1X(x, y):
    return x**2 + y**2 - 9
def derivative1(x, y):
    return 2*x + 2*y

def fun2Y(x, y):
    return math.sin(x) + 1 - y
def derivative2(x, y):
    return math.cos(x) - 1

def totalFun(a, b, E=10**(-20)):
    '''(Решение методом Ньютона)
    Начальная система:
        x^2 + y^2 = 9;
        sin(x) + 1 = y;'''
    X, Y = [a], [b]
    while True:
        X += [X[-1] - fun1X(X[-1], Y[-1]) / derivative1(X[-1], Y[-1])]
        Y += [Y[-1] - fun2Y(X[-2], Y[-1]) / derivative2(X[-2], Y[-1])]
        if abs(X[-1] -X[-2]) <= E and abs(Y[-1] -Y[-2]) <= E: break
    return X, Y

def main():
    X, Y = totalFun(2.6, 1.48)
    print(f'(Ньютон)\nКоличество х: {len(X)}\tКоличиство y:{len(Y)}\nx(k-1): {X[-1]}\ty(k-1): {Y[-1]}\n')
    print(f'Подставими в уравнения для проверки(получили почти 0):\n{X[-1]**2+Y[-1]**2-9}=0\n{math.sin(X[-1])+1-Y[-1]}=0')

if __name__ == '__main__':
    main()
