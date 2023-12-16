import math

countIter = 0 # Если нужно количество делений

def abs(x): return x if x > 0 else -x
def f(x): return x**3

def formulaSrednishPriam(a, b, h) -> float:
    '''Считает интеграл на отрезке [a,b] с шагом h
    по формуле средних треугольников'''
    global countIter
    countIter = 0

    resultSum = 0
    while a < b:
        resultSum += f((2*a+h)/2) * h
        a += h
        countIter += 1
    return resultSum

def integral(a, b, e) -> float:
    '''Считает приближенный интеграл интеграл
    на отрезке [a,b] с заданной точностью e'''
    m, h = 0, abs(a)+abs(b)
    l = [formulaSrednishPriam(a, b, h)] # Первый интеграл (без разбиения)

    m, h = 1, (abs(a)+abs(b)) / 2
    while True:
        l += [formulaSrednishPriam(a, b, h)]
        if abs(l[-1] - l[-2]) < e:
            break
        m += 1
        h = (abs(a)+abs(b))/2**m
    return l[-1]

def main():
    a, b, e =0, 1, 10**(-4)
    # Смотрим на изменения в динамике при увилечении точности
    for i in range(-1,-12,-1):
        print(f'При e^{i}: {integral(a, b, 10**i)} ({countIter})')

if __name__ == '__main__':
    main()
