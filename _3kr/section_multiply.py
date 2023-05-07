import algorithms as algo


def section_multiply(_x, _y):
    x = _x
    y = _y
    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)
    minX = algo.Fullreverse(X.copy())

    print("X = ", X)
    print("Y = ", Y)
    print("-[X]d = ", minX)

    S = ['0' for m in range(len(X) * 2 - 1)]

    while len(minX) != len(S):
        minX.append(minX[0])

    for m in range(1, len(Y)):
        anal_bit = Y[m]
        minX = algo.shift(minX, "rev", -1)
        if anal_bit == '1':
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='rev', kr=3)

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))
        print(S)

    print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
          str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))


section_multiply(12, -5)
