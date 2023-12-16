
import math

def abs(a): return a if a > 0 else -a

def fun(x):
    return math.sin(x)

def main(E=10**(-5)):
    '''Нелинейного уравнения 1-го рода
    Для уравнения: 3X^3 + 5X = 2 '''
    x = [math.pi/4]
    p = True
    while p:
        x += [fun(x[-1])]
        if abs(x[-1] -x[-2]) <= E:
            p = False

    print(f'Количество х: {len(x)}\nx(k-1): {x[-1]}')

if __name__ == '__main__':
    main()
