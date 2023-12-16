def factorial(a):
    fin = a
    for i in range(1,a):
        fin *= i
    return fin
def module(a):
    return a if a > 0 else -a

def main():
    # Начальные значения
    epsilon, a, b, h = 10**(-3), -4, 4, 0.25
    X = list()# Точки
    N0 = list() # Количество слогаемых для каждой точки
    Sn = list() # Значение функций в точках
    # Вспомогательные переменные
    p = a
    s = []

    while p < b:
        s += [p]
        p += h
    for x in range(len(s)):
        X += [s[x]]
        N0 += [0]
        Sn += [0]

    for i in range(len(X)):
        step, znak = 1, 1 # Знак '-' или '+'
        # a - слогаемое
        slog = X[i]**step/factorial(step) # Первое слогаемое в моем случае есть всегда
        while module(slog) >= epsilon: # Суммирование пока больше Epsilon
            Sn[i] += slog
            N0[i] += 1
            step += 2
            znak *= -1
            slog = znak*X[i]**step/factorial(step)
    print('Точка', 'Значение', '\tКоличество итераций', sep='\t')
    for x in range(len(X)):
        print(X[x], Sn[x] ,N0[x], sep='\t')

if __name__ == '__main__':
    main()
