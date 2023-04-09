import algorithms as algo


def generate_A(numb, bit_depth):
    for i in range(len(numb), bit_depth + 1):
        numb.append("0")
    return numb


def generate_S(numb, bit_depth):
    for i in range(len(numb), bit_depth + 1):
        numb.append("0")
    return numb


def generate_P(numb, bit_depth):
    # zero_len = bit_depth - len(numb)
    # P = ['0' for i in range(zero_len)]
    # for i in numb:
    #     P.append(i)
    # P.append("0")
    P = ["0" for i in range(bit_depth + 1)]
    return P


def Boota():
    algo.bit_depth = 6

    M = 21
    R = 16

    m = algo.convert(M)
    r = algo.convert(R)
    minus_m = algo.dop(-M)

    print(m, minus_m, r)

    algo.bit_depth = algo.bit_depth * 2 - 1

    A = generate_A(m.copy(), algo.bit_depth)
    S = generate_S(minus_m.copy(), algo.bit_depth)
    P = generate_P(r.copy(), algo.bit_depth)

    print(A, S, P)
    x = len(r) - 2
    y = len(r)
    for i in range(len(r) - 2):
        if i == 0:
            two_bits = r[x:]
            print(two_bits)

        else:
            two_bits = r[x:y]
            print(two_bits)

        if two_bits == ["1", "0"]:
            P = algo.addition(P, S, algo.bit_depth, kr=3)

        elif two_bits == ["0", "1"]:
            P = algo.addition(P, A, algo.bit_depth, kr=3)

        if i != len(m) - 1:
            P = algo.shift(P, "str" if P[0] == '0' else "rev", -1)
        x = x - 1
        y = y - 1

    P.pop()
    print(P)
    result = algo.convert(algo.reverse(P)) - 1 if P[0] == "1" else algo.convert(P)
    print(str(result) + '/' + str(2 ** (algo.bit_depth - 1)))



