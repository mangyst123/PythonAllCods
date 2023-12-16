def printConsole(X, F, xOut, L):
    print(f"Начальные точки и значения функции в них:", '\n', *X, '\n', *F)
    print(f"Итоговая таблица (x  f):")
    for i in range(len(X)-1):
        print(X[i], '\t', F[i])
        print(xOut[i], '\t', L[i])
    print(X[-1], '\t', F[-1])

def main():
    X = [-2, -1, 0, 2]
    F = [-8, -1, 0, 8]

    xOut = []
    L = []

    for x,y in zip(X, X[1:]):
        xOut += [(x+y)/2]
        L += [0]

    for i in range(len(xOut)):
        for k in range(len(xOut)+1):
            prod = 1
            for g in range(len(X)):
                if g != k:
                    prod *= (xOut[i] - X[g]) / (X[k]- X[g])
            L[i] += F[k]*prod

    printConsole(X, F, xOut, L)
if __name__ == '__main__':
    main()
