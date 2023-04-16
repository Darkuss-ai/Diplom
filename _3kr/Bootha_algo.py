import algorithms as algo
from math import log2


def generate_A(numb, bit_depth):
    for i in range(len(numb), bit_depth + 1):
        numb.append("0")
    return numb


def generate_S(numb, bit_depth):
    for i in range(len(numb), bit_depth + 1):
        numb.append("0")
    return numb


def generate_P(numb, bit_depth):
    zero_len = bit_depth - len(numb)
    P = ['0' for i in range(zero_len)]
    for i in numb:
        P.append(i)
    P.append("0")
    #P = ["0" for i in range(bit_depth + 1)]
    return P


def calculate_bits(x_, y_):
    if x_ + y_ >= 16:
        return 6
    elif x_ + y_ >= 8:
        return 4
    elif x_ + y_ >= 4:
        return 2
    return 3


def Boota(x, y):
    number_of_bits = calculate_bits(x, y) + 2
    X = algo.convert(x, number_of_bits)
    Y = algo.convert(y, number_of_bits)

    print("X = ", X)
    print("Y = ", Y)

    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

    print("[-|X|]d = ", minX)

    S = ['0' for m in range(len(X) * 2 - 1)]

    interval_left = len(Y) - 2
    interval_right = len(Y)

    algo.bit_depth = len(S)

    for i in range(len(Y) - 2):
        two_bits = Y[interval_left:interval_right]
        print(two_bits)

        if two_bits == ['1', '0']:
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)
        elif two_bits == ['0', '1']:
            S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)
        else:
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)

        interval_left -= 1
        interval_right -= 1

    print(S)

    print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
          str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))


def Boota_test(x, y):
    number_of_bits = calculate_bits(x, y)
    X = algo.convert(x, number_of_bits)
    Y = algo.convert(y, number_of_bits)
    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)
    A = generate_A(X.copy(), len(X) * 2)
    S = generate_S(minX.copy(), len(X) * 2)
    P = generate_P(algo.Fullreverse(X.copy()), len(X) * 2)

    print("X = ", X)
    print("Y = ", Y)


    print("[-|X|]d = ", minX)
    print("A = ", A)
    print("S = ", S)


    print("P = ", P)


    for i in range(len(Y)):
        two_bits = P[-2:]
        print(two_bits)

        if two_bits == ['1', '0']:
            P = algo.addition(P, S.copy(), len(X) * 2 - 1, code='dop', kr=3)
            P = algo.shift(P, 'str' if S[0] == '0' else 'rev', -1)
        elif two_bits == ['0', '1']:
            P = algo.addition(P, A.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
            P = algo.shift(P, 'str' if S[0] == '0' else 'rev', -1)
        else:
            P = algo.shift(P, 'str' if P[0] == '0' else 'rev', -1)

    P.pop()
    if P[0] == '1':
        P = algo.dop(algo.convert(P, len(P)))
    print(P)

    print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
          str(algo.convert(P)) + '/' + str(2 ** (len(P) - 1)))


#Boota(21, 11)
Boota_test(4, 5)
