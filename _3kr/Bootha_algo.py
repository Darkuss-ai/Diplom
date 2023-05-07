import algorithms as algo

def calculate_bits(x_, y_):
    if abs(x_) + abs(y_) >= 16:
        return 6
    elif abs(x_) + abs(y_) >= 8:
        return 5
    elif abs(x_) + abs(y_) >= 4:
        return 4
    return 3


def Boota(x, y):
    number_of_bits = calculate_bits(x, y)
    X = algo.convert(x, number_of_bits)
    Y = algo.convert(y, number_of_bits)

    print("X = ", X)
    print("Y = ", Y)

    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

    print("[-|X|]d = ", minX)

    S = ['0' for m in range(len(X) * 2 - 1)]

    Y.append('0')

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

    Y.pop()

    if S[0] == '1':
        S = algo.dop(algo.convert(S, len(S)), len(S))
        print(S)

    print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
          str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))


Boota(8, 15)
