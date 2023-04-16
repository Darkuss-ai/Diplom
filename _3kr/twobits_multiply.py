import algorithms as algo


def change_bits(bits):
    if bits == ['0', '0']:
        return ['0', '1']
    elif bits == ['0', '1']:
        return ['1', '0']
    elif bits == ['1', '0']:
        return ['1', '1']
    else:
        return ['0', '0']


def calculate_bits(x_, y_):
    if x_ + y_ >= 16:
        return 9
    elif x_ + y_ >= 8:
        return 7
    elif x_ + y_ >= 4:
        return 5
    return 3


def Multiply(x, y):
    number_of_bits = calculate_bits(x, y)

    X = algo.convert(x, number_of_bits)
    Y = algo.convert(y, number_of_bits)

    print("X = ", X)
    print("Y = ", Y)
    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)
    print("[-|X|]d = ", minX)
    S = ['0' for i in range(len(X) * 2 - 1)]
    interval_left = len(Y) - 2
    interval_right = len(Y)
    corr = 0
    algo.bit_depth = len(S)
    for i in range((len(Y) - 1) // 2):
        two_bits = Y[interval_left:interval_right]
        if corr == 1:
            two_bits = change_bits(two_bits)
            if two_bits == ["0", "0"]:
                corr = 1
            else:
                corr = 0
        if two_bits == ['0', '0']:
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
        elif two_bits == ["0", '1']:
            S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
        elif two_bits == ['1', '1']:
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
            corr = 1
        else:
            new_X = algo.shift(X.copy(), 'str' if X[0] == '0' else 'rev', 1)
            S = algo.addition(S, new_X, len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)

        interval_left -= 2
        interval_right -= 2

    if Y[0] == '0' and corr == 1:
        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
    elif Y[0] == '1' and corr == 1:
        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
    elif Y[0] == "1" and corr == 0:
        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))
        print(S)

    print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
          str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))


Multiply(43, 45)
