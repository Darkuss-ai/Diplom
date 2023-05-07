import algorithms as algo

x = 13
y = 14

X = algo.convert(x, algo.bit_depth / 2 + 1)
Y = algo.convert(y, algo.bit_depth / 2 + 1)

dopY = algo.dop(y, algo.bit_depth / 2 + 1)

Z = []
S = ['0' for j in range(len(X) * 2 - 1)]

minYdop = algo.Fullreverse(dopY.copy())
minYdop = algo.addition(minYdop, ['1'], code='dop', bits=len(minYdop))

print("X = ", X)
print("Y = ", Y)
print("[Y]d = ", minYdop)

for i in range(len(Y) - 1):
    if i == 0:
        S = algo.addition(X.copy(), minYdop.copy(), len(X) * 2 - 1, code='dop', kr=3)
        if algo.convert(S.copy()) < 0:
            Z.append('0')
            S = algo.addition(S, Y.copy(), len(X) * 2 - 1, code='dop', kr=3)
        else:
            exit("Overflow")
    minYdop.insert(1, minYdop[0])
    S.append("0")
    S = algo.addition(S, minYdop.copy(), len(X) * 2 - 1, code="dop", kr=3)
    Y.insert(1, Y[0])
    if algo.convert(S.copy()) > 0:
        Z.append('1')
    else:
        Z.append("0")
        S = algo.addition(S, Y.copy(), len(X) * 2 - 1, code='dop', kr=3)

if Z[0] == '1':
    Z = algo.rev(algo.convert(Z, len(Z)), len(Z))

print(Z)
print("Answer is " + str(x / y))
print("My answer is " + str(algo.convert(Z)) + '/' + str(2 ** (len(X) - 1)) + '=' + str(algo.convert(Z) / 2 ** (len(X) - 1)))
print("Error is " + str((x / y) - (algo.convert(Z) / 2 ** (len(X) - 1))))
