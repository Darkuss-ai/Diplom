import algorithms as algo

x = -14
y = 14

X = algo.convert(x, algo.bit_depth / 2 + 1)
Y = algo.convert(y, algo.bit_depth / 2 + 1)

dopX = algo.dop(x, algo.bit_depth / 2 + 1)
dopY = algo.dop(y, algo.bit_depth / 2 + 1)

minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

S = ['0' for i in range(len(X) * 2 - 1)]

print("X = ", X)
print("Y = ", Y)
print("Xdop = ", dopX)
print("Ydop = ", dopY)
print("-[X]d = ", minX)

for i in range(len(Y)):
    anal_bit = dopY[i]
    if anal_bit == '1' and i == 0:
        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
    elif anal_bit == '1':
        S = algo.addition(S, dopX.copy(), len(X) * 2 - 1, code='dop', kr=3)
    dopX.insert(1, X[0])

if S[0] == '1':
    S = algo.dop(algo.convert(S, len(S)), len(S))
    print(S)

print(str(algo.convert(X)) + '/' + str(2 ** (len(X) - 1)), str(algo.convert(Y)) + '/' + str(2 ** (len(Y) - 1)),
      str(algo.convert(S)) + '/' + str(2 ** (len(S) - 1)))
